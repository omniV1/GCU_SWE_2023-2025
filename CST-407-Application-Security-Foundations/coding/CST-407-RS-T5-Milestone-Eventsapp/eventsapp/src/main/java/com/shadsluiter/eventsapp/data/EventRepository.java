package com.shadsluiter.eventsapp.data;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.support.GeneratedKeyHolder;
import org.springframework.jdbc.support.KeyHolder;
import org.springframework.stereotype.Repository;

import com.shadsluiter.eventsapp.models.EventEntity;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.List;

@Repository
public class EventRepository implements EventRepositoryInterface {

  private final JdbcTemplate jdbcTemplate;

  @Autowired
  public EventRepository(JdbcTemplate jdbcTemplate) {
    this.jdbcTemplate = jdbcTemplate;
  }

  @Override
  public List<EventEntity> findByOrganizerid(Long organizerid) {
    // VULNERABLE (demo): String sql = "SELECT * FROM events WHERE organizerid = " +
    // organizerid;
    String sql = "SELECT * FROM events WHERE organizerid = ?";
    return jdbcTemplate.query(sql, new EventModelRowMapper(), organizerid);
  }

  @Override
  public List<EventEntity> findAll() {
    // VULNERABLE (demo): String sql = "SELECT * FROM events";
    String sql = "SELECT * FROM events";
    return jdbcTemplate.query(sql, new EventModelRowMapper());
  }

  @Override
  public void deleteById(Long id) {
    // VULNERABLE (demo): String sql = "DELETE FROM events WHERE id = " + id;
    jdbcTemplate.update("DELETE FROM events WHERE id = ?", id);
  }

  @Override
  public EventEntity save(EventEntity event) {
    if (event.getId() == null) {
      // VULNERABLE (demo):
      // String sql = "INSERT INTO events (name, date, location, organizerid,
      // description) VALUES ('"
      // + event.getName() + "', '" + event.getDate() + "', '" + event.getLocation() +
      // "', '"
      // + event.getOrganizerid() + "', '" + event.getDescription() + "')";
      String sql = "INSERT INTO events (name, date, location, organizerid, description) VALUES (?, ?, ?, ?, ?)";
      KeyHolder keyHolder = new GeneratedKeyHolder();
      jdbcTemplate.update(connection -> {
        PreparedStatement ps = connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
        ps.setString(1, event.getName());
        ps.setDate(2, event.getDate());
        ps.setString(3, event.getLocation());
        ps.setString(4, event.getOrganizerid());
        ps.setString(5, event.getDescription());
        return ps;
      }, keyHolder);
      if (keyHolder.getKey() != null) {
        event.setId(keyHolder.getKey().longValue());
      }
    } else {
      // VULNERABLE (demo):
      // String sql = "UPDATE events SET name = '" + event.getName() + "', date = '" +
      // event.getDate()
      // + "', location = '" + event.getLocation() + "', organizerid = '" +
      // event.getOrganizerid()
      // + "', description = '" + event.getDescription() + "' WHERE id = " +
      // event.getId();
      String sql = "UPDATE events SET name = ?, date = ?, location = ?, organizerid = ?, description = ? WHERE id = ?";
      jdbcTemplate.update(sql,
          event.getName(),
          event.getDate(),
          event.getLocation(),
          event.getOrganizerid(),
          event.getDescription(),
          event.getId());
    }
    return event;
  }

  @Override
  public EventEntity findById(Long id) {
    // VULNERABLE (demo): String sql = "SELECT * FROM events WHERE id = " + id;
    String sql = "SELECT * FROM events WHERE id = ?";
    try {
      return jdbcTemplate.queryForObject(sql, new EventModelRowMapper(), id);
    } catch (EmptyResultDataAccessException ex) {
      return null;
    }
  }

  @Override
  public boolean existsById(Long id) {
    String sql = "SELECT COUNT(*) FROM events WHERE id = ?";
    Integer count = jdbcTemplate.queryForObject(sql, Integer.class, id);
    return count != null && count > 0;
  }

  private static class EventModelRowMapper implements RowMapper<EventEntity> {
    @Override
    public EventEntity mapRow(ResultSet rs, int rowNum) throws SQLException {
      EventEntity event = new EventEntity();
      event.setId(rs.getLong("id"));
      event.setName(rs.getString("name"));
      event.setDate(rs.getDate("date"));
      event.setLocation(rs.getString("location"));
      event.setOrganizerid(rs.getString("organizerid"));
      event.setDescription(rs.getString("description"));
      return event;
    }
  }

  @Override
  public List<EventEntity> findByDescription(String description) {
    // VULNERABLE (demo): String sql = "SELECT * FROM events WHERE description LIKE
    // '%" + description + "%'";
    String sql = "SELECT * FROM events WHERE description LIKE ?";
    String searchTerm = description == null ? "" : description.trim();
    return jdbcTemplate.query(sql, new EventModelRowMapper(), "%" + searchTerm + "%");
  }
}

package com.shadsluiter.ordersapp.data;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

import com.shadsluiter.ordersapp.models.UserEntity;

@Repository
public class UsersDAO {


    private final String url = "jdbc:mysql://localhost:3306/orders-app";
    private final String username = "root";
    private final String password = "root";

    public List<UserEntity> findAll() {
        List<UserEntity> users = new ArrayList<>();
        String sql = "SELECT * FROM users";

        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                UserEntity user = new UserEntity();
                user.setId(rs.getLong("id"));
                user.setLoginName(rs.getString("username"));
                user.setPassword(rs.getString("password"));
                users.add(user);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return users;
    }

    public UserEntity findById(Long id) {
        UserEntity user = null;
        String sql = "SELECT * FROM users WHERE id = " + id;  // Vulnerable to SQL injection
    
        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
    
            if (rs.next()) {
                user = new UserEntity();
                user.setId(rs.getLong("id"));
                user.setLoginName(rs.getString("username"));
                user.setPassword(rs.getString("password"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return user;
    }

    public UserEntity findByLoginName(String loginName) {
        UserEntity user = null;
        String sql = "SELECT * FROM users WHERE username = '" + loginName + "'";  // Vulnerable to SQL injection
    
        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
    
            if (rs.next()) {
                user = new UserEntity();
                user.setId(rs.getLong("id"));
                user.setLoginName(rs.getString("username"));
                user.setPassword(rs.getString("password"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return user;
    }

    public void save(UserEntity user) {
        String sql = "INSERT INTO users (username, password) VALUES ('" + user.getLoginName() + "', '" + user.getPassword() + "')";  // Vulnerable to SQL injection

        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement()) {

            stmt.executeUpdate(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void update(UserEntity user) {
        String sql = "UPDATE users SET username = '" + user.getLoginName() + "', password = '" + user.getPassword() + "' WHERE id = " + user.getId();  // Vulnerable to SQL injection

        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement()) {

            stmt.executeUpdate(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void delete(Long id) {
        String sql = "DELETE FROM users WHERE id = " + id;  // Vulnerable to SQL injection

        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement()) {

            stmt.executeUpdate(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
 
    
}

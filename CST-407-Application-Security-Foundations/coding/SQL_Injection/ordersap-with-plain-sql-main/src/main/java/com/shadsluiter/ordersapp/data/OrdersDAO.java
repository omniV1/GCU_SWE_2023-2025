package com.shadsluiter.ordersapp.data; 

import com.shadsluiter.ordersapp.models.OrderEntity;
import org.springframework.stereotype.Repository;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

@Repository
public class OrdersDAO {

    private final String url = "jdbc:mariadb://localhost:3306/orders-app?allowMultiQueries=true";
    private final String username = "root";
    private final String password = "root";

    public List<OrderEntity> findAll() {
        List<OrderEntity> orders = new ArrayList<>();
        String sql = "SELECT * FROM orders";

        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                OrderEntity order = new OrderEntity();
                order.setId(rs.getLong("id"));
                order.setDate(rs.getDate("date"));
                order.setCustomerid(rs.getLong("customerid"));
                order.setNotes(rs.getString("notes"));
                orders.add(order);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return orders;
    }

    public OrderEntity findById(Long id) {
        OrderEntity order = null;
        String sql = "SELECT * FROM orders WHERE id = " + id;  // Vulnerable to SQL injection
    
        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
    
            if (rs.next()) {
                order = new OrderEntity();
                order.setId(rs.getLong("id"));
                order.setDate(rs.getDate("date"));
                order.setCustomerid(rs.getLong("customerid"));
                order.setNotes(rs.getString("notes"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return order;
    }
    

    public OrderEntity save(OrderEntity order) {
        String sql = "INSERT INTO orders (date, customerid, notes) VALUES ('"
            + new java.sql.Date(order.getDate().getTime()) + "', "
            + order.getCustomerid() + ", '"
            + order.getNotes() + "')";  // Vulnerable to SQL injection
    
        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement()) {
        int result =  stmt.executeUpdate(sql, Statement.RETURN_GENERATED_KEYS);
        if (result == 1) {
            ResultSet rs = stmt.getGeneratedKeys();
            if (rs.next()) {
                order.setId(rs.getLong(1));
            }
            return order;
        }
        } catch (SQLException e) {
            e.printStackTrace();
        } 
        return null;
    }
    
    public void update(OrderEntity order) {
        String sql = "UPDATE orders SET date = '" + new java.sql.Date(order.getDate().getTime()) 
            + "', customerid = " + order.getCustomerid() 
            + ", notes = '" + order.getNotes() 
            + "' WHERE id = " + order.getId();  // Vulnerable to SQL injection
    
        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement()) {
    
            stmt.executeUpdate(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    

    public void delete(Long id) {
        String sql = "DELETE FROM orders WHERE id = " + id;  // Vulnerable to SQL injection
    
        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement()) {
    
            stmt.executeUpdate(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public ArrayList<OrderEntity> findByCustomerId(Long id) {
        ArrayList<OrderEntity> orders = new ArrayList<>();
        String sql = "SELECT * FROM orders WHERE customerid = " + id;  // Vulnerable to SQL injection
    
        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
    
            while (rs.next()) {
                OrderEntity order = new OrderEntity();
                order.setId(rs.getLong("id"));
                order.setDate(rs.getDate("date"));
                order.setCustomerid(rs.getLong("customerid"));
                order.setNotes(rs.getString("notes"));
                orders.add(order);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return orders;
    }

    public ArrayList<OrderEntity> findBySearch(String search) {
        ArrayList<OrderEntity> orders = new ArrayList<>();
        String sql = "SELECT * FROM `orders` WHERE `notes` LIKE '%" + search + "%'";  // Vulnerable to SQL injection
        System.out.println("findBySearch: " + sql);
        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
    
            while (rs.next()) {
                OrderEntity order = new OrderEntity();
                order.setId(rs.getLong("id"));
                order.setDate(rs.getDate("date"));
                order.setCustomerid(rs.getLong("customerid"));
                order.setNotes(rs.getString("notes"));
                orders.add(order);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return orders;
    }

    // public List<OrderEntity> findBySearch(String search) {
    //     List<OrderEntity> orders = new ArrayList<>();
    //     String sql = "SELECT * FROM orders WHERE notes LIKE ?";  // Use parameterized query
    
    //     try (Connection conn = DriverManager.getConnection(url, username, password);
    //          PreparedStatement pstmt = conn.prepareStatement(sql)) {
    
    //         pstmt.setString(1, "%" + search + "%");
    //         try (ResultSet rs = pstmt.executeQuery()) {
    //             while (rs.next()) {
    //                 OrderEntity order = new OrderEntity();
    //                 order.setId(rs.getLong("id"));
    //                 order.setDate(rs.getDate("date"));
    //                 order.setCustomerid(rs.getLong("customerid"));
    //                 order.setNotes(rs.getString("notes"));
    //                 orders.add(order);
    //             }
    //         }
    //     } catch (SQLException e) {
    //         e.printStackTrace();
    //     }
    //     return orders;
    // }
    
    
}

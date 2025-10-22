package edu.gcu.cst407.jwt.dto;

import java.math.BigDecimal;
import java.time.LocalDate;

public class OrderResponse {

    private Long id;
    private String description;
    private BigDecimal total;
    private LocalDate orderDate;
    private String createdBy;

    public OrderResponse() {
    }

    public OrderResponse(Long id, String description, BigDecimal total, LocalDate orderDate, String createdBy) {
        this.id = id;
        this.description = description;
        this.total = total;
        this.orderDate = orderDate;
        this.createdBy = createdBy;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public BigDecimal getTotal() {
        return total;
    }

    public void setTotal(BigDecimal total) {
        this.total = total;
    }

    public LocalDate getOrderDate() {
        return orderDate;
    }

    public void setOrderDate(LocalDate orderDate) {
        this.orderDate = orderDate;
    }

    public String getCreatedBy() {
        return createdBy;
    }

    public void setCreatedBy(String createdBy) {
        this.createdBy = createdBy;
    }
}

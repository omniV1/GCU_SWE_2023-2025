package com.shadsluiter.ordersapp.models;

import java.util.Date;

import org.springframework.format.annotation.DateTimeFormat;

public class OrderModel {

    private String id;
    
    @DateTimeFormat(pattern = "yyyy-MM-dd")
    private Date date;
    private String customerid;
    private String notes;

    public OrderModel() {
    }

    public OrderModel(String id, Date date, String customerid, String notes) {
        this.id = id;
        this.date = date;
        this.customerid = customerid;
        this.notes = notes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date2) {
        this.date = date2;
    }

    public String getCustomerid() {
        return customerid;
    }

    public void setCustomerid(String id) {
        this.customerid = id;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
    
}

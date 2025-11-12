package edu.shadsluiter.comments.models;

public class Comment { 
    private int id;
    private String author;
    private String text;

    public Comment() {
    }

    public Comment(int id, String author, String text) {
        this.id = id;
        this.author = author;
        this.text = text;
    }

    public String getAuthor() {
        return author;
    }

    public String getText() {
        return text;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public void setText(String text) {
        this.text = text;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    
}

package edu.shadsluiter.comments.service;

import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.stream.Collectors;

import org.owasp.encoder.Encode;
import org.springframework.stereotype.Service;

import edu.shadsluiter.comments.models.Comment;

@Service
public class CommentService {

    private final List<Comment> comments = new CopyOnWriteArrayList<>(); // CopyOnWriteArrayList is thread-safe
    private int id = 0;
    private int maxId = 0;


    public CommentService () {

        if (comments.isEmpty()) {
            addInitialComments();
        }
    }
       

    private void addInitialComments() {
        comments.add(new Comment(1, "Alice", "This is a comment from Alice"));
        comments.add(new Comment(2, "Bob", "This is a comment from Bob"));
        comments.add(new Comment(3, "Charlie", "This is a comment from Charlie"));
    }


    public List<Comment> getComments() {
        return comments;
    }

    public void addComment(Comment comment) {
        int newId = 0;
       // find new max
        for (Comment c : comments) {
            if (c.getId() > maxId) {
                maxId = c.getId();
            }
        }
        newId = maxId + 1;
        comment.setAuthor(sanitize(comment.getAuthor()));
        comment.setText(sanitize(comment.getText()));
        comment.setId(newId);
        comments.add(comment);
    }

    public void deleteComment(int id) {
        comments.removeIf(c -> c.getId() == id);
    }

    public void updateComment(int id, Comment comment) {
        for (Comment c : comments) {
            if (c.getId() == id) {
                c.setAuthor(sanitize(comment.getAuthor()));
                c.setText(sanitize(comment.getText()));
                break;
            }
        }
    }

    public Comment getComment(int id) {
        return comments.stream()
            .filter(c -> c.getId() == id)
            .findFirst()
            .orElse(null);
    }

    public List<Comment> searchForComment(String searchPhrase) {
        String lowerCasePhrase = sanitize(searchPhrase).toLowerCase();
        return comments.stream()
            .filter(c -> c.getAuthor().toLowerCase().contains(lowerCasePhrase) ||
                         c.getText().toLowerCase().contains(lowerCasePhrase))
            .collect(Collectors.toList());
    }

    private String sanitize(String input) {
        if (input == null) {
            return "";
        }
        return Encode.forHtmlContent(input.trim());
    }
}

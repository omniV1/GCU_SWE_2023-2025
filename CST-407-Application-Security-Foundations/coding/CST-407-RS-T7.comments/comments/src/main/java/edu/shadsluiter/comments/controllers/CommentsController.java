package edu.shadsluiter.comments.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping; 

import edu.shadsluiter.comments.models.Comment;
import edu.shadsluiter.comments.models.CommentSearchForm;
import edu.shadsluiter.comments.service.CommentService;

@Controller 
public class CommentsController {

    @Autowired  
    CommentService commentService;

    // Get comments from service. Send results to comments.html
    @GetMapping
    public String getComments(Model model) {
        List<Comment> comments = commentService.getComments();
        model.addAttribute("comments", comments);
        model.addAttribute("comment", new Comment());
        return "comments";
    }

    // Show form to add a new comment
    @GetMapping("/add")
    public String showCommentAddForm(Model model) {
        model.addAttribute("comment", new Comment());
        return "add";
    }

    @PostMapping("/add")
    public String addComment(Comment comment, Model model) {
        commentService.addComment(comment);
        model.addAttribute("comments", commentService.getComments());
        return "comments";
    }

    @GetMapping("/edit/{id}")   
    public String showCommentEditForm(@PathVariable int id, Model model) {
        Comment comment = commentService.getComment(id);
        model.addAttribute("comment", comment);
        return "edit";
    }

    @PostMapping("/edit")
    public String editComment(Comment comment, Model model) {
        commentService.updateComment(comment.getId(), comment);
        model.addAttribute("comments", commentService.getComments());
        return "comments";
    }


    // Show form to update an existing comment
    @GetMapping("/updateComment/{id}")
    public String showCommentUpdateForm(@PathVariable int id, Model model) {
        Comment comment = commentService.getComment(id);
        model.addAttribute("comment", comment);
        return "updateComment";
    }

    // Update comment in service. Send results to comments.html
    @PutMapping("/updateComment/{id}")
    public String updateComment(@PathVariable int id, Comment comment, Model model) {
        commentService.updateComment(id, comment);
        model.addAttribute("comments", commentService.getComments());
        return "comments";
    }

    // Show the search form
    @GetMapping("/searchForm")
    public String showSearchForm(Model model) {
        model.addAttribute("commentSearchForm", new CommentSearchForm());
        return "search";
    }

    // Search for a comment in service. Send results to comments.html
    @PostMapping("/searchComment")
    public String searchComment(CommentSearchForm commentSearchForm, Model model) {
        List<Comment> searchResults = commentService.searchForComment(commentSearchForm.getSearchPhrase());
        model.addAttribute("comments", searchResults);
        return "comments";
    }

    @GetMapping("/delete/{id}")
    public String deleteComment(@PathVariable int id, Model model) {
        commentService.deleteComment(id);
        model.addAttribute("comment", new Comment());
        List comments = commentService.getComments();
        model.addAttribute("comments", comments);
        return "comments";
    }
}

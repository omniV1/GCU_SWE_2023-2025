package edu.shadsluiter.comments.models;

public class CommentSearchForm {

    private String searchPhrase;

    public CommentSearchForm() {
    }

    public CommentSearchForm(String searchPhrase) {
        this.searchPhrase = searchPhrase;
    }

    public String getSearchPhrase() {
        return searchPhrase;
    }

    public void setSearchPhrase(String searchPhrase) {
        this.searchPhrase = searchPhrase;
    }
}

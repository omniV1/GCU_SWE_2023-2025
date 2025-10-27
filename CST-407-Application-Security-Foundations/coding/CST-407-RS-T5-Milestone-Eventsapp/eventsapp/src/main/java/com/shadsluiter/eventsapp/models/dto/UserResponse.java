package com.shadsluiter.eventsapp.models.dto;

import java.util.Set;

import com.shadsluiter.eventsapp.models.UserModel;

public class UserResponse {

    private String id;
    private String userName;
    private Set<String> roles;

    public static UserResponse fromModel(UserModel userModel) {
        UserResponse response = new UserResponse();
        response.setId(userModel.getId());
        response.setUserName(userModel.getUserName());
        response.setRoles(userModel.getRoles());
        return response;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public Set<String> getRoles() {
        return roles;
    }

    public void setRoles(Set<String> roles) {
        this.roles = roles;
    }
}

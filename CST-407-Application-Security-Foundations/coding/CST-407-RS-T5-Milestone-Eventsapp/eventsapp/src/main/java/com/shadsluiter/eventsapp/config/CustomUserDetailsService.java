package com.shadsluiter.eventsapp.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.shadsluiter.eventsapp.models.UserEntity;
import com.shadsluiter.eventsapp.service.UserService;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

/**
 * Custom UserDetailsService implementation for Spring Security
 * 
 * This service integrates with the existing UserService to provide
 * authentication functionality for Spring Security. It loads user
 * details from the database and converts them to Spring Security
 * UserDetails objects.
 */
@Service
public class CustomUserDetailsService implements UserDetailsService {

    private final UserService userService;

    /**
     * Constructor injection of UserService
     * 
     * @param userService Service for user operations
     */
    @Autowired
    public CustomUserDetailsService(UserService userService) {
        this.userService = userService;
    }

    /**
     * Load user details by username for authentication
     * 
     * This method is called by Spring Security during the authentication process.
     * It retrieves user information from the database and converts it to a
     * UserDetails object that Spring Security can use for authentication.
     * 
     * @param username The username to load (login name)
     * @return UserDetails object containing user information and authorities
     * @throws UsernameNotFoundException if user is not found
     */
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        // Retrieve user entity from database using UserService
        com.shadsluiter.eventsapp.models.UserModel userModel = userService.findByLoginName(username);
        
        if (userModel == null) {
            throw new UsernameNotFoundException("User not found: " + username);
        }

        // Convert user roles to Spring Security authorities
        Collection<GrantedAuthority> authorities = new ArrayList<>();
        if (userModel.getRoles() != null) {
            for (String role : userModel.getRoles()) {
                authorities.add(new SimpleGrantedAuthority(role));
            }
        }

        // Create and return Spring Security User object
        return User.builder()
                .username(userModel.getUserName())
                .password(userModel.getPassword())
                .authorities(authorities)
                .accountExpired(!userModel.isAccountNonExpired())
                .accountLocked(!userModel.isAccountNonLocked())
                .credentialsExpired(!userModel.isCredentialsNonExpired())
                .disabled(!userModel.isEnabled())
                .build();
    }
}

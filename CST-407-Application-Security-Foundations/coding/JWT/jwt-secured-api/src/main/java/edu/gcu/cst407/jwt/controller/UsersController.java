package edu.gcu.cst407.jwt.controller;

import edu.gcu.cst407.jwt.dto.AuthResponse;
import edu.gcu.cst407.jwt.dto.LoginRequest;
import edu.gcu.cst407.jwt.dto.RegisterRequest;
import edu.gcu.cst407.jwt.dto.UserResponse;
import edu.gcu.cst407.jwt.model.UserAccount;
import edu.gcu.cst407.jwt.security.JwtTokenProvider.AuthToken;
import edu.gcu.cst407.jwt.service.AuthService;
import edu.gcu.cst407.jwt.service.UserService;
import jakarta.validation.Valid;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/users")
public class UsersController {

    private final UserService userService;
    private final AuthService authService;

    public UsersController(UserService userService, AuthService authService) {
        this.userService = userService;
        this.authService = authService;
    }

    @PostMapping("/register")
    public ResponseEntity<UserResponse> register(@Valid @RequestBody RegisterRequest request) {
        UserAccount user = userService.register(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(userService.toResponse(user));
    }

    @PostMapping("/login")
    public ResponseEntity<AuthResponse> login(@Valid @RequestBody LoginRequest request) {
        AuthToken authToken = authService.authenticate(request);
        AuthResponse response = new AuthResponse(authToken.token(), authToken.expiresAt());
        return ResponseEntity.ok(response);
    }

    @GetMapping("/me")
    @SecurityRequirement(name = "bearerAuth")
    public ResponseEntity<UserResponse> currentUser(Authentication authentication) {
        UserAccount user = userService.getUserByUsername(authentication.getName());
        return ResponseEntity.ok(userService.toResponse(user));
    }
}

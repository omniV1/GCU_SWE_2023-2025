package edu.gcu.cst407.jwt.controller;

import edu.gcu.cst407.jwt.dto.OrderRequest;
import edu.gcu.cst407.jwt.dto.OrderResponse;
import edu.gcu.cst407.jwt.service.OrderService;
import jakarta.validation.Valid;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/orders")
@SecurityRequirement(name = "bearerAuth")
public class OrdersController {

    private final OrderService orderService;

    public OrdersController(OrderService orderService) {
        this.orderService = orderService;
    }

    @GetMapping
    public ResponseEntity<List<OrderResponse>> list(Authentication authentication) {
        return ResponseEntity.ok(orderService.findOrdersForUser(authentication.getName()));
    }

    @PostMapping
    public ResponseEntity<OrderResponse> create(
            Authentication authentication,
            @Valid @RequestBody OrderRequest request
    ) {
        OrderResponse response = orderService.createOrder(authentication.getName(), request);
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    @GetMapping("/{id}")
    public ResponseEntity<OrderResponse> get(Authentication authentication, @PathVariable Long id) {
        return ResponseEntity.ok(orderService.findByIdForUser(authentication.getName(), id));
    }

    @PutMapping("/{id}")
    public ResponseEntity<OrderResponse> update(
            Authentication authentication,
            @PathVariable Long id,
            @Valid @RequestBody OrderRequest request
    ) {
        return ResponseEntity.ok(orderService.updateOrder(authentication.getName(), id, request));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(Authentication authentication, @PathVariable Long id) {
        orderService.deleteOrder(authentication.getName(), id);
        return ResponseEntity.noContent().build();
    }
}

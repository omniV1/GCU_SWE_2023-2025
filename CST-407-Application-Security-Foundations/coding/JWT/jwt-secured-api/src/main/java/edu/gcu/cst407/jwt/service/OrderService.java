package edu.gcu.cst407.jwt.service;

import edu.gcu.cst407.jwt.dto.OrderRequest;
import edu.gcu.cst407.jwt.dto.OrderResponse;
import edu.gcu.cst407.jwt.model.CustomerOrder;
import edu.gcu.cst407.jwt.model.UserAccount;
import edu.gcu.cst407.jwt.repository.CustomerOrderRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.NoSuchElementException;
import java.util.stream.Collectors;

@Service
public class OrderService {

    private final CustomerOrderRepository orderRepository;
    private final UserService userService;

    public OrderService(CustomerOrderRepository orderRepository, UserService userService) {
        this.orderRepository = orderRepository;
        this.userService = userService;
    }

    @Transactional(readOnly = true)
    public List<OrderResponse> findOrdersForUser(String username) {
        UserAccount user = userService.getUserByUsername(username);
        return orderRepository.findByUser(user)
                .stream()
                .map(this::toResponse)
                .collect(Collectors.toList());
    }

    @Transactional
    public OrderResponse createOrder(String username, OrderRequest request) {
        UserAccount user = userService.getUserByUsername(username);
        CustomerOrder order = new CustomerOrder(
                request.getDescription(),
                request.getTotal(),
                request.getOrderDate(),
                user
        );
        return toResponse(orderRepository.save(order));
    }

    @Transactional(readOnly = true)
    public OrderResponse findByIdForUser(String username, Long id) {
        CustomerOrder order = orderRepository.findById(id)
                .filter(o -> o.getUser().getUsername().equals(username))
                .orElseThrow(() -> new NoSuchElementException("Order not found: " + id));
        return toResponse(order);
    }

    @Transactional
    public OrderResponse updateOrder(String username, Long id, OrderRequest request) {
        CustomerOrder order = orderRepository.findById(id)
                .filter(o -> o.getUser().getUsername().equals(username))
                .orElseThrow(() -> new NoSuchElementException("Order not found: " + id));
        order.setDescription(request.getDescription());
        order.setTotal(request.getTotal());
        order.setOrderDate(request.getOrderDate());
        return toResponse(order);
    }

    @Transactional
    public void deleteOrder(String username, Long id) {
        CustomerOrder order = orderRepository.findById(id)
                .filter(o -> o.getUser().getUsername().equals(username))
                .orElseThrow(() -> new NoSuchElementException("Order not found: " + id));
        orderRepository.delete(order);
    }

    private OrderResponse toResponse(CustomerOrder order) {
        return new OrderResponse(
                order.getId(),
                order.getDescription(),
                order.getTotal(),
                order.getOrderDate(),
                order.getUser().getFullName()
        );
    }
}

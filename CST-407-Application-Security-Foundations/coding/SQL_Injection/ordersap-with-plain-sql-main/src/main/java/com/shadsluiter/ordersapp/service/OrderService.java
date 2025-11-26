package com.shadsluiter.ordersapp.service; 
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
 
import com.shadsluiter.ordersapp.models.OrderEntity;
import com.shadsluiter.ordersapp.models.OrderModel; 
import com.shadsluiter.ordersapp.data.OrdersDAO;


import java.util.ArrayList;
import java.util.List;

@Service
public class OrderService {

    @Autowired
    private OrdersDAO orderRepository;

    private OrderModel convertToModel(OrderEntity orderEntity) {
        OrderModel orderModel = new OrderModel();
        orderModel.setId(String.valueOf(orderEntity.getId()));
        orderModel.setDate(orderEntity.getDate());
        orderModel.setCustomerid(String.valueOf(orderEntity.getCustomerid()));
        orderModel.setNotes(orderEntity.getNotes());
        return orderModel;
    }

    private OrderEntity convertToEntity(OrderModel orderModel) {
        OrderEntity orderEntity = new OrderEntity();
        if (orderModel.getId() != null) {
            orderEntity.setId(Long.parseLong(orderModel.getId()));
        }
        orderEntity.setDate(orderModel.getDate());
        orderEntity.setCustomerid(Long.parseLong(orderModel.getCustomerid()));
        orderEntity.setNotes(orderModel.getNotes());
        return orderEntity;
    }

    public List<OrderModel> findAll() {
        
        List<OrderEntity> orderEntities = orderRepository.findAll();
        List<OrderModel> orderModels = new ArrayList<>();
        for (OrderEntity orderEntity : orderEntities) {
            orderModels.add(convertToModel(orderEntity));
        }
        return orderModels;
    }

    public List<OrderModel> findBySearchTerm(String searchTerm) {
        List<OrderEntity> orderEntities = orderRepository.findBySearch(searchTerm);
        List<OrderModel> orderModels = new ArrayList<>();
        for (OrderEntity orderEntity : orderEntities) {
            orderModels.add(convertToModel(orderEntity));
        }
        return orderModels;
    }

    public List<OrderModel> findByCustomerid(String customerid) {
        List<OrderEntity> orderEntities = orderRepository.findByCustomerId(Long.valueOf(customerid));
        List<OrderModel> orderModels = new ArrayList<>();
        for (OrderEntity orderEntity : orderEntities) {
            orderModels.add(convertToModel(orderEntity));
        }
        return orderModels; 
    }

    public void save(OrderModel order) { 
        OrderEntity orderEntity = convertToEntity(order);
        orderRepository.save(orderEntity); 
    }

    public void delete(String id) {
        orderRepository.delete(Long.valueOf(id));
    }

    public void updateOrder(String id, OrderModel order) {
        OrderEntity orderEntity = convertToEntity(order);
        orderEntity.setId(Long.valueOf(id)); 
        orderRepository.save(orderEntity);
    }

    public OrderModel findById(String id) {
        OrderEntity orderEntity = orderRepository.findById(Long.valueOf(id));
        if (orderEntity == null) {
            return null;
        }
        return convertToModel(orderEntity);
    }


}


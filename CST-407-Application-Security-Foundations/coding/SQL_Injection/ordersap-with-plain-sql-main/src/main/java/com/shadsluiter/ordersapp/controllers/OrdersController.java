package com.shadsluiter.ordersapp.controllers; 

    import com.shadsluiter.ordersapp.models.OrderModel;
    import com.shadsluiter.ordersapp.service.OrderService;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.stereotype.Controller;
    import org.springframework.ui.Model;
    import org.springframework.web.bind.annotation.*;

    import java.util.List;

    @Controller
    @RequestMapping("/orders") 
public class OrdersController {  
    
        @Autowired
        private OrderService orderService;
    
        @GetMapping
        public String getAllOrders(Model model) {
            List<OrderModel> orders = orderService.findAll();
            model.addAttribute("orders", orders);

            model.addAttribute("pageTitle", "Orders");
            return "orders";
        }
    
        @GetMapping("/create")
        public String showCreateOrderForm(Model model) {
            model.addAttribute("order", new OrderModel());
            model.addAttribute("pageTitle", "Create Order");
            return "create-order";
        }
    
        @PostMapping("/create")
        public String createOrder(@ModelAttribute OrderModel order, Model model) { 
             orderService.save(order); 
            return "redirect:/orders";
        }
    
        @GetMapping("/customer/{customerid}")
        public String getOrdersByCustomerId(@PathVariable String customerid, Model model) {
            List<OrderModel> orders = orderService.findByCustomerid(customerid);
            model.addAttribute("orders", orders);
            return "orders";
        }
    
        @GetMapping("/edit/{id}")
        public String showEditOrderForm(@PathVariable String id, Model model) {
            OrderModel order = orderService.findById(id);
            model.addAttribute("order", order);
            return "edit-order";
        }
    
        @PostMapping("/edit/{id}")
        public String updateOrder(@PathVariable String id, @ModelAttribute OrderModel order, Model model) {
            orderService.updateOrder(id, order);
            return "redirect:/orders";
        }
    
        @GetMapping("/delete/{id}")
        public String deleteOrder(@PathVariable String id) {
            orderService.delete(id);
            return "redirect:/orders";
        }

        @GetMapping("/showSearchForm")
        public String showSearchForm(Model model) {
            model.addAttribute("searchTerm", "");
            model.addAttribute("pageTitle", "Search Orders");
            return "search-form";
        }
    
        @PostMapping("/search")
        public String searchOrders(@RequestParam("searchTerm") String searchTerm, Model model) {
            List<OrderModel> orders = orderService.findBySearchTerm(searchTerm);
            model.addAttribute("orders", orders);
            model.addAttribute("pageTitle", "Search Results");
            return "orders";
        }
}


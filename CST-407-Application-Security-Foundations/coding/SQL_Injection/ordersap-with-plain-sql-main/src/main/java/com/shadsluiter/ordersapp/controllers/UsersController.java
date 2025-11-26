package com.shadsluiter.ordersapp.controllers;

import com.shadsluiter.ordersapp.models.UserModel;
import com.shadsluiter.ordersapp.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/users")
public class UsersController {

    @Autowired
    private UserService userService;

    @GetMapping("/")   
    public String home() {
        return "home";
    }

    // Show registration form
    @GetMapping("/register")
    public String showRegistrationForm(Model model) {
        model.addAttribute("user", new UserModel());
        return "register";
    }

    // Perform registration from form submission
    @PostMapping("/register")
    public String registerUser(@ModelAttribute UserModel user, Model model) {
        if (userService.findByLoginName(user.getLoginName()) != null) {
            model.addAttribute("error", "User already exists!");
            return "register";
        }
        userService.save(user);
        return "redirect:/users/loginForm";
    }
 
  // Show login form
  @GetMapping("/loginForm")
  public String showLoginForm(Model model) {
      model.addAttribute("user", new UserModel());
      model.addAttribute("pageTitle", "Login");
      return "login";
  }

    // Perform login from form submission
    @PostMapping("/login")
    public String authenticateUser(@ModelAttribute UserModel loginRequest, Model model) {
        UserModel user = userService.findByLoginName(loginRequest.getLoginName());
        if (user == null || !user.getPassword().equals(loginRequest.getPassword())) {
            model.addAttribute("error", "Invalid login credentials!");
            return "login";
        }
        model.addAttribute("user", user);
        return "home";
    }

    @GetMapping("/logout")
    public String logout() {
        return "redirect:/users/loginForm";
    }
}

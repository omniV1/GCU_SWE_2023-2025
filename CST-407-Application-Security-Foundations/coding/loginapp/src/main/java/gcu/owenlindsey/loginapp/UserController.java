package gcu.owenlindsey.loginapp;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ModelAttribute;


@Controller
@RequestMapping("/")
public class UserController {

    @GetMapping
   public String showLoginForm(Model model) {
    model.addAttribute("userModel", new UserModel());
    return "loginForm";
   }
    
   @PostMapping("/")
   public String loginUser(@ModelAttribute UserModel userModel, Model model) {
       
       
       if("owen".equals(userModel.getUsername()) && "secretpw".equals(userModel.getPassword())){
        
        // Authentication Success

        model.addAttribute("message", "Login Successful!");
        model.addAttribute("user", userModel);
    } else {

        // Authentication failure 
        
        model.addAttribute("message", "Invalid username or password.");
        model.addAttribute("user", userModel);
    }

    return "loginresult";
   }
}


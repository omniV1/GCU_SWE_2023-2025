package edu.gcu.cst407.jwt.config;

import edu.gcu.cst407.jwt.model.CustomerOrder;
import edu.gcu.cst407.jwt.model.UserAccount;
import edu.gcu.cst407.jwt.repository.CustomerOrderRepository;
import edu.gcu.cst407.jwt.repository.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;

@Configuration
public class DataInitializer {

    @Bean
    CommandLineRunner seedDemoData(UserRepository userRepository,
                                   CustomerOrderRepository orderRepository,
                                   PasswordEncoder passwordEncoder) {
        return args -> {
            if (userRepository.count() == 0) {
                UserAccount alice = new UserAccount(
                        "alice",
                        passwordEncoder.encode("Password!23"),
                        "Alice Anderson",
                        "ROLE_USER"
                );
                UserAccount bob = new UserAccount(
                        "bob",
                        passwordEncoder.encode("Password!23"),
                        "Bob Barnes",
                        "ROLE_USER"
                );
                userRepository.saveAll(List.of(alice, bob));

                orderRepository.saveAll(List.of(
                        new CustomerOrder("Office supplies", new BigDecimal("149.99"), LocalDate.now().minusDays(3), alice),
                        new CustomerOrder("Laptop upgrade", new BigDecimal("1249.00"), LocalDate.now().minusDays(10), alice),
                        new CustomerOrder("Coffee beans subscription", new BigDecimal("39.95"), LocalDate.now().minusDays(1), bob)
                ));
            }
        };
    }
}

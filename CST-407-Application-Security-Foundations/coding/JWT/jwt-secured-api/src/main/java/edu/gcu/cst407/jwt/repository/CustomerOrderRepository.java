package edu.gcu.cst407.jwt.repository;

import edu.gcu.cst407.jwt.model.CustomerOrder;
import edu.gcu.cst407.jwt.model.UserAccount;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface CustomerOrderRepository extends JpaRepository<CustomerOrder, Long> {

    List<CustomerOrder> findByUser(UserAccount user);
}

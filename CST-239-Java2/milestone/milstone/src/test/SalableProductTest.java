package test;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import product.SalableProduct;

public class SalableProductTest {

    private SalableProduct product;

    @BeforeEach
    void setUp() {
    	 product = new SalableProduct("Test Product","bow", "description", 99.99, 10);
        product.setQuantity(10); // Starting with a quantity of 10
    }

    @Test
    void testIncrementQuantity() {
        product.incrementQuantity(5);
        assertEquals(15, product.getQuantity(), "Quantity should be incremented by 5");
    }

    @Test
    void testIncrementQuantityWithNegativeNumber() {
        product.incrementQuantity(-5);
        assertEquals(10, product.getQuantity(), "Quantity should not change when incremented by a negative number");
    }

    @Test
    void testDecrementQuantity() {
        product.decrementQuantity(3);
        assertEquals(7, product.getQuantity(), "Quantity should be decremented by 3");
    }

    @Test
    void testDecrementQuantityWithNegativeNumber() {
        product.decrementQuantity(-3);
        assertEquals(10, product.getQuantity(), "Quantity should not change when decremented by a negative number");
    }

    @Test
    void testDecrementMoreThanAvailable() {
        product.decrementQuantity(15);
        assertEquals(10, product.getQuantity(), "Quantity should not change when trying to decrement more than available");
    }

    @Test
    void testAdjustQuantity() {
        assertTrue(product.adjustQuantity(5), "Should return true when quantity is adjusted positively");
        assertEquals(15, product.getQuantity(), "Quantity should be adjusted by 5");

        assertTrue(product.adjustQuantity(-10), "Should return true when quantity is adjusted to not below zero");
        assertEquals(5, product.getQuantity(), "Quantity should be adjusted by -10");

        assertFalse(product.adjustQuantity(-10), "Should return false when trying to adjust to a negative quantity");
        assertEquals(5, product.getQuantity(), "Quantity should not change when trying to adjust to a negative quantity");
    }
}



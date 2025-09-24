package test;

import static org.junit.jupiter.api.Assertions.*;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;


import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import product.SalableProduct;
import storefront.ShoppingCart;

public class ShoppingCartTest {

    private ShoppingCart cart;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;

    @BeforeEach
    public void setUp() {
        cart = new ShoppingCart();
        System.setOut(new PrintStream(outContent));
    }

    @AfterEach
    public void restoreStreams() {
        System.setOut(originalOut);
    }

    @Test
    public void testAddProduct() {
        SalableProduct product = new SalableProduct("Health Potion", "health_potion", "Restores 50 HP", 10.0, 1);
        assertTrue(cart.addProduct(product, 3), "Product should be added successfully");
        assertEquals(1, cart.getProducts().size(), "There should be one product in the cart");
        assertEquals(3, cart.getProducts().get(0).getQuantity(), "The quantity of the product should be 3");
    }

    @Test
    public void testAddProductInvalidQuantity() {
        SalableProduct product = new SalableProduct("Health Potion", "health_potion", "Restores 50 HP", 10.0, 1);
        assertFalse(cart.addProduct(product, -1), "Product should not be added with negative quantity");
        assertTrue(cart.getProducts().isEmpty(), "Cart should be empty after attempting to add with invalid quantity");
    }

    @Test
    public void testAddProductNullProduct() {
        assertFalse(cart.addProduct(null, 1), "Adding a null product should fail");
        assertTrue(cart.getProducts().isEmpty(), "Cart should be empty after attempting to add a null product");
    }

    @Test
    public void testRemoveProductByName() {
        SalableProduct product = new SalableProduct("Health", "health_potion", "Restores 50 HP", 10.0, 1);
        cart.addProduct(product, 1);
        assertNotNull(cart.removeProductByName("Health"), "Product should be found and removed");
        assertTrue(cart.getProducts().isEmpty(), "Cart should be empty after product removal");
    }

    @Test
    public void testRemoveProductByNameNotFound() {
        assertNull(cart.removeProductByName("Health Potion"), "Trying to remove a non-existing product should return null");
    }

    @Test
    public void testClear() {
        SalableProduct product = new SalableProduct("Health Potion", "health_potion", "Restores 50 HP", 10.0, 1);
        cart.addProduct(product, 1);
        cart.clear();
        assertTrue(cart.getProducts().isEmpty(), "Cart should be empty after clear method is called");
    }

    @Test
    public void testDisplayEmptyCart() {
        cart.display();
        assertEquals("Shopping cart is empty." + System.lineSeparator(), outContent.toString(),
                "Output should indicate that the cart is empty");
    }

    @Test
    public void testDisplayCartWithProducts() {
        SalableProduct product1 = new SalableProduct("Health Potion", "health_potion", "Restores 50 HP", 10.0, 1);
        cart.addProduct(product1, 2);

        cart.display();
        String expectedOutput = "Health Potion - Restores 50 HP - $10.0 x 2" + System.lineSeparator();
        assertEquals(expectedOutput, outContent.toString(),
                "Output should display the product details");
    }
}

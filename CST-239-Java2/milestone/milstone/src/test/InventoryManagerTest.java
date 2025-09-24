package test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.List;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import product.SalableProduct;
import storefront.InventoryManager;
import utils.FileIO; // Assuming FileIO implements FileIOInterface

class InventoryManagerTest {

    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;
    private InventoryManager inventoryManager;

    @BeforeEach
    void setUp() {
        System.setOut(new PrintStream(outContent));
        FileIO fileIO = new FileIO(); // You would mock this if it interacts with the filesystem
        inventoryManager = new InventoryManager(fileIO);
    }

    @AfterEach
    void tearDown() {
        System.setOut(originalOut);
    }

    @Test
    void testAddToInventory() {
        SalableProduct product = new SalableProduct("Mana Potion", "mana_potion", "Restores 50 mana", 5.0, 15);
        inventoryManager.addToInventory(product);
        assertTrue(inventoryManager.getInventory().contains(product), "Product should be added to inventory");
    }

    @Test
    void testDisplayProducts() {
        SalableProduct product1 = new SalableProduct("Mana Potion", "mana_potion", "Restores 50 mana", 5.0, 15);
        SalableProduct product2 = new SalableProduct("Health Potion", "health_potion", "Restores 50 HP", 10.0, 10);
        inventoryManager.addToInventory(product1);
        inventoryManager.addToInventory(product2);

        inventoryManager.displayProducts();

        String expectedOutput = "Available Products:\r\n" + product1.toString() + "\r\n" + product2.toString() + "\r\n";
        assertEquals(expectedOutput, outContent.toString(), "Output should display all products in inventory");
    }

    @Test
    void testGetAllProducts() {
        SalableProduct product1 = new SalableProduct("Mana Potion", "mana_potion", "Restores 50 mana", 5.0, 15);
        SalableProduct product2 = new SalableProduct("Health Potion", "health_potion", "Restores 50 HP", 10.0, 10);
        inventoryManager.addToInventory(product1);
        inventoryManager.addToInventory(product2);

        List<SalableProduct> products = inventoryManager.getAllProducts();
        assertEquals(2, products.size(), "Inventory should have two products");
        assertTrue(products.contains(product1), "Inventory should contain Mana Potion");
        assertTrue(products.contains(product2), "Inventory should contain Health Potion");
    }
}

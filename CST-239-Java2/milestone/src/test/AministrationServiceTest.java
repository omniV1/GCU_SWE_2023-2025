package test;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import admin.AdministrationService;

import org.junit.jupiter.api.AfterEach;
import product.SalableProduct;
import utils.FileIO;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class AdministrationServiceTest {

    private AdministrationService adminService;

    // For capturing System.out output
    private final PrintStream standardOut = System.out;
    private final ByteArrayOutputStream outputStreamCaptor = new ByteArrayOutputStream();

    // Stub FileIO to prevent actual file operations
    class StubFileIO extends FileIO {
        private String fileContent = "";

        @Override
        public String readFromFile(String filePath) {
            return fileContent;
        }

        @Override
        public void writeToFile(String filePath, String content) {
            this.fileContent = content;
        }
    }

    @BeforeEach
    void setUp() {
        // Initialize AdministrationService with the stub FileIO
        FileIO stubFileIO = new StubFileIO();
        adminService = new AdministrationService(stubFileIO);

        // Redirect System.out to capture console output
        System.setOut(new PrintStream(outputStreamCaptor));
    }

    @Test
    void testUpdateProductQuantity() {
        // Add a test product to the inventory
        SalableProduct testProduct = new SalableProduct("TestType", "Test Product", "Test Description", 10.0, 10);
        adminService.inventoryManager.addToInventory(testProduct);

        // Try updating the product quantity
        boolean result = adminService.updateProductQuantity("Test Product", 5);

        // Assert that the product quantity has been updated
        assertTrue(result);
        List<SalableProduct> inventory = adminService.inventoryManager.getInventory();
        assertEquals(15, inventory.get(0).getQuantity());
        assertTrue(outputStreamCaptor.toString().trim().contains("Inventory updated correctly. New quantity for Test Product is 15."));
    }

    @AfterEach
    void tearDown() {
        // Restore System.out
        System.setOut(standardOut);
    }
}

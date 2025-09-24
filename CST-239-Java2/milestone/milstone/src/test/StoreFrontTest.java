package test;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import product.SalableProduct;
import storefront.InventoryManager;
import storefront.StoreFront;
import utils.FileIO;
import utils.FileIOInterface;

import static org.junit.jupiter.api.Assertions.*;

// Other necessary imports

class StoreFrontTest {

    private StoreFront store;
    private InventoryManager inventoryManager;
    private FileIOInterface fileIO;

    @BeforeEach
    void setUp() {
    	 fileIO = new FileIO();// initialize your FileIOInterface implementation here
        inventoryManager = new InventoryManager(fileIO);
        store = new StoreFront(inventoryManager);
        
        // Make sure to load the inventory before tests, or mock fileIO's readFromFile method if needed
        inventoryManager.loadInventory("E:\\cst-239\\\\milstone\\src\\inventory.json");
    }

    @Test
    public void testDisplayProducts() {
        // This method outputs to the console, you would need to capture the stdout if you wanted to test this
        // Otherwise, you could simply check if the displayProducts() calls the right method from InventoryManager
    }

    @Test
    public void testInitialization() {
        // Ensure the inventory is loaded, should contain products if setUp correctly
        assertFalse(inventoryManager.getInventory().isEmpty());
    }

    
   
    @Test
    public void testWriteReceiptToFile() {
        // Assuming that StoreFront has a checkout method that finalizes the purchase and writes the receipt to a file
        String productName = "Nails";
        store.purchaseProduct(productName, 1);
        store.checkout(); // Assume this method triggers writeReceiptToFile
        // Now check if the file has been written with the correct content.
        // The actual method to test file writing depends on how you implement file writing in StoreFront
        // Without mocking, you would have to read the file directly from the file system.
    }

    
}

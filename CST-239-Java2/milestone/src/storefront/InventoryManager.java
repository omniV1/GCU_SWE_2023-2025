package storefront;

import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import product.SalableProduct;
import utils.FileIOInterface;

import java.io.IOException;
import java.util.List;

import java.util.ArrayList;
import java.util.Arrays;

public class InventoryManager {
    private List<SalableProduct> storeInventory;
    private FileIOInterface fileIO;
    private ObjectMapper mapper;

    // Constructor
    public InventoryManager(FileIOInterface fileIO) {
        this.fileIO = fileIO;
        this.storeInventory = new ArrayList<>();
        this.mapper = new ObjectMapper();
        
        // Configure ObjectMapper to ignore unknown properties
        this.mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
    }
    
    // Method to load inventory from a JSON file
    public void loadInventory(String filename) {
        try {
            // Log the path that will be used to read the file
            System.out.println("Attempting to load inventory from file: " + filename);

            String inventoryData = fileIO.readFromFile(filename);

            // Assuming mapper is an initialized instance of ObjectMapper from the Jackson library
            SalableProduct[] productsArray = mapper.readValue(inventoryData, SalableProduct[].class);

            // Convert the array to a List and store it in the storeInventory
            storeInventory = new ArrayList<>(Arrays.asList(productsArray));
            
            System.out.println("Inventory loaded successfully with " + storeInventory.size() + " items.");
            
        } catch (IOException e) {
            // Log the exception to the console
            System.err.println("Error loading inventory: " + e.getMessage());
            e.printStackTrace();
            // Handle the exception appropriately
            // For example, you might want to set storeInventory to an empty list or possibly rethrow the exception
            storeInventory = new ArrayList<>();
        }
    }



    // Method to save inventory to a JSON file
    public void saveInventoryToFile(String filename) {
        try {
            String inventoryJson = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(storeInventory);
            fileIO.writeToFile(filename, inventoryJson);
            System.out.println("Inventory saved to file: " + filename);
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Error saving inventory to file: " + filename);
        }
    }

    // Remaining methods for managing inventory...

    // Example method to add a product to the inventory
    public void addToInventory(SalableProduct product) {
        storeInventory.add(product);
    }
    /**
     * Retrieves the store's inventory.
     *
     * @return The list of SalableProducts in the store's inventory.
     */
    public List<SalableProduct> getInventory() {
        return storeInventory;
    }

    /**
     * Displays the available products in the store's inventory.
     */
    public void displayProducts() {
        System.out.println("Available Products:");
        for (SalableProduct product : storeInventory) {
            System.out.println(product);
        }
    }
    /**
     * Retrieves all products in the inventory.
     *
     * @return A list of all products in the inventory.
     */
    public List<SalableProduct> getAllProducts() {
        return storeInventory;
    }


    /**
     * Remove a specified quantity of a product from the store inventory.
     *
     * @param product  The product to be removed from the inventory.
     * @param quantity The quantity of the product to remove.
     * @return true if the removal was successful, false if the specified quantity is not available.
     */
    public boolean removeFromInventory(SalableProduct product, int quantity) {
        for (SalableProduct inventoryProduct : storeInventory) {
            if (inventoryProduct.getName().equals(product.getName())) {
                if (inventoryProduct.getQuantity() >= quantity) {
                    inventoryProduct.decrementQuantity(quantity);
                    return true; // Removal successful
                } else {
                    return false; // Insufficient quantity in stock
                }
            }
        }
        return false; // Product not found in the inventory
    }
    /**
     * Retrieves all products in the inventory.
     *
     * @return A list of all products in the inventory.
     */
   
    
    /**
     * Retrieves a product from the inventory by its name.
     *
     * @param name The name of the product to retrieve.
     * @return The product with the given name, or null if no such product exists.
     */
    public SalableProduct getProductByName(String name) {
        for (SalableProduct product : storeInventory) {
            if (product.getName().equals(name)) {
                return product;
            }
        }
        return null;
    }

    /**
     * Returns the specified quantity of the product to the inventory.
     *
     * @param product  The product being returned.
     * @param quantity The quantity of the product to return.
     */
    public void returnProduct(SalableProduct product, int quantity) {
        // Find the product in the inventory
        for (SalableProduct inventoryProduct : storeInventory) {
            if (inventoryProduct.getName().equals(product.getName())) {
                // Increase the quantity in inventory
                inventoryProduct.incrementQuantity(quantity);
                break;
            }
        }
    }
}
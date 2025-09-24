/*
 * Owen Lindsey
 * CST-239
 * This work is my own
 * Milestone 4
 * 10/15/2023
 */


package storefront;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;


import product.SalableProduct;
import utils.FileIO;



/**
 * Represents the main interface of the store application.
 * <p>
 * The StoreFront class offers users various actions, including viewing products, purchasing products,
 * canceling purchases, viewing the shopping cart, and checking out. Users can interact with the StoreFront
 * through a console-based interface.
 * </p>
 */
public class StoreFront {

    private InventoryManager inventoryManager;
    private ShoppingCart shoppingCart;
    private List<SalableProduct> purchasedItems;
    public static final String INVENTORY_JSON_FILE = "E:\\cst-239\\milstone\\src\\inventory.json";

 // Load the inventory from a JSON file at the start of the program
    
  

    /**
     * Initializes the store front with a given inventory of products.
     *
     * @param initialProducts A list of products to be added to the store's inventory upon initialization.
     */
    public StoreFront(InventoryManager inventoryManager) {
        this.inventoryManager = inventoryManager;
        shoppingCart = new ShoppingCart();
        purchasedItems = new ArrayList<>();
        System.out.println("Welcome to Owen's Workshop");
       
        loadInventory();

      
    }
 // Load the inventory from a JSON file at the start of the program
    private void loadInventory() {
        // The loadInventoryFromFile method should handle reading from the file
        // and populating the inventory
        inventoryManager.loadInventory(INVENTORY_JSON_FILE);
    }
    /**
     * Displays the available products in the store's inventory.
     */
    public void displayProducts() {
    	// Sort the inventory by name before displaying
    	 List<SalableProduct> sortedInventory = new ArrayList<>(inventoryManager.getInventory());
         Collections.sort(sortedInventory, Comparator.comparing(SalableProduct::getName));

         System.out.println("---- Available Products ----");
         for (SalableProduct product : sortedInventory) {
             System.out.println(product);
         }
     }
    /**
     * Purchases a product and adds it to the shopping cart.
     *
     * @param name     The name of the product to purchase.
     * @param quantity The quantity of the product to purchase.
     */
    public void purchaseProduct(String productName, int quantity) {
        String productNameToSearch = productName.toLowerCase(); // Convert input to lower case

        // Assume that InventoryManager has a method to get the list of products
        List<SalableProduct> products = inventoryManager.getAllProducts();

        boolean productFound = false;

        for (SalableProduct product : products) {
            if (product.getName().toLowerCase().equals(productNameToSearch)) {
                productFound = true;

                // Check if the requested quantity is available
                if (product.getQuantity() >= quantity) {
                    // Reduce the available quantity by the amount purchased
                    product.setQuantity(product.getQuantity() - quantity);
                    // ... additional code to handle the purchase transaction ...
                    System.out.println("Successfully purchased " + quantity + " " + product.getName() + "(s).");
                } else {
                    System.out.println("Not enough stock available for the product: " + product.getName());
                }
                break;
            }
        }

        if (!productFound) {
            System.out.println("Product not found. Please ensure you have entered the correct product name.");
        }
    }

    /**
     * Cancels a previously made purchase and returns the product to the inventory.
     *
     * @param name The name of the product to cancel the purchase for.
     */
    public void cancelPurchase(String name) {
        SalableProduct product = shoppingCart.removeProductByName(name);
        if (product != null) {
            inventoryManager.addToInventory(product);
            purchasedItems.remove(product);
            System.out.println("Purchase cancelled successfully.");
        } else {
            System.out.println("Product not found in the shopping cart.");
        }
    }

    /**
     * Displays the contents of the shopping cart.
     */
    public void display() {
        shoppingCart.display();
    }

    /**
     * Checks out and calculates the total cost of items in the shopping cart.
     * Clears the purchased items and shopping cart.
     */
    public void checkout() {
        double total = calculateTotal(purchasedItems);
        System.out.println("Total amount: $" + total);
        System.out.println("Thank you for shopping with us!");
        purchasedItems.clear();
        shoppingCart.clear();
    }

    private double calculateTotal(List<SalableProduct> items) {
        double total = 0;
        for (SalableProduct product : items) {
            total += product.getPrice();
        }
        return total;
    }
    /**
     * Writes the list of purchased items to a file as a receipt.
     *
     * @param purchasedItems The list of purchased items to write to the file.
     */
    public void writeReceiptToFile(List<SalableProduct> purchasedItems) {
        try (PrintWriter writer = new PrintWriter(new FileWriter("receipt.txt"))) {
            writer.println("Receipt:");
            for (SalableProduct product : purchasedItems) {
                writer.println(product.getName() + " - $" + product.getPrice());
            }
            writer.println("Total: $" + calculateTotal(purchasedItems));
            System.out.println("Receipt saved to receipt.txt");
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Error saving receipt to file.");
        }
    }

    /**
     * The main entry point for the StoreFront application.
     * <p>
     * This method initializes the storefront with a set of sample products for testing purposes.
     * Then, it provides an interactive user interface, allowing users to display available products,
     * purchase products, cancel purchases, view the current shopping cart, and exit the application.
     * </p>
     * <p>
     * The user is prompted with a list of available actions and can select one by entering the corresponding
     * number. The application will keep running until the user decides to exit.
     * </p>
     * <ul>
     * <li>1 - Display available products</li>
     * <li>2 - Purchase product</li>
     * <li>3 - Cancel purchase of a product</li>
     * <li>4 - View shopping cart</li>
     * <li>5 - Checkout</li>
     * <li>6 - Exit the application</li>
     * </ul>
     *
     * @param args Command-line arguments. Currently not used by this application.
     */
    public static void main(String[] args) {
        // Assuming that FileIO has a parameterless constructor
        FileIO fileIO = new FileIO(); // Create an instance of FileIO
        InventoryManager inventoryManager = new InventoryManager(fileIO); // Pass it to InventoryManager

        // Diagnostic code to check file existence
        Path inventoryFilePath = Paths.get("E:\\cst-239\\milstone\\src\\inventory.json");
        if (Files.exists(inventoryFilePath)) {
            System.out.println("The file exists!");
        } else {
            System.out.println("The file does not exist!");
            // Handle the error appropriately here
            // For example, you could exit the program or ask the user for a different path
            return; // Exit if the file doesn't exist
        }

        // Proceed with loading the inventory if the file exists
        inventoryManager.loadInventory(inventoryFilePath.toString());
        StoreFront store = new StoreFront(inventoryManager); // Create the StoreFront with the inventory manager

        Scanner scanner = new Scanner(System.in);
        boolean exitProgram = false;
        
           while (!exitProgram) {
            try {
                System.out.println("---- Store Front ----");
                System.out.println("1. Display available products");
                System.out.println("2. Purchase product");
                System.out.println("3. Cancel purchase");
                System.out.println("4. View shopping cart");
                System.out.println("5. Checkout");
                System.out.println("6. Exit");
                System.out.print("Choose an option: ");

                int choice = scanner.nextInt();
                scanner.nextLine();  // Consume newline left-over

                switch (choice) {
                    case 1:
                        store.displayProducts(); // Display available products
                        break;
                    case 2:
                        System.out.print("Enter product name to purchase: ");
                        String name = scanner.nextLine();
                        System.out.print("Enter quantity to purchase: ");
                        int quantity = scanner.nextInt();
                        scanner.nextLine();  // Consume newline left-over
                        store.purchaseProduct(name, quantity);
                        break;
                    case 3:
                        System.out.print("Enter product name to cancel purchase: ");
                        name = scanner.nextLine();
                        store.cancelPurchase(name);
                        break;
                    case 4:
                        store.display();
                        break;
                    case 5:
                        store.checkout();
                        break;
                    case 6:
                        System.out.println("Exiting...");
                        store.inventoryManager.saveInventoryToFile(StoreFront.INVENTORY_JSON_FILE);
                        exitProgram = true;
                        break;

                    default:
                        System.out.println("Invalid choice. Please try again.");
                        break;
                }
            } catch (InputMismatchException e) { // Catch InputMismatchException
                // Handle the exception (invalid input) here
                System.out.println("Invalid input. Please enter a valid option.");
                scanner.nextLine(); // Consume invalid input
            }
        }

        // Close the scanner when exiting the program
        scanner.close();
    }
}
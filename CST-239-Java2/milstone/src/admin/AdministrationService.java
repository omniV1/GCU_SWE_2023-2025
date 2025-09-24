package admin;

import com.fasterxml.jackson.databind.ObjectMapper;

import product.SalableProduct;
import storefront.InventoryManager;
import utils.FileIO;
import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.Scanner;
import com.fasterxml.jackson.annotation.JsonInclude;

/**
 * Manages administrative tasks for the store, including updating inventory and handling commands.
 */
public class AdministrationService {
    public InventoryManager inventoryManager;
   /**
     * Constructs an AdministrationService and initializes the InventoryManager.
     */
    public AdministrationService(FileIO fileIO) {
        this.inventoryManager = new InventoryManager(fileIO);
    }
    /**
     * ObjectMapper used for JSON serialization and deserialization.
     */
    private static final ObjectMapper mapper = new ObjectMapper();
    /**
     * The default file path for the inventory JSON file.
     */
    private static final String DEFAULT_INVENTORY_FILE_PATH = "resources/inventory.json"; static {
    	
    	// Set ObjectMapper configuration
        mapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);
    }
 
    
    /**
     * Updates the quantity of a product in the store's inventory.
     *
     * @param productName The name of the product to update.
     * @param change      The change in quantity (positive or negative).
     * @return true if the update was successful, false otherwise.
     */
    public boolean updateProductQuantity(String productName, int change) {
        return incrementProductQuantity(productName, change);
    }
    /**
     * Returns the entire inventory of SalableProducts in JSON format.
     *
     * @return A JSON representation of the store's inventory.
     */
    public List<SalableProduct> returnInventory() {
        return inventoryManager.getInventory();
    }
    /**
     * Increments the quantity of a product in the store's inventory.
     *
     * @param productName The name of the product to increment.
     * @param incrementBy The amount by which to increment the quantity.
     * @return true if the increment was successful, false otherwise.
     */
    public boolean incrementProductQuantity(String productName, int incrementBy) {
        for (SalableProduct product : inventoryManager.getInventory()) {
            if (product.getName().equalsIgnoreCase(productName)) {
                int newQuantity = product.getQuantity() + incrementBy;
                if (newQuantity >= 0) {
                    product.setQuantity(newQuantity);  // This is the crucial missing line
                    System.out.println("Inventory updated correctly. New quantity for " + productName + " is " + newQuantity + ".");
                    return true;
                } else {
                    System.out.println("Update failed. Please ensure the resulting quantity is not negative.");
                    return false;
                }
            }
        }
        System.out.println("Product not found in inventory.");
        return false;
    }
    /**
     * Serializes the entire inventory to a JSON string.
     *
     * @return A JSON string representing the store's inventory.
     * @throws IOException if there is an error during serialization.
     */
    public String serializeInventoryToJson() throws IOException {
        return mapper.writeValueAsString(inventoryManager.getInventory());
    }

    /**
     * Starts the console for interaction with the AdministrationService.
     *
     * @throws IOException if there is an error during console input/output.
     */
    public void startConsole() throws IOException {
        BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in));

        // Initialization and setup tasks
        System.out.println("Starting console...");
        inventoryManager.loadInventory(DEFAULT_INVENTORY_FILE_PATH); // Use the static field

        handleCommands(); // Let this method handle command processing
    }


    /**
     * Handles user commands entered in the console.
     */
    public void handleCommands() {
        Scanner scanner = new Scanner(System.in);
        
        String command;
        do {
            System.out.print("Enter a command (U to update, R to return, I to increment, or Q to quit): ");
            command = scanner.nextLine();
            
            if (command.equalsIgnoreCase("I")) {
                System.out.println("Increment command detected.");

                try {
                    System.out.print("Enter product name to increment: ");
                    String productName = scanner.nextLine();

                    System.out.print("Enter amount to increment by: ");
                    int amount = Integer.parseInt(scanner.nextLine());

                    boolean success = incrementProductQuantity(productName, amount);

                    if (success) {
                        System.out.println("Inventory updated successfully for product: " + productName);

                        // Save the updated inventory to file
                        try {
                            saveInventoryToFile(DEFAULT_INVENTORY_FILE_PATH); // Or use a chosen file path
                            System.out.println("Inventory saved to file.");
                        } catch (IOException e) {
                            System.out.println("Error saving inventory to file: " + e.getMessage());
                        }
                    }

                } catch (NumberFormatException e) {
                    System.out.println("Invalid number format. Please enter a valid number for increment amount.");
                } catch (Exception e) {
                    System.out.println("An error occurred: " + e.getMessage());
                }
            }

       
            
            // Handle the U command (Update from file)
            if (command.equalsIgnoreCase("U")) {
            	
                System.out.println("Add new product to the inventory.");

                // Capture item details
                System.out.print("Enter the type of the product (Weapon, Armor, Health): ");
                String productType;
                do {
                    productType = scanner.nextLine().trim();
                    if (!productType.equalsIgnoreCase("Weapon") && !productType.equalsIgnoreCase("Armor") && !productType.equalsIgnoreCase("Health")) {
                        System.out.print("Invalid type. Please enter either Weapon, Armor, or Health: ");
                    }
                } while (!productType.equalsIgnoreCase("Weapon") && !productType.equalsIgnoreCase("Armor") && !productType.equalsIgnoreCase("Health"));

                System.out.print("Enter the name of the product: ");
                String productName = scanner.nextLine().trim();

                System.out.print("Enter the description of the product: ");
                String productDescription = scanner.nextLine().trim();

                double productPrice = -1;
                do {
                    System.out.print("Enter the price of the product: ");
                    try {
                        productPrice = Double.parseDouble(scanner.nextLine().trim());
                    } catch (NumberFormatException e) {
                        System.out.println("Please enter a valid number for the price.");
                    }
                } while (productPrice < 0);

                int productQuantity = -1;
                do {
                    System.out.print("Enter the quantity of the product: ");
                    try {
                        productQuantity = Integer.parseInt(scanner.nextLine().trim());
                    } catch (NumberFormatException e) {
                        System.out.println("Please enter a valid number for the quantity.");
                    }
                } while (productQuantity < 0);

                // Create a new product instance and add it to the inventory
                SalableProduct newProduct = new SalableProduct(productType, productName, productDescription, productPrice, productQuantity);
                newProduct.setType(productType);  // Set the product type
                inventoryManager.addToInventory(newProduct);
                System.out.println("Product successfully added to the inventory.");

                // Save the updated inventory to file
                try {
                    saveInventoryToFile(DEFAULT_INVENTORY_FILE_PATH);
                    System.out.println("Inventory saved to file.");
                } catch (IOException e) {
                    System.out.println("Error saving inventory to file: " + e.getMessage());
                }
            }




            // Handle the R command (Return inventory)
            if (command.equalsIgnoreCase("R")) {
                List<SalableProduct> products = returnInventory();
                System.out.println("Current Inventory:");
                for (SalableProduct product : products) {
                    System.out.println("Product Name: " + product.getName() + ", Quantity: " + product.getQuantity());
                }
            }

        } while (!command.equalsIgnoreCase("Q"));
        
        System.out.println("Quitting...");
        System.exit(0);
    }
    public void saveInventoryToFile(String filePath) throws IOException {
    	 String json = serializeInventoryToJson();
    	    try (FileWriter writer = new FileWriter(filePath, false)) { // Explicitly overwrite the file
    	        writer.write(json);;
        }
    }


    public String processClientCommand(String command) {
        // For demonstration, just echo back the command
       
        return "Server received command: " + command;
    }



    public static void main(String[] args) {
        FileIO fileIO = new FileIO(); // Instantiate your FileIO implementation
        AdministrationService service = new AdministrationService(fileIO);
        try {
            service.startConsole();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}








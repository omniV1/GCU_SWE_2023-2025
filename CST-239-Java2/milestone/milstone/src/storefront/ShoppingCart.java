package storefront;

import product.SalableProduct;

import java.util.ArrayList;
import java.util.List;

/**
 * Represents a shopping cart that holds salable products.
 */
public class ShoppingCart {

    private List<SalableProduct> products;

    /**
     * Constructs a new empty ShoppingCart.
     */
    public ShoppingCart() {
        this.products = new ArrayList<>();
    }

    /**
     * Retrieves the shopping cart's products.
     * 
     * @return A list of salable products in the shopping cart.
     */
    public List<SalableProduct> getProducts() {
        return new ArrayList<>(products); // Returns a copy of the products list for encapsulation
    }

    /**
     * Adds a product to the shopping cart.
     *
     * @param product  The product to add.
     * @param quantity The quantity of the product to add.
     * @return true if the product was added successfully, false otherwise.
     */
    public boolean addProduct(SalableProduct product, int quantity) {
        if (product == null || quantity <= 0) {
            return false; // Guard clause for invalid input
        }
        for (SalableProduct existingProduct : products) {
            if (existingProduct.getName().equals(product.getName())) {
                existingProduct.incrementQuantity(quantity);
                return true; // Product quantity updated successfully
            }
        }
        // If the product isn't in the cart, add it with the specified quantity
        return products.add(new SalableProduct(
                product.getType(),
                product.getName(),
                product.getDescription(),
                product.getPrice(),
                quantity
        ));
    }

    /**
     * Removes a product from the shopping cart by name.
     *
     * @param productName The name of the product to remove.
     * @return The removed product if found, null otherwise.
     */
    public SalableProduct removeProductByName(String productName) {
        SalableProduct productToRemove = products.stream()
                .filter(p -> p.getName().equals(productName))
                .findFirst()
                .orElse(null);

        if (productToRemove != null) {
            products.remove(productToRemove);
        }
        return productToRemove; // Will be null if the product was not found
    }

    /**
     * Empties the shopping cart.
     */
    public void clear() {
        products.clear();
    }

    /**
     * Displays the products currently in the shopping cart.
     */
    public void display() {
        if (products.isEmpty()) {
            System.out.println("Shopping cart is empty.");
        } else {
            for (SalableProduct product : products) {
                System.out.println(product.getName() + " - " + product.getDescription() +
                        " - $" + product.getPrice() + " x " + product.getQuantity());
            }
        }
    }
}


   

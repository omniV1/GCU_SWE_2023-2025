package product;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonTypeName;

/**
 * Represents a product available in the store.
 * <p>
 * The SalableProduct class is a base class for all salable products in the store.
 * </p>
 */
@JsonTypeName("SalableProduct")
public class SalableProduct {

    private String type;
    private String name;
    private String description;
    private double price;
    private int quantity;

    @JsonCreator
    public SalableProduct(@JsonProperty("type") String type,
                          @JsonProperty("name") String name,
                          @JsonProperty("description") String description,
                          @JsonProperty("price") double price,
                          @JsonProperty("quantity") int quantity) {
        this.type = type;
        this.name = name;
        this.description = description;
        this.price = price;
        this.quantity = quantity;
    }


    @JsonProperty("type")
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    @JsonProperty("name")
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public void incrementQuantity(int amount) {
        if (amount > 0) {
            quantity += amount;
        } else {
            System.out.println("Invalid quantity specified.");
        }
    }

    public void decrementQuantity(int amount) {
        if (amount > 0 && quantity >= amount) {
            quantity -= amount;
        } else {
            System.out.println("Insufficient quantity in stock or invalid quantity specified.");
        }
    }

    public boolean adjustQuantity(int change) {
        int newQuantity = this.quantity + change;
        if (newQuantity >= 0) {
            this.quantity = newQuantity;
            return true;
        } else {
            System.out.println("Invalid adjustment. Resulting quantity would be negative.");
            return false;
        }
    }

    @Override
    public String toString() {
        return name + ": " + description + " - Price: $" + price + " - Available: " + quantity;
    }

    public int compareTo(SalableProduct otherProduct) {
        return this.name.compareTo(otherProduct.name);
    }


}

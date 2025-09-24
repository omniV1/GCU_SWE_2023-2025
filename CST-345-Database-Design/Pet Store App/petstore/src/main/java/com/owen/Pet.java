
package com.owen;

/**
 * This class represents a Pet entity in the pet store application.
 */
public class Pet {
    private String id; 
    private String name; 
    private String description; 
    private double price; 
    private int categoryId;

    /**
     * Default constructor.
     */
    public Pet() {}

    /**
     * Constructs a Pet with specified details.
     *
     * @param id The ID of the pet.
     * @param name The name of the pet.
     * @param description The description of the pet.
     * @param price The price of the pet.
     * @param categoryId The category ID of the pet.
     */
    public Pet(String id, String name, String description, double price, int categoryId) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.price = price;
        this.categoryId = categoryId;
    }

    
    public void setId(String id) {
        this.id = id;
    }
    public void setName(String name) {
        this.name = name;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void setCategoryId(int categoryId) {
        this.categoryId = categoryId;
    }

    public String getId() {
        return id;
    }
    
    public String getName() {
        return name;
    }
    
    public String getDescription() {
        return description;
    }
    
    public double getPrice() {
        return price;
    }
    
    public int getCategoryId() {
        return categoryId;
    }
    
    @Override
    public String toString() {
        return "Pet{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", description='" + description + '\'' +
                ", price=" + price +
                ", categoryId=" + categoryId +
                '}';
    }
    

}

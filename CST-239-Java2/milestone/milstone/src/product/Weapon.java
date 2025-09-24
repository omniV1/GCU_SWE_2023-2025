package product;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonTypeName;

/**
 * Represents a weapon product available in the store.
 * <p>
 * The Weapon class extends the SalableProduct class and represents weapon items that can be purchased from the store.
 * Weapon items have additional properties like damage points.
 * </p>
 */
@JsonTypeName("Weapon")
public class Weapon extends SalableProduct {

    private int damage;

    /**
     * Constructs a Weapon object with the specified properties.
     *
     * @param name        The name of the weapon.
     * @param description A description of the weapon.
     * @param price       The price of the weapon.
     * @param quantity    The initial quantity available in the store.
     * @param damage      The damage points the weapon inflicts.
     */
    @JsonCreator
    public Weapon(@JsonProperty("name") String name,
                  @JsonProperty("description") String description,
                  @JsonProperty("price") double price,
                  @JsonProperty("quantity") int quantity,
                  @JsonProperty("damage") int damage) {
        super("Weapon", name, description, price, quantity);
        this.damage = damage;
    }

    /**
     * Gets the damage points of the weapon.
     *
     * @return The damage points.
     */
    public int getDamage() {
        return damage;
    }

    /**
     * Sets the damage points of the weapon.
     *
     * @param damage The damage points to set.
     */
    public void setDamage(int damage) {
        this.damage = damage;
    }
}

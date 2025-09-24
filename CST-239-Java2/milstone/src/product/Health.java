package product;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonTypeName;

/**
 * Represents a health product available in the store.
 * <p>
 * The Health class extends the SalableProduct class and represents health items that can be purchased from the store.
 * Health items have additional properties like healing points.
 * </p>
 */
@JsonTypeName("Health")
public class Health extends SalableProduct {

    private int healingPoints;

    /**
     * Constructs a Health object with the specified properties.
     *
     * @param name          The name of the health item.
     * @param description   A description of the health item.
     * @param price         The price of the health item.
     * @param quantity      The initial quantity available in the store.
     * @param healingPoints The number of healing points the health item provides.
     */
    @JsonCreator
    public Health(@JsonProperty("name") String name,
                  @JsonProperty("description") String description,
                  @JsonProperty("price") double price,
                  @JsonProperty("quantity") int quantity,
                  @JsonProperty("healingPoints") int healingPoints) {
        super("Health", name, description, price, quantity);
        this.healingPoints = healingPoints;
    }

    /**
     * Gets the healing points of the health item.
     *
     * @return The healing points.
     */
    public int getHealingPoints() {
        return healingPoints;
    }

    /**
     * Sets the healing points of the health item.
     *
     * @param healingPoints The healing points to set.
     */
    public void setHealingPoints(int healingPoints) {
        this.healingPoints = healingPoints;
    }
}

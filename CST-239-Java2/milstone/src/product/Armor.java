package product;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonTypeName;

/**
 * Represents an armor product available in the store.
 * <p>
 * The Armor class extends the SalableProduct class and represents armor items that can be purchased from the store.
 * Armor has additional properties like defense points.
 * </p>
 */
@JsonTypeName("Armor")
public class Armor extends SalableProduct {

    private int defensePoints;

    /**
     * Constructs an Armor object with the specified properties.
     *
     * @param name          The name of the armor.
     * @param description   A description of the armor.
     * @param price         The price of the armor.
     * @param quantity      The initial quantity available in the store.
     * @param defensePoints The number of defense points the armor provides.
     */
    @JsonCreator
    public Armor(@JsonProperty("name") String name,
                 @JsonProperty("description") String description,
                 @JsonProperty("price") double price,
                 @JsonProperty("quantity") int quantity,
                 @JsonProperty("defensePoints") int defensePoints) {
        super("Armor", name, description, price, quantity);
        this.defensePoints = defensePoints;
    }
    /**
     * Gets the defense points of the armor.
     *
     * @return The defense points.
     */
    public int getDefensePoints() {
        return defensePoints;
    }

    /**
     * Sets the defense points of the armor.
     *
     * @param defensePoints The defense points to set.
     */
    public void setDefensePoints(int defensePoints) {
        this.defensePoints = defensePoints;
    }
}

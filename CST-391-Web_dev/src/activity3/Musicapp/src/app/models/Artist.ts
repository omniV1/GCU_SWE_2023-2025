// Exporting the Artist class so it can be imported and used in other parts of the application.
export class Artist {
    // Private properties to store the artist's ID and name. The encapsulation principle is applied here to restrict direct access to these properties.
    private id: number = -1; // Initializes the artist's ID with a default value of -1.
    private name: string = ""; // Initializes the artist's name with a default, empty string.

    // The constructor for the Artist class. It's called when creating a new instance of Artist, allowing the ID and name to be specified.
    constructor(id: number, name: string) {
        this.id = id; // Sets the artist's ID.
        this.name = name; // Sets the artist's name.
    }

    // A getter for the artist's ID. This provides read-only access to the private id property.
    get Id(): number {
        return this.id;
    }
    // A setter for the artist's ID. This allows the id property to be updated in a controlled manner.
    set Id(id: number) {
        this.id = id;
    }

    // A getter for the artist's name. This provides read-only access to the private name property.
    get Name(): string {
        return this.name;
    }
    // A setter for the artist's name. This allows the name property to be updated while maintaining encapsulation.
    set Name(name: string) {
        this.name = name;
    }
}

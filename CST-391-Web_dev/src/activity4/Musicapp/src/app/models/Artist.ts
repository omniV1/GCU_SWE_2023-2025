// Artist class representing the structure of an artist
export class Artist {
    private id: number = -1; // ID of the artist, default -1
    private name: string = ""; // Name of the artist, default empty string
    
    constructor(id: number, name: string) {
        this.id = id;
        this.name = name;
    }

    // Getter and setter for the ID property
    get Id(): number {
        return this.id;
    }
    set Id(id: number) {
        this.id = id;
    }

    // Getter and setter for the Name property
    get Name(): string {
        return this.name;
    }
    set Name(name: string) {
        this.name = name;
    }
}

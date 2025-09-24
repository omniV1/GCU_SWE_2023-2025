package com.owen;

import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Filters;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;

import org.bson.Document;
import org.bson.types.ObjectId;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * DAO class for handling database operations related to Pets.
 */
public class PetStoreDataAccessObject {
    private MongoDatabase database;
    private MongoCollection<Document> collection;

    /**
     * Constructor to initialize MongoDB connection.
     */
    public PetStoreDataAccessObject() {
        
        String connectionString = "mongodb+srv://myAtlasDBUser:1@myatlasclustered.byiowq8.mongodb.net/?retryWrites=true&w=majority";
        MongoClient mongoClient = MongoClients.create(connectionString);
        this.database = mongoClient.getDatabase("Pets");
        this.collection = database.getCollection("petscollection");
    }

    /**
     * Adds a new pet to the database.
     * 
     * @param pet The Pet object to add.
     * @return true if the operation was successful.
     */
    public boolean addNewPet(Pet pet) {
        Document petDocument = new Document()
            .append("name", pet.getName())
            .append("description", pet.getDescription())
            .append("price", pet.getPrice())
            .append("categoryId", pet.getCategoryId());
        collection.insertOne(petDocument);
        return true;
    }

    /**
     * Retrieves a pet by its ID.
     * 
     * @param id The ID of the pet to retrieve.
     * @return The found Pet object, or null if not found.
     */
    public Pet getPetById(String id) {
        Document query = new Document("_id", new ObjectId(id));
        Document petDocument = collection.find(query).first();
        if (petDocument != null) {
            return documentToPet(petDocument);
        }
        return null;
    }


    /**
     * Updates a pet in the database.
     * 
     * @param pet The Pet object to update.
     * @return true if the operation was successful.
     */
    public boolean updatePet(Pet pet) {
        try {
            ObjectId id = new ObjectId(pet.getId()); // Converts the string ID to ObjectId
            Document update = new Document()
                    .append("name", pet.getName())
                    .append("description", pet.getDescription())
                    .append("price", pet.getPrice())
                    .append("categoryId", pet.getCategoryId());
            
            // Update the document in the collection corresponding to the ObjectId
            collection.updateOne(Filters.eq("_id", id), new Document("$set", update));
            
            // If the code reaches this point without an exception, the update was successful
            return true;
        } catch (Exception e) {
            // If there's an exception, print its message and return false
            System.err.println("An error occurred while updating the pet: " + e.getMessage());
            return false;
        }
    }
    
    /**
     * Deletes a pet from the database by name.
     * 
     * @param name The name of the pet to delete.
     * @return true if the operation was successful.
     */
    public boolean deletePetByName(String name) {
        Document query = new Document("name", name);
        return collection.deleteOne(query).getDeletedCount() > 0;
    }

    /**
     * Searches for pets by a keyword in their name or description.
     * 
     * @param keyword The keyword to search for.
     * @return A list of Pet objects matching the keyword.
     */
    public List<Pet> searchPetsByKeyword(String keyword) {
        List<Pet> pets = new ArrayList<>();
        Document query = new Document("$or", Arrays.asList(
            new Document("name", new Document("$regex", keyword).append("$options", "i")),
            new Document("description", new Document("$regex", keyword).append("$options", "i"))
        ));
        collection.find(query).forEach(doc -> pets.add(documentToPet(doc)));
        return pets;
    }
    
   
    
    

    /**
     * Retrieves all pets from the database.
     * 
     * @return A list of all Pet objects.
     */
    public List<Pet> getAllPets() {
        List<Pet> pets = new ArrayList<>();
        collection.find().forEach(doc -> pets.add(documentToPet(doc)));
        return pets;
    }

    /**
     * Converts a Document object to a Pet object.
     * 
     * @param doc The Document object to convert.
     * @return A Pet object.
     */
    private Pet documentToPet(Document doc) {
        Pet pet = new Pet();
        pet.setId(doc.getObjectId("_id").toString());
        pet.setName(doc.getString("name"));
        pet.setDescription(doc.getString("description"));
        
        // Retrieve the price as a Number and convert to double
        Number price = doc.get("price", Number.class);
        pet.setPrice(price.doubleValue());
        
        pet.setCategoryId(doc.getInteger("categoryId"));
        return pet;
    }
}

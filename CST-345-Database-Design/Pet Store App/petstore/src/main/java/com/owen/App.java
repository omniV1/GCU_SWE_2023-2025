package com.owen;

import java.util.List;
import java.util.Scanner;

public class App {
    private static final Scanner scanner = new Scanner(System.in);
    private static final PetStoreDataAccessObject dao = new PetStoreDataAccessObject();

    public static void main(String[] args) {
        System.out.println("Welcome to Pet World!");

        int option;
        do {
            displayMenu();
            option = scanner.nextInt();
            scanner.nextLine(); // consume the leftover newline

            switch (option) {
                case 1:
                    showAllPets();
                    break;
                case 2:
                    addNewPet();
                    break;
                case 3:
                    updatePet();
                    break;
                case 4:
                    deletePetByName();
                    break;
                case 5:
                    searchPetsByKeyword();
                    break;
                case 0:
                    System.out.println("Exiting Pet World. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid option! Please try again.");
            }
        } while (option != 0);
    }

    private static void displayMenu() {
        System.out.println("\nMenu:");
        System.out.println("1. List all pets");
        System.out.println("2. Add a new pet");
        System.out.println("3. Update a pet");
        System.out.println("4. Delete a pet");
        System.out.println("5. Search for a pet by keyword");
        System.out.println("0. Exit");
        System.out.print("Enter your choice: ");
    }

    private static void showAllPets() {
        List<Pet> pets = dao.getAllPets();
        if (pets.isEmpty()) {
            System.out.println("No pets found.");
        } else {
            for (Pet pet : pets) {
                System.out.println(pet);
            }
        }
    }

    private static void addNewPet() {
        System.out.println("Enter pet details to add:");
        System.out.print("Name: ");
        String name = scanner.nextLine();

        System.out.print("Description: ");
        String description = scanner.nextLine();

        System.out.print("Price: ");
        double price = scanner.nextDouble();

        System.out.print("Category ID: ");
        int categoryId = scanner.nextInt();
        scanner.nextLine(); // consume the leftover newline

        Pet pet = new Pet();
        pet.setName(name);
        pet.setDescription(description);
        pet.setPrice(price);
        pet.setCategoryId(categoryId);

        boolean isAdded = dao.addNewPet(pet);
        if (isAdded) {
            System.out.println("New pet added successfully!");
        } else {
            System.out.println("Failed to add the new pet.");
        }
    }
    

    private static void deletePetByName() {
        System.out.print("Enter the name of the pet you want to delete: ");
        String name = scanner.nextLine();
        boolean isDeleted = dao.deletePetByName(name);
        if (isDeleted) {
            System.out.println("Pet deleted successfully.");
        } else {
            System.out.println("Pet could not be deleted.");
        }
    }
    

   // Part of App class
private static void searchPetsByKeyword() {
    System.out.print("Enter keyword to search for pets: ");
    String keyword = scanner.nextLine();

    // Use the DAO to search for pets with the given keyword
    List<Pet> pets = dao.searchPetsByKeyword(keyword);

    // Check if the list is empty and print an appropriate message
    if (pets.isEmpty()) {
        System.out.println("No pets found with the keyword '" + keyword + "'.");
    } else {
        // Otherwise, print out each pet found
        for (Pet pet : pets) {
            System.out.println(pet);
        }
    }
}


    private static void updatePet() {
        System.out.println("Update Pet Details");
        System.out.print("Enter the ID of the pet you want to update: ");
        String id = scanner.nextLine();
    
        Pet petToUpdate = dao.getPetById(id);
        if (petToUpdate == null) {
            System.out.println("Pet not found!");
            return;
        }
    
        updatePetDetails(petToUpdate, scanner);

        boolean isUpdated = dao.updatePet(petToUpdate);
        if (isUpdated) {
            System.out.println("Pet updated successfully!");
        } else {
            System.out.println("Failed to update the pet.");
        }
    }

    private static void updatePetDetails(Pet petToUpdate, Scanner scanner) {
        System.out.println("Current details of the pet: " + petToUpdate);
        System.out.println("Enter new details for the pet (press ENTER to skip updating a field):");

        System.out.print("New Name (current - " + petToUpdate.getName() + "): ");
        String newName = scanner.nextLine();
        if (!newName.trim().isEmpty()) {
            petToUpdate.setName(newName);
        }

        System.out.print("New Description (current - " + petToUpdate.getDescription() + "): ");
        String newDescription = scanner.nextLine();
        if (!newDescription.trim().isEmpty()) {
            petToUpdate.setDescription(newDescription);
        }

        System.out.print("New Price (current - " + petToUpdate.getPrice() + "): ");
        String newPriceStr = scanner.nextLine();
        if (!newPriceStr.trim().isEmpty()) {
            try {
                double newPrice = Double.parseDouble(newPriceStr);
                petToUpdate.setPrice(newPrice);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input for price. Keeping the current value.");
            }
        }

        System.out.print("New Category ID (current - " + petToUpdate.getCategoryId() + "): ");
        String newCategoryIdStr = scanner.nextLine();
        if (!newCategoryIdStr.trim().isEmpty()) {
            try {
                int newCategoryId = Integer.parseInt(newCategoryIdStr);
                petToUpdate.setCategoryId(newCategoryId);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input for category ID. Keeping the current value.");
            }
        }
    }
}

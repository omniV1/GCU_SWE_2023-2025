// Importing Component for defining a new component, OnInit for the component initialization hook, and Input for receiving data from a parent component.
import { Component, OnInit, Input } from '@angular/core';

// The @Component decorator defines metadata for the component:
@Component({
  selector: 'app-info', // Defines the custom HTML tag for this component.
  templateUrl: './info.component.html', // Specifies the path to the template file for the component.
  styleUrl: './info.component.css' // Specifies the path to the CSS file for the component. Should be corrected to 'styleUrls' in an array format.
})
export class InfoComponent implements OnInit { // Implements OnInit to hook into the component initialization lifecycle.
  @Input() name!: string; // The @Input decorator allows 'name' to be passed to this component from a parent component.
  quantity = 0; // Initializes 'quantity' with a default value of 0.
  products: string[] = []; // Initializes 'products' as an empty array to be populated with strings.
  selectedProduct = "Star Wars"; // Sets the default selected product.

  constructor() {} // The constructor for the class, used for dependency injection and initial setup.

  ngOnInit() {
    // Lifecycle hook that is called after Angular has initialized all data-bound properties.
    this.quantity = 0; // Resets quantity to 0.
    this.products = [ "Star Wars", "The Empire Strikes Back", "Return of the Jedi"]; // Populates the products array.
    this.selectedProduct = "Star Wars"; // Resets the selected product to "Star Wars".
  }

  newInfo() {
    // Custom method to reset the component's state and log a message.
    this.quantity = 0; // Resets quantity to 0.
    this.products = [ "Star Wars", "The Empire Strikes Back", "Return of the Jedi"]; // Re-populates the products array.
    this.selectedProduct = "Star Wars"; // Resets the selected product.
    console.log("IN newInfo() and resetting Info"); // Logs a message indicating that the info is being reset.
  }
  
  onSubmit() {
    // Custom method to handle form submission, logging the current quantity and selected product.
    console.log("In onSubmit() with quantity of " + this.quantity + " and movie selected is " + this.selectedProduct); 
  }
}

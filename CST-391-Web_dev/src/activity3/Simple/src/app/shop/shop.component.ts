// Importing Component decorator and form classes from Angular core.
import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

// The @Component decorator marks the class as an Angular component and provides metadata including the selector, the path to the HTML template, and the path to the CSS styles.
@Component({
  selector: 'app-shop', // The CSS selector name that represents this component.
  templateUrl: './shop.component.html', // The path to the template file for the component.
  styleUrls: ['./shop.component.css'] // The path to the CSS file for styling the component.
})
export class ShopComponent {
  // Properties of the ShopComponent class.
  question = "What’s your name?"; // A string property to store a question.
  answer = "unknown"; // A string property to store the user's answer, initialized as 'unknown'.
  
  // Initializing a FormGroup to handle form data. The form has a single control named 'answer'.
  appForm = new FormGroup({
    answer: new FormControl('') // Creates a new form control for inputting an answer, initialized with an empty string.
  });

  // Method to handle form submission.
  onSubmit(data: Partial<{ answer: string | null }>) { // Accepts partial form data with 'answer' which may be a string or null.
    this.answer = data.answer!; // Updates the 'answer' property with the submitted form data. The '!' is a TypeScript non-null assertion operator, asserting that `data.answer` is not null.
    console.log('Your name is:', this.answer); // Logs the submitted answer to the console.
  }
}

// Importing Component decorator from Angular core to define a new component.
import { Component } from '@angular/core';
// Router is imported to programmatically navigate within the application.
import { Router } from '@angular/router';

// The @Component decorator is used to provide Angular with information about this component.
@Component({
  selector: 'app-root', // The custom HTML tag that will be used to invoke this component.
  templateUrl: './app.component.html', // The path to the HTML template for this component.
  styleUrls: ['./app.component.css'] // The path to the CSS styles for this component. Note: It should be 'styleUrls' in plural.
})
export class AppComponent {
  // Property 'title' of type String to store the title of the application.
  title: String = "My Music Collection";
  // Property 'version' of type String to store the current version of the application.
  version: String = "1.0";

  // Constructor for this component with Router service injected.
  // The Router is used for navigating between pages programmatically.
  constructor(private router: Router){}

  // Method 'displayVersion' to show the application version in an alert dialog.
  displayVersion(){
    alert(this.version);
  };

  // Method 'displayArtistList' to navigate to the 'list-artists' route.
  // It logs to the console and navigates, appending a query parameter with the current date.
  displayArtistList(){
    console.log("displayArtistList");
    // 'navigate' method of the Router is used to change the route.
    // 'list-artists' is the target route, and queryParams are passed with it.
    this.router.navigate(['list-artists'], { queryParams: { data: new Date()} });
  };
}

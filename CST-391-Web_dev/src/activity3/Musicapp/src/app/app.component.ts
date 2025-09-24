import { Component } from '@angular/core';
import { Router } from '@angular/router';

// The @Component decorator provides metadata for the component, including its selector, 
// the URL of its accompanying HTML and CSS files.
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

// AppComponent is the root component of the application, 
// which acts as the primary layout for the app.
export class AppComponent
{
   // Title of the application, used for display in the NavBar and browser title.
  title = 'My Music Collection';

  // Current version of the application, displayed in the NavBar through displayVersion().
  version = "1.0";

  // The constructor injects the Router service for navigation.
  // Router allows for programmatically navigating to different components.
  constructor(private router: Router)
  {

  }
  // displayVersion() is an event handler for displaying the app version in an alert box.
  // It's triggered by user interaction with the NavBar.
  public displayVersion()
  {
    alert(this.title + " Version: " + this.version);
  }
  // displayArtistList() is an event handler for navigating to the list-artists route.
  // It passes a timestamp in query params, forcing component reinitialization.
  
  public displayArtistList()
  {
    this.router.navigate(['list-artists'], { queryParams: { data: new Date()} });
  }
}

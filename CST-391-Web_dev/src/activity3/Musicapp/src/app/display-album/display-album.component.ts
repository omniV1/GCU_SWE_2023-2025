// Angular core imports for defining components and handling initialization.
import { Component, OnInit, Input } from '@angular/core';
// Importing the Album model to type-check the input data.
import { Album } from '../models/Album';

// The @Component decorator is used to define class metadata.
@Component({
    selector: 'app-display-album', // The custom HTML element name for this component.
    templateUrl: './display-album.component.html', // Path to the HTML template for the component.
    styleUrls: ['./display-album.component.css'], // Path to the styles specific to this component.
})
export class DisplayAlbumComponent implements OnInit {
    // The @Input decorator declares that this component can receive an Album object from its parent component.
    // This allows for data to be passed to this component for display.
    @Input() album: Album | null = null;

    // Constructor method for the component. Typically used for dependency injection.
    // This component does not inject dependencies, so the constructor is empty.
    constructor() { }

    // The ngOnInit method is a lifecycle hook called by Angular to indicate that Angular is done creating the component.
    // In this component, there's no initialization logic required, so the method is empty.
    ngOnInit() { }
}


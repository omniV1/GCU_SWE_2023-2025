import { Request, Response, Router } from 'express';
import * as ArtistsController from './artists.controllers'; // Importing the controller functions for handling artist-related requests

const router = Router(); // Creating an Express router instance

router
    .route('/artists') // Defines a route for handling GET requests to /artists
    .get(ArtistsController.readArtists); // Calls the readArtists function from the ArtistsController when a GET request is made to /artists

export default router; // Exports the router instance for use in other parts of the application

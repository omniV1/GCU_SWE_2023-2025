// Importing the express module and specific types from 'express'
import express, { Request, Response } from 'express';

// Creating an instance of express
const app = express();

// Defining the port number on which the server will listen
const port = 9991;

// Handling GET requests to the root ('/') URL
// req represents the request object, res represents the response object
app.get('/', (req: Request, res: Response) => {
    // Sending a text response 'Hello World from TypeScript!' to the client
    res.send('Hello World from TypeScript!');
});

// Starting the server on the specified port
// The listen method takes the port number and an optional callback function

app.listen(port, () => {
    // This callback function is executed once the server starts listening
    // Logging the URL where the server is listening
    console.log(`Example app listening at http://localhost:${port}`);
});

import { Request, Response, NextFunction } from "express";
import { v4 as uuidv4 } from 'uuid'; // Importing the v4 function from the uuid library to generate unique IDs

// Function to calculate processing time in milliseconds from a tuple representing the time
const getProcessingTimeInMS = (time: [number, number]): string => {
    return `${(time[0] * 1000 + time[1] / 1e6).toFixed(2)}ms`; // Convert hrtime to milliseconds and format the result
}

// Middleware function to log HTTP request and response details
export default function logger(req: Request, res: Response, next: NextFunction) {
    const id = uuidv4(); // Generate a unique ID using uuidv4()

    const now = new Date(); // Get the current date and time
    const timestamp = [now.getFullYear(), '-', now.getMonth() + 1, '-', now.getDate(), ' ', now.getHours(), ':', now.getMinutes(), ':', now.getSeconds()]
        .join(' '); // Format the timestamp

    const { method, url } = req; // Extract HTTP method and URL from the request object

    const start = process.hrtime(); // Record the start time of processing using process.hrtime()
    const startText = `START:${getProcessingTimeInMS(start)}`; // Get start time in milliseconds
    const idText = `[${id}]`; // Enclose ID in square brackets for logging
    const timestampText = `[${timestamp}]`; // Enclose timestamp in square brackets for logging

    // Log a message indicating the start of processing, including request ID, timestamp, HTTP method, URL, and start time
    console.log(`${idText}${timestampText} ${method}:${url} ${startText}`);

    // Attach an event listener to the response object's 'finish' event, which fires when the response has been sent to the client
    res.once('finish', () => {
        const end = process.hrtime(start); // Calculate the end time of processing
        const endText = `END:${getProcessingTimeInMS(end)}`; // Get end time in milliseconds
        // Log a message indicating the end of processing, including request ID, timestamp, HTTP method, URL, response status code, and processing time
        console.log(`${idText}${timestampText} ${method}:${url} ${res.statusCode} ${endText}`);
    });

    next(); // Call the next middleware function
}

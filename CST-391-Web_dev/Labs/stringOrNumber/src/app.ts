// Import the promptSync function from the 'prompt-sync' library
import promptSync from 'prompt-sync';

// Create an instance of the prompt function
const prompt = promptSync();

// Define the main function to detect input types
function detectInput(): void 
{
    // Start an infinite loop to continuously prompt for input
    while (true) 
        {
        // Prompt the user for input and store it in the 'input' variable
        const input = prompt('Enter something (or "quit" to exit): ');
        
        // Check if the user wants to quit the program
        if (input.toLowerCase() === 'quit') 
        {
            // Print an exit message
            console.log('Exiting program.');
            // Break out of the infinite loop to end the program
            break;
        }
        
        // Check if the input can be converted to a number
        if (!isNaN(Number(input))) 
        {
            // If it's a number, log that a number was entered
            console.log('a number entered');
        } else {
            // If it's not a number, log that a string was entered
            console.log('a string entered');
        }
    }
}

// Call the detectInput function to start the program
detectInput();
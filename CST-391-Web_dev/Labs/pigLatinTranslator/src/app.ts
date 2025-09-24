import promptSync from 'prompt-sync';

class PigLatin 
{
    private static prompt = promptSync();

    public static main(): void 
    {
        while (true) 
            {
            console.log("Enter one or more words to translate to Pig Latin (or 'quit' to exit): ");
            const userInput: string = this.prompt({});

            if (userInput.toLowerCase() === 'quit') 
                {
                console.log("Exiting program.");
                break;
            }

            // Splits the string into an array of words
            const words: string[] = userInput.split(" ");
            let output: string = "";

            for (let i = 0; i < words.length; i++) 
                {

                // Translates each word individually
                const pigLatinWord: string = this.translateWord(words[i]);

                // Joins the translated word back into the output
                output += pigLatinWord + " ";
            }

            console.log("Original Word(s): " + userInput);
            console.log("Translation: " + output.trim());

             // Add a blank line for readability
            console.log();
        }
    }

    public static translateWord(word: string): string 
    {
        // Separate punctuation from the word
        const punctuation = word.match(/[.,!?;:]$/);
        const cleanWord = word.replace(/[.,!?;:]$/, '');

        const lowerCaseWord: string = cleanWord.toLowerCase();
        // Position of first vowel
        let pos: number = -1;
        let ch: string;

        // This for loop finds the index of the first vowel in the word
        for (let i = 0; i < lowerCaseWord.length; i++)
            {
            ch = lowerCaseWord.charAt(i);

            if (this.isVowel(ch)) {
                pos = i;
                break;
            }
        }

        let result: string;
        if (pos === 0) 
            {
            // Translating word if the first character is a vowel
            // Adding "yay" to the end of string (can also be "way" or just "ay")
            result = lowerCaseWord + "yay";
        } 
        else 
        {
            // Translating word if the first character(s) are consonants 
            // Extracting all characters in the word beginning from the 1st vowel
            const a: string = lowerCaseWord.substring(pos);
            // Extracting all characters located before the first vowel
            const b: string = lowerCaseWord.substring(0, pos);
            // Adding "ay" at the end of the extracted words after joining them
            result = a + b + "ay";
        }

        // Preserve original capitalization
        if (word[0] === word[0].toUpperCase()) 
        {
            result = result.charAt(0).toUpperCase() + result.slice(1);
        }

        // Reattach punctuation if it existed
        return punctuation ? result + punctuation[0] : result;
    }

    // This method checks if the character passed is a vowel (the letter "y" is counted as a vowel in this context)
    public static isVowel(ch: string): boolean 
    {
        return ['a', 'e', 'i', 'o', 'u', 'y'].includes(ch);
    }
}

// Run the program
PigLatin.main();
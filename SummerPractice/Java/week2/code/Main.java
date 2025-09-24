package week2.code;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        // Variables and data types 
        int number = 10; 
        double decimalNumber = 26.5;
        char letter = 'A';
        String message = "HI I AM OWEN";
        boolean isTrue = true; 
        float floatNumber = 5.5f; 

        // new variables and data types
        long longNumber = 10000000L; 
        byte byteNumber = 2; 
        short shortNumber = 100;

        // Output to the console
        System.out.println("Integer: " + number); 
        System.out.println("Double: " + decimalNumber); 
        System.out.println("Character: " + letter); 
        System.out.println("String: " + message); 
        System.out.println("Boolean: " + isTrue); 
        System.out.println("Long Number: " + longNumber); 
        System.out.println("Byte number: " + byteNumber); 
        System.out.println("Short number: " + shortNumber); 
        System.out.println("Float number: " + floatNumber); 

        // Control structure
        if (number > 5) {
            System.out.println("Number is greater than 5"); 
        } else {
            System.out.println("Number is 5 or less");
        }

        for (int i = 0; i < 5; i++) {
           System.out.println("For Loop: " + i); 
        }

        int count = 0; 
        while (count < 5) {
            System.out.println("While Loop: " + count); 
            count++; 
        }

        // switch case example
        switch (number) { 
            case 10: 
                System.out.println("Number is 10"); 
                break; 
            case 5: 
                System.out.println("Number is 5");
                break; 
            default: 
                System.out.println("Number is not 10 or 5"); 
        }

        // Methods 
        printMessage("This is a custom method"); 

        // OOP Concepts
        Person person = new Person(); 
        person.setName("Owen Lindsey"); 
        person.setAge(26); 
        person.introduce(); 

        // Array example
        int[] numbers = {1,2,3,4,5}; 
        for (int num : numbers) {
            System.out.println("Array element: " + num); 
        }

        // ArrayList example
        ArrayList<String> fruits = new ArrayList<>(); 
        fruits.add("apple"); 
        fruits.add("Banana"); 
        fruits.add("Cherry"); 
        for (String fruit : fruits) {
            System.out.println("ArrayList element: " + fruit);
        }

        // recursive method example
        System.out.println("Factorial of 5: " + factorial(5));

        // try-catch example
        try { 
            int result = divide(10, 0); 
            System.out.println("Result: " + result); 
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    // Custom method to print a message
    public static void printMessage(String msg) {
        System.out.println(msg); 
    }

    // Overloaded methods 
    public static void printMessage(String msg, int times) {
        for (int i = 0; i < times; i++) {
            System.out.println(msg); 
        }
    }

    // Recursive method
    public static int factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    // Method to divide two numbers
    public static int divide(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("Division by zero is not allowed");
        }
        return a / b; 
    }
}

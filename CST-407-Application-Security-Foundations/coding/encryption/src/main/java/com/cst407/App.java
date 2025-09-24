package com.cst407;
/**Owen Lindsey 
 * CST-407
 * 09/09/2025
 * This program implements the RSA encryption algorithm.
 * It allows the user to encrypt and decrypt messages using the RSA algorithm.
 * It also allows the user to choose the bit length and exponent for the RSA algorithm.
 * It also allows the user to choose the message to encrypt and decrypt.
 */

import java.math.BigInteger;
import java.security.SecureRandom;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class App {
    // List of ANSI color codes
    private static final List<String> colors = Arrays.asList(
            "\u001B[30m", // Black
            "\u001B[31m", // Red
            "\u001B[32m", // Green
            "\u001B[33m", // Yellow
            "\u001B[34m", // Blue
            "\u001B[35m", // Magenta
            "\u001B[36m", // Cyan
            "\u001B[37m" // White
    );

    public static void main(String[] args) {
        SecureRandom random = new SecureRandom();

        // user input
        Scanner scanner = new Scanner(System.in);
        while (true) {
            // black
            System.out.println(colors.get(0) + "Welcome to the Encryption Program!");
            System.out.println(colors.get(0) + "Please enter a message to encrypt:");
            String message = scanner.nextLine();

            int bitLength = getBitLength(scanner);

            BigInteger exponent = getExponent(scanner);

            Date startTime = new Date();

            BigInteger e = exponent;

            // Generate two 1024-bit primes
            BigInteger p = generatePrime(random, bitLength);
            BigInteger q = generatePrime(random, bitLength);

            // calculate modulus n = p * q
            BigInteger n = p.multiply(q);

            // Calculate phi = (p - 1) * (q - 1)
            BigInteger phi = calculatePhi(p, q);

            // Ensure that e is coprime with phi
            if (!isCoprime(e, phi)) {
                printColored("Error: e is not coprime with phi. Chose a different exponent.", colors.get(1));
                continue;
            }

            // Calculate d = e^-1 mod phi
            BigInteger d = e.modInverse(phi);

            // Print values with colors
            printColored("p: " + p, colors.get(1));
            printColored("q: " + q, colors.get(2));
            printColored("n: " + n, colors.get(3));
            printColored("phi: " + phi, colors.get(4));
            printColored("e: is the public exponent " + e, colors.get(5));
            printColored("d: is the private key " + d, colors.get(6));
            printColored("startTime: " + startTime, colors.get(0));

            // Encrypt message
            printColored("Message:" + message, colors.get(0));
            BigInteger encryptedMessage = encryptMessage(message, e, n);
            printColored("Encrypted message as integer: " + encryptedMessage, colors.get(1));

            // Decrypt message
            BigInteger decryptedMessageInt = decryptMessage(encryptedMessage, d, n);
            printDecryptedMessage(new String(decryptedMessageInt.toByteArray()));

            Date endTime = new Date();
            long timeElapsed = endTime.getTime() - startTime.getTime();
            printColored("Time elapsed:" + timeElapsed + "ms", colors.get(7));

            // Ask if the user wants to encrypt another message
            System.out.println(colors.get(0) + "Do you want to encrypt another message? (y/n)");
            String answer = scanner.nextLine();
            if (answer.equalsIgnoreCase("n")) {
                break;
            }
        }
        scanner.close();
        System.out.println(colors.get(0) + "Thank you for using the Encryption Program!");
    }

    private static boolean isCoprime(BigInteger e, BigInteger phi) {
        return e.gcd(phi).equals(BigInteger.ONE);
    }
    private static BigInteger generatePrime(SecureRandom random, int bitLength) {
        return BigInteger.probablePrime(bitLength, random);
    }
    private static BigInteger calculatePhi(BigInteger p, BigInteger q) {
        return (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));
    }
    private static BigInteger encryptMessage(String message, BigInteger e, BigInteger n) {
        BigInteger messageInt = new BigInteger(message.getBytes());
        return messageInt.modPow(e, n);
    }
    private static BigInteger decryptMessage(BigInteger encryptedMessage, BigInteger d, BigInteger n) {
        return encryptedMessage.modPow(d, n);
    }
    private static void printColored(String message, String color) {
        System.out.println(color + message + "\u001B[0m");
    }
    private static void printDecryptedMessage(String decryptedMessage) {
        printColored("Decrypted message: " + decryptedMessage, colors.get(2));
    }
    private static int getBitLength(Scanner scanner) {
        System.out.println(colors.get(0) + "Please enter the bit length for the primes:");
        int bitLength = scanner.nextInt();
        scanner.nextLine(); // consume the rest of the line
        return bitLength;
    }
    private static BigInteger getExponent(Scanner scanner) {
        System.out.println(colors.get(0) + "Please enter the exponent:");
        return new BigInteger(scanner.nextLine());
    }
}

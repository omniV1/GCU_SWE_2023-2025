package gcu.hashing;

/**
 * Password Hashing Algorithm Comparison Application
 * 
 * Purpose: Demonstrates and compares the performance of various cryptographic
 * hashing algorithms commonly used for password security in compliant systems.
 * 
 * Author: CST-407 Class Project
 * Date: September 2025
 */

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Scanner;
import org.mindrot.jbcrypt.BCrypt;

public class App {
    
    // Class constants for algorithm names and formatting
    private static final String ANSI_RESET = "\u001B[0m";
    private static final String ANSI_RED = "\u001B[31m";
    private static final String ANSI_BLUE = "\u001B[34m";
    private static final String ANSI_GREEN = "\u001B[32m";
    private static final String ANSI_YELLOW = "\u001B[33m";
    
    /**
     * Main application entry point
     * 
     * SEQUENCE:
     *   1. Initialize scanner for user input
     *   2. Prompt user for password input
     *   3. FOR each hashing algorithm DO
     *        Execute timing test and display results
     *   4. Close scanner and terminate program
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Display application header with purpose and compliance note
        printHeader();
        
        // Obtain password input from user for hashing comparison
        System.out.print("Please enter a password to hash: ");
        String password = scanner.nextLine();
        
        System.out.println("\n" + ANSI_YELLOW + "=== HASHING ALGORITHM PERFORMANCE COMPARISON ===" + ANSI_RESET);
        System.out.println("Testing password: \"" + password + "\"\n");
        
        // Execute comprehensive timing tests for each algorithm
        // Note: Results demonstrate relative performance characteristics
        testHashingAlgorithm(password, "MD5");
        testHashingAlgorithm(password, "SHA-1");
        testHashingAlgorithm(password, "SHA-256");
        testHashingAlgorithm(password, "SHA-512");
        testBCryptAlgorithm(password);
        
        // Display performance analysis summary
        printPerformanceAnalysis();
        
        scanner.close();
    }
    
    /**
     * Display application header with educational context
     * 
     * Purpose: Provides context for the comparison study and emphasizes
     * the importance of secure hashing in compliant systems
     */
    private static void printHeader() {
        System.out.println(ANSI_GREEN + "╔════════════════════════════════════════════════════════════╗");
        System.out.println("║           PASSWORD HASHING ALGORITHM COMPARISON           ║");
        System.out.println("║                                                            ║");
        System.out.println("║  Educational demonstration of cryptographic hash timing   ║");
        System.out.println("║  for compliant password security implementations          ║");
        System.out.println("╚════════════════════════════════════════════════════════════╝" + ANSI_RESET);
        System.out.println();
    }
    
    /**
     * Test and time a specific MessageDigest-based hashing algorithm
     * 
     * @param password The plaintext password to hash
     * @param algorithm The algorithm name (MD5, SHA-1, SHA-256, SHA-512)
     * 
     * SEQUENCE:
     *   1. Record start time in nanoseconds
     *   2. Execute hashing algorithm with error handling
     *   3. Record end time and calculate duration
     *   4. Display formatted results with timing data
     */
    private static void testHashingAlgorithm(String password, String algorithm) {
        // Begin timing measurement for performance analysis
        long startTime = System.nanoTime();
        
        // Execute hashing with comprehensive error handling
        String hash = hashWithMessageDigest(password, algorithm);
        
        // Complete timing measurement and calculate duration
        long endTime = System.nanoTime();
        long durationNanos = endTime - startTime;
        double durationMillis = durationNanos / 1_000_000.0;
        
        // Display results with color coding for readability
        printAlgorithmResults(algorithm, hash, durationMillis, durationNanos);
    }
    
    /**
     * Test and time the bCrypt algorithm with adaptive cost factor
     * 
     * @param password The plaintext password to hash
     * 
     * Purpose: bCrypt is specifically designed for password hashing with
     * built-in salt generation and configurable work factor for compliance
     * 
     * SEQUENCE:
     *   1. Record start time for timing analysis
     *   2. Generate salt and execute bCrypt hashing
     *   3. Calculate execution duration
     *   4. Display results with timing comparison data
     */
    private static void testBCryptAlgorithm(String password) {
        long startTime = System.nanoTime();
        
        // bCrypt uses cost factor 12 for strong security vs. performance balance
        // Higher cost factors provide better security but require more processing time
        String hash = BCrypt.hashpw(password, BCrypt.gensalt(12));
        
        long endTime = System.nanoTime();
        long durationNanos = endTime - startTime;
        double durationMillis = durationNanos / 1_000_000.0;
        
        printAlgorithmResults("bCrypt (cost=12)", hash, durationMillis, durationNanos);
    }
    
    /**
     * Hash password using Java MessageDigest algorithms
     * 
     * @param password The plaintext password to hash
     * @param algorithm The specific algorithm to use
     * @return String representation of the hash in hexadecimal format
     * 
     * SEQUENCE:
     *   1. Initialize MessageDigest instance for specified algorithm
     *   2. Convert password to byte array and digest
     *   3. FOR each byte in hash result DO
     *        Convert to hexadecimal representation
     *   4. Return concatenated hexadecimal string
     * 
     * Error Handling: Returns descriptive error message if algorithm unavailable
     */
    private static String hashWithMessageDigest(String password, String algorithm) {
        try {
            // MessageDigest supports multiple algorithms but not adaptive functions
            // Note: MD5 and SHA-1 are deprecated for new compliant implementations
            MessageDigest md = MessageDigest.getInstance(algorithm);
            
            // Convert password to bytes and compute hash digest
            byte[] hashBytes = md.digest(password.getBytes());
            
            // Convert byte array to hexadecimal string representation
            StringBuilder sb = new StringBuilder();
            for (byte b : hashBytes) {
                // Format each byte as two-digit hexadecimal with leading zeros
                sb.append(String.format("%02x", b));
            }
            
            return sb.toString();
            
        } catch (NoSuchAlgorithmException e) {
            return "Algorithm not found: " + algorithm + " - " + e.getMessage();
        }
    }
    
    /**
     * Display formatted results for a single algorithm test
     * 
     * @param algorithm Name of the algorithm tested
     * @param hash The resulting hash value
     * @param durationMillis Execution time in milliseconds
     * @param durationNanos Execution time in nanoseconds
     * 
     * Purpose: Provides consistent formatting for performance comparison
     * and educational analysis of timing characteristics
     */
    private static void printAlgorithmResults(String algorithm, String hash, 
                                            double durationMillis, long durationNanos) {
        // Color-coded output for enhanced readability and analysis
        System.out.printf("%-20s", ANSI_RED + algorithm + ":" + ANSI_RESET);
        System.out.printf(" %s%s%s\n", ANSI_BLUE, hash.substring(0, Math.min(32, hash.length())), ANSI_RESET);
        
        // Display comprehensive timing data for performance analysis
        System.out.printf("%-20s", "");
        System.out.printf(" %sTime: %.3f ms (%,d ns)%s\n", 
                         ANSI_YELLOW, durationMillis, durationNanos, ANSI_RESET);
        System.out.printf("%-20s", "");
        System.out.printf(" %sHash Length: %d characters%s\n\n", 
                         ANSI_GREEN, hash.length(), ANSI_RESET);
    }
    
    /**
     * Display educational analysis of algorithm performance characteristics
     * 
     * Purpose: Provides context for understanding the timing results in
     * terms of security implications and compliant system design
     */
    private static void printPerformanceAnalysis() {
        System.out.println(ANSI_YELLOW + "=== PERFORMANCE ANALYSIS ===" + ANSI_RESET);
        System.out.println();
        System.out.println(ANSI_GREEN + "Algorithm Security Analysis:" + ANSI_RESET);
        System.out.println("• MD5: " + ANSI_RED + "DEPRECATED" + ANSI_RESET + " - Fast but cryptographically broken");
        System.out.println("• SHA-1: " + ANSI_RED + "DEPRECATED" + ANSI_RESET + " - Faster than SHA-2 but vulnerable");
        System.out.println("• SHA-256: " + ANSI_YELLOW + "ACCEPTABLE" + ANSI_RESET + " - Good security, moderate speed");
        System.out.println("• SHA-512: " + ANSI_YELLOW + "ACCEPTABLE" + ANSI_RESET + " - Higher security, slower processing");
        System.out.println("• bCrypt: " + ANSI_GREEN + "RECOMMENDED" + ANSI_RESET + " - Designed for passwords, adaptive cost");
        System.out.println();
        System.out.println(ANSI_BLUE + "Key Observations:" + ANSI_RESET);
        System.out.println("1. Speed ≠ Security: Faster algorithms are often less secure");
        System.out.println("2. bCrypt's slowness is intentional for brute-force resistance");
        System.out.println("3. Adaptive algorithms like bCrypt remain secure as hardware improves");
        System.out.println("4. Compliant systems should prioritize security over performance");
    }
}
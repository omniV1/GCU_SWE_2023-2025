package com.block;

import java.security.MessageDigest;
import java.sql.Date;
import java.text.DateFormat;

/**
 * Block class
 * Each block represents a single block in the blockchain
 * 
 * Purpose: Demonstrates the fundamental structure of blockchain blocks
 * with cryptographic hashing, timestamp verification, and chain linking
 * for compliant distributed ledger implementations.
 */
public class Block {

    private int id; // sequence number of the block
    private String data; // The data stored in the block
    private String previousHash; // The hash of the previous block
    private String hash; // The hash of the block data

    // time of the block creation. showing date and time
    private Date timestamp;

    /**
     * Block constructor
     * 
     * @param id Unique sequential identifier for the block
     * @param data Information content to be stored in the block
     * @param previousHash Cryptographic hash of the previous block in the chain
     * 
     * SEQUENCE:
     *   1. Initialize block properties with provided parameters
     *   2. Calculate cryptographic hash for block integrity
     *   3. Record creation timestamp for audit trail
     */
    public Block(int id, String data, String previousHash) {
        this.id = id;
        this.data = data;
        this.previousHash = previousHash;
        this.hash = calculateHash();
        // format to show the time when the block was created
        this.timestamp = new Date(System.currentTimeMillis());
    }

    /**
     * calculateHash method
     * Use the SHA-256 algorithm to calculate the hash of the block data
     * 
     * Purpose: Creates cryptographic fingerprint ensuring block integrity
     * and enabling tamper detection in compliant blockchain systems
     * 
     * SEQUENCE:
     *   1. Combine block data with previous hash for chain linkage
     *   2. Apply SHA-256 cryptographic hash function
     *   3. Convert resulting bytes to hexadecimal representation
     *   4. Return hash string for block identification
     */
    public String calculateHash() {
        try {
            // Combine block data with the previous hash
            String input = data + previousHash;
            // Create a SHA-256 digest
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            // Calculate the hash of the input
            byte[] hashBytes = digest.digest(input.getBytes("UTF-8"));
            // Convert the byte[] into a hex string
            return bytesToHex(hashBytes);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    /**
     * Helper method to convert byte array to hex string
     * 
     * @param hashBytes Byte array from cryptographic hash function
     * @return String representation in hexadecimal format
     * 
     * Purpose: Converts binary hash output to human-readable format
     * for display and verification in compliant systems
     */
    private String bytesToHex(byte[] hashBytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : hashBytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    // Getter methods for accessing block properties
    public int getId() {
        return id;
    }

    public String getData() {
        return data;
    }

    public String getPreviousHash() {
        return previousHash;
    }

    public String getHash() {
        return hash;
    }

    // Setter methods for modifying block properties
    public void setId(int id) {
        this.id = id;
    }

    public void setData(String data) {
        this.data = data;
    }

    public void setPreviousHash(String previousHash) {
        this.previousHash = previousHash;
    }

    public void setHash(String hash) {
        this.hash = hash;
    }

    /**
     * toString method creates a box with the block information
     * 
     * Purpose: Provides formatted visual representation of block structure
     * with color-coded information for educational blockchain analysis
     * 
     * SEQUENCE:
     *   1. Define ANSI color codes for visual differentiation
     *   2. Format block properties with appropriate colors
     *   3. Calculate maximum content width for alignment
     *   4. Create bordered box with padded content
     *   5. Add visual connector showing chain linkage
     */
    @Override
    public String toString() {
        // Define ANSI color codes
        final String RESET = "\033[0m";
        final String RED = "\033[31m";
        final String GREEN = "\033[32m";
        final String YELLOW = "\033[33m";
        final String BLUE = "\033[34m";
        final String MAGENTA = "\033[35m";

        // Define the block content with color
        String line1 = RED + "Block ID: " + id + RESET;
        String line2 = GREEN + "Block data: " + data + RESET;
        String line3 = YELLOW + "Block hash: " + hash + RESET;
        String line4 = BLUE + "Block previous hash: " + previousHash + RESET;

        DateFormat dateFormat = DateFormat.getDateTimeInstance();

        String output = dateFormat.format(timestamp);
        String line5 = MAGENTA + "Block timestamp: " + output + RESET;

        // Calculate the maximum length of content, ignoring ANSI codes
        int maxLength = Math.max(Math.max(visibleLength(line1), visibleLength(line2)), Math.max(visibleLength(line3), visibleLength(line4)));

        // Create padding to make the content align inside the box
        String border = "+-" + "-".repeat(maxLength) + "-+";
        String paddedLine1 = "| " + padRight(line1, maxLength) + " |";
        String paddedLine2 = "| " + padRight(line2, maxLength) + " |";
        String paddedLine3 = "| " + padRight(line3, maxLength) + " |";
        String paddedLine4 = "| " + padRight(line4, maxLength) + " |";
        String paddedLine5 = "| " + padRight(line5, maxLength) + " |";
        String connector = " ".repeat(maxLength / 2) + "|" + "\n" +
                " ".repeat(maxLength / 2) + "V";

        // Return the box with dynamic padding and colored lines
        return border + "\n" +
                paddedLine1 + "\n" +
                paddedLine2 + "\n" +
                paddedLine3 + "\n" +
                paddedLine4 + "\n" +
                paddedLine5 + "\n" +
                border + "\n" +
                connector;
    }

    /**
     * Helper method to calculate the visible length of a string without ANSI codes
     * 
     * @param str String containing ANSI color codes
     * @return Integer length of visible characters only
     * 
     * Purpose: Ensures proper text alignment by excluding formatting codes
     * from length calculations for display consistency
     */
    private int visibleLength(String str) {
        // strip out the ANSI color codes and return the length using regex pattern that matches ANSI color codes
        return str.replaceAll("\\u001B\\[[;\\d]*m", "").length();
    }

    /**
     * Helper method to pad the content with spaces to the right, based on visible length
     * 
     * @param str String to be padded
     * @param totalLength Target length for padding
     * @return String with appropriate right padding
     * 
     * Purpose: Maintains consistent formatting and alignment in block display
     * regardless of ANSI color code presence
     */
    private String padRight(String str, int totalLength) {
        int visibleLen = visibleLength(str);
        return str + " ".repeat(totalLength - visibleLen);
    }
}

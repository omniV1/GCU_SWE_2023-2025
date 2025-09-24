package com.block;

/**
 * Blockchain Demonstration Application
 * 
 * Purpose: Interactive demonstration of blockchain fundamentals including
 * block creation, cryptographic linking, and chain integrity verification
 * for educational understanding of compliant distributed ledger technology.
 * 
 * Educational Objectives:
 * - Demonstrate block structure and hashing mechanisms
 * - Show chain linkage through previous hash references
 * - Illustrate timestamp-based audit trails
 * - Provide hands-on blockchain construction experience
 * 
 * Author: CST-407 Class Project
 * Date: September 2025
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class App {
    
    /**
     * Main application entry point for blockchain demonstration
     * 
     * SEQUENCE:
     *   1. Initialize blockchain as ArrayList collection
     *   2. Create genesis block with default parameters
     *   3. WHILE user wants to continue DO
     *        a. Prompt for block data input
     *        b. Create new block linked to previous
     *        c. Add block to blockchain collection
     *        d. Display current blockchain state
     *        e. Query user for continuation
     *   4. Terminate demonstration gracefully
     */
    public static void main(String[] args) {
        // Initialize blockchain data structure for block storage
        List<Block> blockchain = new ArrayList<Block>();
        
        // Create genesis block - the foundational block of every blockchain
        // Genesis blocks have no previous hash, conventionally set to "0"
        Block genesisBlock = new Block(0, "Genesis Block", "0");

        // Display genesis block creation confirmation
        System.out.println("Genesis Block created!");
        System.out.println(genesisBlock.toString());
        blockchain.add(genesisBlock);

        // Scanner for user input - replaced System.console() for IDE compatibility
        Scanner scanner = new Scanner(System.in);
        
        // Main demonstration loop for interactive block creation
        boolean finished = false;
        while (!finished) {
            System.out.println("Enter the data for the next block:");
            String data = scanner.nextLine();
            
            // Create new block with incremented ID, user data, and previous block's hash
            // This demonstrates the cryptographic linking that secures blockchain integrity
            Block newBlock = new Block(genesisBlock.getId() + 1, data, genesisBlock.getHash());
            genesisBlock = newBlock; // Update reference to most recent block
            
            System.out.println("Block added to the blockchain!");
            blockchain.add(genesisBlock);
            
            // Display complete blockchain state for verification
            printBlocks(blockchain);
            
            System.out.println("Would you like to add another block? (y/n)");
            String response = scanner.nextLine();
            
            // Continue loop IF user responds with 'y', terminate otherwise
            if (!response.equals("y")) {
                finished = true;
            }
        }
        
        // Clean up resources
        scanner.close();
        System.out.println("Blockchain demonstration completed.");
    }

    /**
     * Display formatted blockchain visualization
     * 
     * @param blockchain List of Block objects representing the complete chain
     * 
     * Purpose: Provides comprehensive view of blockchain structure showing
     * block relationships, hash linkage, and temporal sequence for educational
     * analysis of compliant distributed ledger properties
     * 
     * SEQUENCE:
     *   1. Display blockchain header for context
     *   2. FOR each block in blockchain DO
     *        Display formatted block information with visual connectors
     *   3. Provide summary statistics for analysis
     */
    private static void printBlocks(List<Block> blockchain) {
        // Display header with educational context
        System.out.println("\n" + "=".repeat(60));
        System.out.println("           BLOCKCHAIN STRUCTURE VISUALIZATION");
        System.out.println("=".repeat(60));
        
        // Display each block with numbered sequence for clarity
        for (int i = 0; i < blockchain.size(); i++) {
            Block block = blockchain.get(i);
            System.out.println("Block #" + (i + 1) + " in Chain:");
            System.out.println(block.toString());
            
            // Add spacing between blocks for readability
            if (i < blockchain.size() - 1) {
                System.out.println(); // Extra line for visual separation
            }
        }
        
        // Provide blockchain summary statistics
        System.out.println("=".repeat(60));
        System.out.println("Blockchain Summary:");
        System.out.println("• Total Blocks: " + blockchain.size());
        System.out.println("• Genesis Block ID: " + blockchain.get(0).getId());
        
        if (blockchain.size() > 1) {
            Block lastBlock = blockchain.get(blockchain.size() - 1);
            System.out.println("• Latest Block ID: " + lastBlock.getId());
            System.out.println("• Chain Integrity: " + verifyChainIntegrity(blockchain));
        }
        
        System.out.println("=".repeat(60) + "\n");
    }
    
    /**
     * Verify blockchain integrity through hash validation
     * 
     * @param blockchain List of blocks to validate
     * @return String indicating validation status
     * 
     * Purpose: Demonstrates cryptographic verification process essential
     * for compliant blockchain systems to detect tampering or corruption
     * 
     * SEQUENCE:
     *   1. FOR each block after genesis DO
     *        a. Verify previous hash matches actual previous block hash
     *        b. IF mismatch found THEN return failure status
     *   2. IF all verifications pass THEN return success status
     */
    private static String verifyChainIntegrity(List<Block> blockchain) {
        for (int i = 1; i < blockchain.size(); i++) {
            Block currentBlock = blockchain.get(i);
            Block previousBlock = blockchain.get(i - 1);
            
            // Verify that current block's previousHash matches previous block's hash
            if (!currentBlock.getPreviousHash().equals(previousBlock.getHash())) {
                return "COMPROMISED - Hash mismatch detected at block " + i;
            }
        }
        return "VERIFIED - All cryptographic links valid";
    }
}
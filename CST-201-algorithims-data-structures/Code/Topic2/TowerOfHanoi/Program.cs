/*
 * Owen Lindsey
 * Professor Demland, David
 * CST-201
 * Complexity
 * 10/6/2024
 * This work is my own
 */ 


using System;
using System.Collections.Generic;

class Program
{
    class TowerOfHanoi
    {
        // List to represent the three towers (A, B, C)
        static List<Stack<int>> towers = new List<Stack<int>>();

        static void InitializeTowers(int numDisks)
        {
            // Clear any existing data in the towers
            towers.Clear();

            // Create three empty stacks to represent the towers
            towers.Add(new Stack<int>()); // Tower A
            towers.Add(new Stack<int>()); // Tower B
            towers.Add(new Stack<int>()); // Tower C

            // Place all disks on the first tower (A) in descending order of size
            for (int i = numDisks; i >= 1; i--)
            {
                towers[0].Push(i);
            }

            // Display the initial state of the towers
            PrintTowers(numDisks);
        }
        /// <summary>
        /// This method correctly moves all disks from the source peg to the destination peg
        /// using an auxiliary peg
        /// </summary>
        /// <param name="numDisks">The total number of disks to be moved</param>
        /// <param name="source">The index of the source peg (0 for A)</param>
        /// <param name="destination">The index of the destination peg (2 for C)</param>
        /// <param name="auxiliary">The index of the auxiliary peg (1 for B)</param>
        static int[] MoveDisksIterative(int numDisks, int source, int destination, int auxiliary)
        {
            int totalMoves = (1 << numDisks) - 1; // 2^n - 1
            int[] diskMoves = new int[numDisks]; // Array to store moves for each disk

            for (int move = 1; move <= totalMoves; move++)
            {
                int from = (move & move - 1) % 3;
                int to = ((move | move - 1) + 1) % 3;

                // Map the calculated indices to the actual tower indices
                from = (from == 0) ? source : (from == 1) ? auxiliary : destination;
                to = (to == 0) ? source : (to == 1) ? auxiliary : destination;

                // Determine which disk is being moved
                int diskSize = GetDiskSize(from, to);

                // Increment the move count for this disk
                // Note: diskSize - 1 is used as index because array is 0-indexed
                diskMoves[diskSize - 1]++;

                MoveSingleDisk(from, to, numDisks);
            }

            return diskMoves;
        }

        /// <summary>
        /// Determines the size of the disk being moved.
        /// </summary>
        /// <param name="from">Source peg index.</param>
        /// <param name="to">Destination peg index.</param>
        /// <returns>The size of the disk being moved.</returns>
        static int GetDiskSize(int from, int to)
        {
            // The disk being moved is always the top disk on the 'from' tower
            return towers[from].Peek();
        }


        /// <summary>
        /// Moves a single disk from the source peg to the destination peg if the move is valid
        /// </summary>
        /// <param name="source">The index of the source peg (0 for A, 1 for B, 2 for C)</param>
        /// <param name="destination">The index of the destination peg (0 for A, 1 for B, 2 for C)</param>
        /// <param name="totalDisks">The total number of disks in the puzzle, used for display purposes</param>
        static void MoveSingleDisk(int source, int destination, int totalDisks)
        {
            // Check if the move is valid:
            // 1. Source peg has at least one disk
            // 2. Either destination peg is empty or the top disk on source is smaller than the top disk on destination
            if (towers[source].Count > 0 &&
                (towers[destination].Count == 0 || towers[source].Peek() < towers[destination].Peek()))
            {
                // Remove the top disk from the source peg
                int disk = towers[source].Pop();
                // Add the disk to the destination peg
                towers[destination].Push(disk);
                // Display the current state of the towers after the move
                PrintTowers(totalDisks);
            }
        }

        /// <summary>
        /// Prints the current state of the Tower of Hanoi puzzle to the console
        /// Displays the disks on each tower and labels the towers A, B, and C
        /// </summary>
        /// <param name="totalDisks">The total number of disks in the puzzle</param>
        static void PrintTowers(int totalDisks)
        {
            Console.Clear();
            Console.WriteLine("Towers:");

            // Calculate the width for each tower's display area
            int towerWidth = (totalDisks * 2) + 3; // 2 * max disk width + 1 for center + 2 for spacing

            // Iterate through each level of the towers, from top to bottom
            for (int level = totalDisks - 1; level >= 0; level--)
            {
                // Print each of the three towers side by side
                for (int i = 0; i < 3; i++)
                {
                    if (towers[i].Count > level)
                    {
                        // If there's a disk at this level, calculate its size and print it
                        int disk = towers[i].ToArray()[towers[i].Count - level - 1];
                        PrintDisk(disk, totalDisks, towerWidth);
                    }
                    else
                    {
                        // If no disk, print empty space with a centered vertical bar
                        Console.Write($"{new string(' ', (towerWidth - 1) / 2)}|{new string(' ', towerWidth / 2)}");
                    }
                }
                Console.WriteLine(); // Move to the next line after printing all three towers
            }

            // Print labels (A, B, C) for the towers
            for (int i = 0; i < 3; i++)
            {
                char label = (char)('A' + i); // Convert 0, 1, 2 to 'A', 'B', 'C'
                Console.Write($"{new string(' ', (towerWidth - 1) / 2)}{label}{new string(' ', towerWidth / 2)}");
            }
            Console.WriteLine();
            Console.WriteLine();

            // Pause briefly to make the visualization easier to follow
            System.Threading.Thread.Sleep(500);
        }

        /// <summary>
        /// Prints a single disk for the Tower of Hanoi puzzle
        /// Disks are represented by '=' characters and colored alternately
        /// </summary>
        /// <param name="size">The size of the disk to print</param>
        /// <param name="totalDisks">The total number of disks in the puzzle</param>
        /// <param name="towerWidth">The width of each tower's display area</param>
        static void PrintDisk(int size, int totalDisks, int towerWidth)
        {
            // Set color based on disk size (cyan for even, yellow for odd)
            Console.ForegroundColor = size % 2 == 0 ? ConsoleColor.Cyan : ConsoleColor.Yellow;

            // Create a string of '=' characters to represent the disk
            string disk = new string('=', size * 2 - 1);

            // Calculate padding to center the disk within the tower width
            int padding = (towerWidth - disk.Length) / 2;

            // Print the disk with appropriate padding
            Console.Write($"{new string(' ', padding)}{disk}{new string(' ', padding)}");

            // Reset console color for subsequent output
            Console.ResetColor();
        }

        static void Main()
        {
            Console.WriteLine("Enter the number of disks:");
            int numDisks = int.Parse(Console.ReadLine());

            InitializeTowers(numDisks);

            int[] diskMoves = MoveDisksIterative(numDisks, 0, 2, 1);

            Console.WriteLine("Puzzle solved!");
            Console.WriteLine("Enter the rank of the disk to see its number of moves (1 for largest, " + numDisks + " for smallest):");
            int rank = int.Parse(Console.ReadLine());

            if (rank >= 1 && rank <= numDisks)
            {
                Console.WriteLine($"The {rank}th largest disk moved {diskMoves[rank - 1]} times.");
            }
            else
            {
                Console.WriteLine("Invalid rank entered.");
            }
        }
    }
}
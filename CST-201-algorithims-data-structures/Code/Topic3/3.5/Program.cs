using System;


   public class NetworkTopologyIdentifier
{
    // Main method to identify the network topology
    public static string IdentifyTopology(bool[,] A)
    {
        // Get the size of the matrix (number of nodes)
        int n = A.GetLength(0);

        // Check if the number of nodes meets the problem's requirement
        if (n <= 3) return "Invalid: n must be greater than 3";

        // Check for each topology in order
        if (IsRing(A, n)) return "Ring";
        if (IsStar(A, n)) return "Star";
        if (IsFullyConnectedMesh(A, n)) return "Fully Connected Mesh";

        // If none of the topologies match, return this message
        return "None of the given topologies";
    }
private static bool IsRing(bool[,] A, int n)
{
    // Check if each node has exactly two connections
    for (int i = 0; i < n; i++)
    {
        int connections = 0;
        for (int j = 0; j < n; j++)
        {
            if (A[i, j]) connections++;
        }
        if (connections != 2) return false;
    }

    // Check if the connections form a single cycle
    bool[] visited = new bool[n];
    int current = 0;
    int count = 0;

    while (count < n)
    {
        visited[current] = true;
        count++;

        // Find the next unvisited neighbor
        int next = -1;
        for (int j = 0; j < n; j++)
        {
            if (A[current, j] && !visited[j])
            {
                next = j;
                break;
            }
        }

        // If we can't find an unvisited neighbor
        if (next == -1)
        {
            // If we've visited all nodes, check if we can return to the start
            if (count == n)
            {
                for (int j = 0; j < n; j++)
                {
                    if (A[current, j] && j == 0) return true;
                }
            }
            return false;
        }

        current = next;
    }
// This line should never be reached in a valid ring
    return false; 
}

// Helper method to get the next unvisited neighbor in the ring
private static int GetNextUnvisitedNeighbor(bool[,] A, int current, bool[] visited)
{
    for (int i = 0; i < A.GetLength(0); i++)
    {
        if (A[current, i] && !visited[i]) return i;
    }
    return -1;
}

    // Method to check if the topology is a star
    private static bool IsStar(bool[,] A, int n)
    {
        // Counter for potential center nodes (should be 1 for a star)
        int centerNodeCount = 0;

        // Counter for leaf nodes (should be n-1 for a star)
        int leafNodeCount = 0;

        // Iterate through each node
        for (int i = 0; i < n; i++)
        {
            // Counter for connections of the current node
            int connections = 0;

            // Check connections with all other nodes
            for (int j = 0; j < n; j++)
            {
                // If there's a connection, increment the counter
                if (A[i, j]) connections++;
            }

            // If node has n-1 connections, it's a potential center node
            if (connections == n - 1)
                centerNodeCount++;
            // If node has 1 connection, it's a potential leaf node
            else if (connections == 1)
                leafNodeCount++;
            // If node has any other number of connections, it's not a star
            else
                return false;
        }

        // It's a star if there's 1 center node and n-1 leaf nodes
        return (centerNodeCount == 1 && leafNodeCount == n - 1);
    }

    // Method to check if the topology is a fully connected mesh
    private static bool IsFullyConnectedMesh(bool[,] A, int n)
    {
        // Iterate through each pair of nodes
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                // If it's the same node, there should be no self-connection
                if (i == j && A[i, j]) return false;

                // If it's a different node, there should be a connection
                if (i != j && !A[i, j]) return false;
            }
        }

        // If all checks pass, it's a fully connected mesh
        return true;
    }


 // Main method to demonstrate the topology identification
    public static void Main(string[] args)
    {
        // Example adjacency matrix to be identified
        bool[,] exampleMatrix = {
            {false, true, false, false, true},
            {true, false, true, false, false},
            {false, true, false, true, false},
            {false, false, true, false, true},
            {true, false, false, true, false}
        };

        // Identify the topology of the example matrix
        string result = IdentifyTopology(exampleMatrix);

        // Output the result
        Console.WriteLine("The given adjacency matrix represents a: " + result);

        // Explain the time efficiency
        Console.WriteLine("\nTime Efficiency Analysis:");
        Console.WriteLine("The algorithm has a time complexity of O(n^2), where n is the number of nodes.");
        Console.WriteLine("This is because we potentially check every element of the n x n adjacency matrix");
        Console.WriteLine("for each topology type (ring, star, and fully connected mesh).");
    }
}
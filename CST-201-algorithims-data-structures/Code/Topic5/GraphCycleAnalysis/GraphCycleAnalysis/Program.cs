using System;
using System.Collections.Generic;

/// <summary>
/// Provides functionality to analyze weighted directed graphs and find minimum weight cycles.
/// </summary>
public class GraphAnalyzer
{
    /// <summary>
    /// Represents the counts of operations performed during graph analysis.
    /// </summary>
    public struct OperationCounts
    {
        /// <summary>
        /// The number of comparison operations performed.
        /// </summary>
        public int Comparisons;

        /// <summary>
        /// The number of data exchange operations performed.
        /// </summary>
        public int DataExchanges;
    }

    /// <summary>
    /// Represents information about a cycle found in the graph.
    /// </summary>
    public struct CycleInfo
    {
        /// <summary>
        /// The sequence of vertices forming the cycle.
        /// </summary>
        public List<int> Path;

        /// <summary>
        /// The total weight of all edges in the cycle.
        /// </summary>
        public int Weight;
    }

    private readonly int[,] weightMatrix;    // Adjacency matrix representing the graph
    private readonly int vertices;           // Number of vertices in the graph
    private OperationCounts counts;          // Tracks operation counts
    private List<CycleInfo> minimumCycles;   // Stores all cycles with minimum weight
    private int minimumWeight;               // Weight of the minimum cycle(s)
    private HashSet<string> usedEdges;       // Tracks edges used in current path

    /// <summary>
    /// Initializes a new instance of the GraphAnalyzer class.
    /// </summary>
    /// <param name="matrix">The adjacency matrix representing the weighted directed graph.
    /// Use int.MaxValue to represent absence of edges between vertices.</param>
    /// <exception cref="ArgumentNullException">Thrown when matrix is null.</exception>
    public GraphAnalyzer(int[,] matrix)
    {
        if (matrix == null)
            throw new ArgumentNullException(nameof(matrix), "Weight matrix cannot be null");

        weightMatrix = matrix;
        vertices = matrix.GetLength(0);
        counts = new OperationCounts();
        minimumCycles = new List<CycleInfo>();
        minimumWeight = int.MaxValue;
        usedEdges = new HashSet<string>();
    }

    /// <summary>
    /// Finds all minimum weight cycles in the graph and counts operations performed.
    /// Time Complexity: O(V * E) where V is number of vertices and E is number of edges.
    /// Space Complexity: O(V) for storing the current path and used edges.
    /// </summary>
    /// <returns>An OperationCounts struct containing the number of comparisons and data exchanges.</returns>
    public OperationCounts FindMinimumWeightCycles()
    {
        for (int startVertex = 0; startVertex < vertices; startVertex++)
        {
            for (int nextVertex = 0; nextVertex < vertices; nextVertex++)
            {
                counts.Comparisons++;
                if (weightMatrix[startVertex, nextVertex] != int.MaxValue)
                {
                    counts.DataExchanges++;
                    usedEdges.Clear();
                    var currentPath = new List<int> { startVertex };
                    ExplorePathsFromVertex(startVertex, nextVertex, currentPath, 0);
                }
            }
        }
        return counts;
    }

    /// <summary>
    /// Recursively explores paths from the current vertex to find cycles.
    /// </summary>
    /// <param name="startVertex">The vertex where the cycle should end.</param>
    /// <param name="currentVertex">The current vertex being explored.</param>
    /// <param name="path">The current path being explored.</param>
    /// <param name="currentWeight">The accumulated weight of the current path.</param>
    private void ExplorePathsFromVertex(int startVertex, int currentVertex, List<int> path, int currentWeight)
    {
        string edgeKey = $"{path[path.Count - 1]}-{currentVertex}";

        // Check if edge has been used
        counts.Comparisons++;
        if (usedEdges.Contains(edgeKey))
            return;

        // Record the edge usage
        counts.DataExchanges++;
        usedEdges.Add(edgeKey);
        path.Add(currentVertex);
        currentWeight += weightMatrix[path[path.Count - 2], currentVertex];
        counts.DataExchanges++;

        // Check for cycle completion
        counts.Comparisons++;
        if (currentVertex == startVertex && path.Count > 2)
        {
            ProcessFoundCycle(path, currentWeight);
        }
        else
        {
            ExploreNextVertices(startVertex, currentVertex, path, currentWeight);
        }
    }

    /// <summary>
    /// Processes a newly found cycle, updating minimum cycles if applicable.
    /// </summary>
    private void ProcessFoundCycle(List<int> path, int currentWeight)
    {
        counts.Comparisons++;
        if (currentWeight < minimumWeight)
        {
            counts.DataExchanges++;
            minimumWeight = currentWeight;
            minimumCycles.Clear();
            minimumCycles.Add(new CycleInfo
            {
                Path = new List<int>(path),
                Weight = currentWeight
            });
        }
        else if (currentWeight == minimumWeight)
        {
            counts.DataExchanges++;
            minimumCycles.Add(new CycleInfo
            {
                Path = new List<int>(path),
                Weight = currentWeight
            });
        }
    }

    /// <summary>
    /// Explores all possible next vertices from the current position.
    /// </summary>
    private void ExploreNextVertices(int startVertex, int currentVertex, List<int> path, int currentWeight)
    {
        for (int nextVertex = 0; nextVertex < vertices; nextVertex++)
        {
            counts.Comparisons++;
            if (weightMatrix[currentVertex, nextVertex] != int.MaxValue)
            {
                string potentialEdge = $"{currentVertex}-{nextVertex}";
                counts.Comparisons++;
                if (!usedEdges.Contains(potentialEdge))
                {
                    ExplorePathsFromVertex(startVertex, nextVertex, new List<int>(path), currentWeight);
                }
            }
        }
    }

    /// <summary>
    /// Prints the analysis results including operation counts and found cycles.
    /// </summary>
    public void PrintResults()
    {
        Console.WriteLine($"Number of Comparisons: {counts.Comparisons}");
        Console.WriteLine($"Number of Data Exchanges: {counts.DataExchanges}");
        Console.WriteLine("\nMinimum Weight Cycles:");

        foreach (var cycle in minimumCycles)
        {
            Console.WriteLine($"Weight: {cycle.Weight}");
            Console.WriteLine($"Path: {string.Join(" -> ", cycle.Path)}");
        }
    }
}

/// <summary>
/// Main program class that demonstrates the usage of GraphAnalyzer.
/// </summary>
class Program
{
    /// <summary>
    /// Entry point of the program.
    /// Creates a sample graph and analyzes it for minimum weight cycles.
    /// </summary>
    static void Main(string[] args)
    {
        // Example graph represented as an adjacency matrix
        int[,] weightMatrix = new int[,]
        {
            {0, 3, -4, int.MaxValue},
            {int.MaxValue, 0, 0, int.MaxValue},
            {int.MaxValue, 2, 0, 2},
            {int.MaxValue, int.MaxValue, 0, 0}
        };

        try
        {
            var analyzer = new GraphAnalyzer(weightMatrix);
            var results = analyzer.FindMinimumWeightCycles();
            analyzer.PrintResults();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
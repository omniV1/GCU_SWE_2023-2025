using System;
using System.Collections.Generic;

namespace GraphCycleAnalysis
{
    /// <summary>
    /// Analyzes directed graphs to find minimum weight cycles and track operation counts.
    /// This class implements an algorithm to find all possible cycles with minimum weight
    /// in a directed graph where edges cannot be traversed more than once.
    /// </summary>
    public class GraphAnalyzer
    {
        /// <summary>
        /// The adjacency matrix representing the weighted directed graph.
        /// int.MaxValue represents no edge between vertices.
        /// </summary>
        private readonly int[,] weightMatrix;

        /// <summary>
        /// The number of vertices in the graph.
        /// </summary>
        private readonly int vertices;

        /// <summary>
        /// Tracks the number of comparisons and data exchanges during algorithm execution.
        /// </summary>
        private OperationCounts counts;

        /// <summary>
        /// Stores all cycles found with the minimum weight.
        /// Multiple cycles may share the same minimum weight.
        /// </summary>
        private List<CycleInfo> minimumCycles;

        /// <summary>
        /// The weight of the minimum weight cycle(s) found.
        /// Initialized to int.MaxValue and updated as cycles are found.
        /// </summary>
        private int minimumWeight;

        /// <summary>
        /// Tracks edges that have been used in the current path exploration.
        /// Prevents reusing edges in the same cycle.
        /// </summary>
        private HashSet<string> usedEdges;

        /// <summary>
        /// Initializes a new instance of the GraphAnalyzer class.
        /// </summary>
        /// <param name="matrix">The adjacency matrix representing the weighted directed graph.
        /// Use int.MaxValue to represent no edge between vertices.</param>
        /// <exception cref="ArgumentNullException">Thrown when matrix is null.</exception>
        public GraphAnalyzer(int[,] matrix)
        {
            if (matrix == null)
                throw new ArgumentNullException(nameof(matrix));

            weightMatrix = matrix;
            vertices = matrix.GetLength(0);
            counts = new OperationCounts();
            minimumCycles = new List<CycleInfo>();
            minimumWeight = int.MaxValue;
            usedEdges = new HashSet<string>();
        }

        /// <summary>
        /// Finds all minimum weight cycles in the graph and counts operations performed.
        /// </summary>
        /// <returns>An OperationCounts struct containing the number of comparisons and data exchanges performed.</returns>
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
        /// Updates minimumCycles and minimumWeight when a new minimum weight cycle is found.
        /// </summary>
        /// <param name="startVertex">The vertex where the cycle should end.</param>
        /// <param name="currentVertex">The current vertex being explored.</param>
        /// <param name="path">The current path being explored.</param>
        /// <param name="currentWeight">The total weight of the current path.</param>
        private void ExplorePathsFromVertex(int startVertex, int currentVertex, List<int> path, int currentWeight)
        {
            string edgeKey = $"{path[path.Count - 1]}-{currentVertex}";
            counts.Comparisons++;
            if (usedEdges.Contains(edgeKey))
            {
                return;
            }

            counts.DataExchanges++;
            usedEdges.Add(edgeKey);
            path.Add(currentVertex);
            currentWeight += weightMatrix[path[path.Count - 2], currentVertex];
            counts.DataExchanges++;

            counts.Comparisons++;
            if (currentVertex == startVertex && path.Count > 2)
            {
                ProcessCycleFound(path, currentWeight);
            }
            else
            {
                ExploreNextVertices(startVertex, currentVertex, path, currentWeight);
            }
        }

        /// <summary>
        /// Gets the list of all minimum weight cycles found.
        /// </summary>
        /// <returns>A List of CycleInfo containing all cycles with minimum weight.</returns>
        public List<CycleInfo> GetMinimumCycles()
        {
            return minimumCycles;
        }

        /// <summary>
        /// Gets the minimum cycle weight found.
        /// </summary>
        /// <returns>The weight of the minimum weight cycle(s).</returns>
        public int GetMinimumWeight()
        {
            return minimumWeight;
        }

        /// <summary>
        /// Prints the algorithm execution results including operation counts and cycle information.
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

        /// <summary>
        /// Processes a found cycle, updating minimumCycles if it has the minimum weight.
        /// </summary>
        /// <param name="path">The path forming the cycle.</param>
        /// <param name="currentWeight">The total weight of the cycle.</param>
        private void ProcessCycleFound(List<int> path, int currentWeight)
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
        /// Explores all possible next vertices from the current vertex.
        /// </summary>
        /// <param name="startVertex">The vertex where the cycle should end.</param>
        /// <param name="currentVertex">The current vertex being explored.</param>
        /// <param name="path">The current path being explored.</param>
        /// <param name="currentWeight">The total weight of the current path.</param>
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
    }
}
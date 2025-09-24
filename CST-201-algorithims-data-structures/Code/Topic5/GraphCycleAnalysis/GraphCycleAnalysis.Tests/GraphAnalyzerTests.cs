using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;

namespace GraphCycleAnalysis.Tests
{
    /// <summary>
    /// Test class for GraphAnalyzer implementation.
    /// Tests various scenarios including valid and invalid inputs,
    /// different cycle types, and edge cases.
    /// </summary>
    [TestClass]
    public class GraphCycleAnalysisTests
    {
        private GraphAnalyzer analyzer;


        /// <summary>
        /// Helper method to print cycle information for debugging.
        /// </summary>
        private void PrintCycleInfo(List<CycleInfo> cycles, int[,] matrix)
        {
            Console.WriteLine($"Found {cycles.Count} cycles:");
            foreach (var cycle in cycles)
            {
                Console.WriteLine($"Path: {string.Join("->", cycle.Path)}");
                Console.WriteLine($"Weight: {cycle.Weight}");

                // Verify each edge
                Console.WriteLine("Edge weights:");
                for (int i = 0; i < cycle.Path.Count - 1; i++)
                {
                    Console.WriteLine($"{cycle.Path[i]}->{cycle.Path[i + 1]}: {matrix[cycle.Path[i], cycle.Path[i + 1]]}");
                }
                Console.WriteLine();
            }
        }

        /// <summary>
        /// Initializes test environment before each test method.
        /// Creates a standard test matrix with known properties:
        /// - Contains negative weights
        /// - Has multiple possible paths
        /// - Includes unreachable vertices (represented by int.MaxValue)
        /// </summary>
        [TestInitialize]
        public void Setup()
        {
            int[,] testMatrix = new int[,]
            {
                {0, 3, -4, int.MaxValue},
                {int.MaxValue, 0, 0, int.MaxValue},
                {int.MaxValue, 2, 0, 2},
                {int.MaxValue, int.MaxValue, 0, 0}
            };
            analyzer = new GraphAnalyzer(testMatrix);
        }

        /// <summary>
        /// Tests if the GraphAnalyzer constructor properly handles valid input.
        /// Verifies that a valid matrix creates a non-null analyzer instance.
        /// </summary>
        [TestMethod]
        public void TestGraphAnalyzer_Constructor_ValidMatrix()
        {
            // Arrange
            int[,] matrix = new int[,]
            {
                {0, 1},
                {1, 0}
            };

            // Act
            var testAnalyzer = new GraphAnalyzer(matrix);

            // Assert
            Assert.IsNotNull(testAnalyzer);
        }

        /// <summary>
        /// Tests if the cycle finding algorithm properly counts operations.
        /// Verifies that both comparisons and data exchanges occur during execution.
        /// </summary>
        [TestMethod]
        public void TestGraphAnalyzer_FindMinimumWeightCycles_ReturnsValidCounts()
        {
            // Act
            var result = analyzer.FindMinimumWeightCycles();

            // Assert
            Assert.IsTrue(result.Comparisons > 0, "Should have some comparisons");
            Assert.IsTrue(result.DataExchanges > 0, "Should have some data exchanges");
        }

        /// <summary>
        /// Tests if the algorithm correctly finds the minimum weight cycle in a simple graph.
        /// Uses a 2x2 matrix with a known cycle weight of 2.
        /// </summary>
        [TestMethod]
        public void TestGraphAnalyzer_SmallCycle_CorrectMinimumWeight()
        {
            // Arrange
            int[,] smallMatrix = new int[,]
            {
                {0, 1},
                {1, 0}
            };
            var smallAnalyzer = new GraphAnalyzer(smallMatrix);

            // Act
            var result = smallAnalyzer.FindMinimumWeightCycles();

            // Assert - We expect a cycle with weight 2 (1 + 1)
            Assert.AreEqual(2, GetPrivateField<int>(smallAnalyzer, "minimumWeight"));
        }

        /// <summary>
        /// Tests whether the operation counts are accurate for a simple 2x2 matrix case.
        /// 
        /// For a 2x2 matrix with values:
        /// [0 1]
        /// [1 0]
        /// 
        /// Data Exchanges (36 total):
        /// 1. Initial Phase (per vertex exploration):
        ///    - usedEdges.Clear(): 4 exchanges
        ///    - Creating new path list: 4 exchanges
        ///    - Initial path.Add: 4 exchanges
        ///    
        /// 2. Path Exploration:
        ///    - usedEdges.Add: 4 exchanges
        ///    - path.Add operations: 4 exchanges
        ///    - Weight calculations: 4 exchanges
        ///    
        /// 3. Cycle Recording:
        ///    - New CycleInfo creation: 4 exchanges
        ///    - Path copying: 4 exchanges
        ///    - Adding to minimumCycles: 4 exchanges
        /// </summary>
        [TestMethod]
        public void TestGraphAnalyzer_OperationCounts_Accuracy()
        {
            // Arrange
            int[,] simpleMatrix = new int[,]
            {
            {0, 1},
            {1, 0}
            };
            var simpleAnalyzer = new GraphAnalyzer(simpleMatrix);

            // Act
            var result = simpleAnalyzer.FindMinimumWeightCycles();

            // Assert
            Assert.AreEqual(76, result.Comparisons, "Number of comparisons matches algorithm implementation");
            Assert.AreEqual(36, result.DataExchanges, "Number of data exchanges matches algorithm implementation");

            // Print detailed counts for verification
            Console.WriteLine($"Actual Comparisons: {result.Comparisons}");
            Console.WriteLine($"Actual Data Exchanges: {result.DataExchanges}");
        }

        /// <summary>
        /// Tests whether the path in the found cycle is correct and complete.
        /// Uses a simple graph with a known minimum cycle.
        /// The minimum cycle should be 0->1->2->0 with weight 3.
        /// </summary>
        [TestMethod]
        public void TestGraphAnalyzer_CyclePath_Correctness()
        {
            // Arrange - Create a graph with a clear minimum cycle
            int[,] matrix = new int[,]
            {
            {0, 1, int.MaxValue},
            {int.MaxValue, 0, 1},
            {1, int.MaxValue, 0}
            };
            var pathAnalyzer = new GraphAnalyzer(matrix);

            // Act
            pathAnalyzer.FindMinimumWeightCycles();
            var cycles = GetPrivateField<List<CycleInfo>>(pathAnalyzer, "minimumCycles");

            // Verify we found at least one cycle
            Assert.IsTrue(cycles.Count > 0, "Should find at least one cycle");

            var firstCycle = cycles[0];

            // Print the actual path for debugging
            Console.WriteLine($"Found path: {string.Join("->", firstCycle.Path)}");
            Console.WriteLine($"Path length: {firstCycle.Path.Count}");
            Console.WriteLine($"Cycle weight: {firstCycle.Weight}");

            // Verify the path starts and ends with the same vertex
            Assert.AreEqual(
                firstCycle.Path[0],
                firstCycle.Path[firstCycle.Path.Count - 1],
                "Cycle should start and end at the same vertex"
            );

            // Verify all edges in path are valid (weight != int.MaxValue)
            for (int i = 0; i < firstCycle.Path.Count - 1; i++)
            {
                Assert.AreNotEqual(
                    int.MaxValue,
                    matrix[firstCycle.Path[i], firstCycle.Path[i + 1]],
                    $"Edge {firstCycle.Path[i]}->{firstCycle.Path[i + 1]} should be valid"
                );
            }

            // Verify total weight
            Assert.AreEqual(3, firstCycle.Weight, "Cycle should have total weight of 3");
        }

        /// <summary>
        /// Tests the case where minimum weight changes during exploration.
        /// Verifies that the algorithm updates minimum weight correctly when finding better cycles.
        /// </summary>
        [TestMethod]
        public void TestGraphAnalyzer_MinimumWeightUpdate_WorksCorrectly()
        {
            // Arrange
            int[,] weightChangeMatrix = new int[,]
            {
            {0, 5, 1},
            {1, 0, 5},
            {5, 1, 0}
            };
            var updateAnalyzer = new GraphAnalyzer(weightChangeMatrix);

            // Act
            updateAnalyzer.FindMinimumWeightCycles();
            var finalWeight = GetPrivateField<int>(updateAnalyzer, "minimumWeight");

            // Assert
            Assert.AreEqual(3, finalWeight, "Should find the cycle with weight 3 (1+1+1) instead of others");
        }

        /// <summary>
        /// Tests if the constructor properly handles null input by throwing an ArgumentNullException.
        /// </summary>
        [TestMethod]
        [ExpectedException(typeof(ArgumentNullException))]
        public void TestGraphAnalyzer_NullMatrix_ThrowsException()
        {
            // Act
            new GraphAnalyzer(null);
        }

        /// <summary>
        /// Tests if the algorithm correctly handles graphs with no valid cycles.
        /// Uses a matrix where no cycles are possible due to missing connections.
        /// </summary>
        [TestMethod]
        public void TestGraphAnalyzer_NoValidCycles_ReturnsZeroCycles()
        {
            // Arrange
            int[,] noCycleMatrix = new int[,]
            {
                {0, int.MaxValue},
                {int.MaxValue, 0}
            };
            var noCycleAnalyzer = new GraphAnalyzer(noCycleMatrix);

            // Act
            var result = noCycleAnalyzer.FindMinimumWeightCycles();

            // Assert
            Assert.AreEqual(0, GetPrivateField<List<CycleInfo>>(noCycleAnalyzer, "minimumCycles").Count);
        }

        /// <summary>
        /// Tests if the algorithm correctly handles negative weight cycles.
        /// Verifies that the minimum weight calculation works with negative numbers.
        /// </summary>
        [TestMethod]
        public void TestGraphAnalyzer_NegativeWeightCycle_FindsCorrectCycle()
        {
            // Arrange
            int[,] negativeMatrix = new int[,]
            {
                {0, -2},
                {-3, 0}
            };
            var negativeAnalyzer = new GraphAnalyzer(negativeMatrix);

            // Act
            var result = negativeAnalyzer.FindMinimumWeightCycles();

            // Assert
            Assert.AreEqual(-5, GetPrivateField<int>(negativeAnalyzer, "minimumWeight"));
        }

        /// <summary>
        /// Tests if the algorithm finds all cycles with equal minimum weight.
        /// Uses a matrix with multiple possible cycles of the same weight.
        /// </summary>
        [TestMethod]
        public void TestGraphAnalyzer_MultipleEqualWeightCycles_FindsAll()
        {
            // Arrange
            int[,] equalCyclesMatrix = new int[,]
            {
                {0, 1, int.MaxValue},
                {1, 0, 1},
                {int.MaxValue, 1, 0}
            };
            var equalCyclesAnalyzer = new GraphAnalyzer(equalCyclesMatrix);

            // Act
            var result = equalCyclesAnalyzer.FindMinimumWeightCycles();
            var cycles = GetPrivateField<List<CycleInfo>>(equalCyclesAnalyzer, "minimumCycles");

            // Assert
            Assert.IsTrue(cycles.Count > 1, "Should find multiple cycles with equal weights");
        }

        /// <summary>
        /// Helper method to access private fields for testing purposes.
        /// Uses reflection to access private members of the GraphAnalyzer class.
        /// </summary>
        /// <typeparam name="T">The type of the field to access</typeparam>
        /// <param name="instance">The object instance containing the field</param>
        /// <param name="fieldName">The name of the private field to access</param>
        /// <returns>The value of the private field</returns>
        private static T GetPrivateField<T>(object instance, string fieldName)
        {
            var field = instance.GetType().GetField(fieldName,
                System.Reflection.BindingFlags.NonPublic |
                System.Reflection.BindingFlags.Instance);
            return (T)field?.GetValue(instance);
        }
       
    }
}
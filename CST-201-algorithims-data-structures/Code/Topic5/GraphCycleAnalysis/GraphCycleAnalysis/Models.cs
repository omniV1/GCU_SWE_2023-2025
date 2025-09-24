namespace GraphCycleAnalysis
{
        /// <summary>
        /// Struct to track operation counts during graph analysis.
        /// Used to measure algorithm performance in terms of comparisons and data exchanges.
        /// </summary>
        public struct OperationCounts
        {
            /// <summary>
            /// Number of comparison operations performed during algorithm execution.
            /// This includes path existence checks, cycle detection, and weight comparisons.
            /// </summary>
            public int Comparisons;

            /// <summary>
            /// Number of data exchange operations performed during algorithm execution.
            /// This includes matrix accesses, path updates, and cycle storage operations.
            /// </summary>
            public int DataExchanges;

            /// <summary>
            /// Initializes a new instance of the OperationCounts struct with zero counts.
            /// </summary>
            public OperationCounts()
            {
                Comparisons = 0;
                DataExchanges = 0;
            }
        }

        /// <summary>
        /// Struct to store information about a cycle found in the graph.
        /// Includes both the path of vertices and the total weight of the cycle.
        /// </summary>
        public struct CycleInfo
        {
            /// <summary>
            /// List of vertices that form the cycle in order of traversal.
            /// The path starts and ends at the same vertex to form a complete cycle.
            /// </summary>
            public List<int> Path;

            /// <summary>
            /// Total weight of the cycle, calculated as the sum of weights of all edges in the cycle.
            /// Can be negative if the graph contains negative weight edges.
            /// </summary>
            public int Weight;

            /// <summary>
            /// Initializes a new instance of the CycleInfo struct.
            /// Creates an empty path and sets initial weight to 0.
            /// </summary>
            public CycleInfo()
            {
                Path = new List<int>();
                Weight = 0;
            }
        }
    }
 
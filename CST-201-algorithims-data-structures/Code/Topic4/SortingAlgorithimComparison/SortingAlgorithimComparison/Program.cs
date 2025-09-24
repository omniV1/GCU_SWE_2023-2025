//Owen Lindsey
// Professor Demland, David
// This work is my own
// CST-201 Compare sorting algos
// 11/03/2024

class Program
{
    // Define a structure to hold comparison and exchange counts for sorting algorithms
    public struct SortMetrics
    {
        // Track number of times elements are compared during sorting
        public long Comparisons;

        // Track number of times elements are swapped during sorting
        public long Exchanges;

        // Method to combine metrics from different sorting operations
        public void AddMetrics(SortMetrics otherMetrics)
        {
            // Add comparisons from another metrics instance
            Comparisons += otherMetrics.Comparisons;

            // Add exchanges from another metrics instance
            Exchanges += otherMetrics.Exchanges;
        }
    }

    static int Partition(int[] array, int lowIndex, int highIndex, out SortMetrics metrics)
    {
        // Initialize metrics structure
        metrics = new SortMetrics();

        // Select rightmost element as pivot
        int pivotValue = array[highIndex];

        // Index of smaller element
        int smallerElementIndex = lowIndex - 1;

        // Compare each element with pivot
        for (int currentIndex = lowIndex; currentIndex < highIndex; currentIndex++)
        {
            // Increment comparison counter
            metrics.Comparisons++;

            // If current element is smaller than pivot
            if (array[currentIndex] < pivotValue)
            {
                // Increment index of smaller element
                smallerElementIndex++;

                // Swap elements
                int tempValue = array[smallerElementIndex];
                array[smallerElementIndex] = array[currentIndex];
                array[currentIndex] = tempValue;
                metrics.Exchanges++;
            }
        }

        // Place pivot in its correct position
        int tempPivot = array[smallerElementIndex + 1];
        array[smallerElementIndex + 1] = array[highIndex];
        array[highIndex] = tempPivot;
        metrics.Exchanges++;

        // Return pivot's final position
        return smallerElementIndex + 1;
    }

    static SortMetrics QuickSort(int[] array, int startIndex, int endIndex)
    {
        // Initialize metrics structure
        SortMetrics metrics = new SortMetrics();

        // Check if there are at least 2 elements to sort
        if (startIndex < endIndex)
        {
            // Variable to store partition metrics
            SortMetrics partitionMetrics;

            // Partition array and get pivot index
            int pivotIndex = Partition(array, startIndex, endIndex, out partitionMetrics);

            // Recursively sort elements before and after partition
            SortMetrics leftPartitionMetrics = QuickSort(array, startIndex, pivotIndex - 1);
            SortMetrics rightPartitionMetrics = QuickSort(array, pivotIndex + 1, endIndex);

            // Combine all metrics from partitioning and recursive sorts
            metrics.Comparisons = partitionMetrics.Comparisons + leftPartitionMetrics.Comparisons + rightPartitionMetrics.Comparisons;
            metrics.Exchanges = partitionMetrics.Exchanges + leftPartitionMetrics.Exchanges + rightPartitionMetrics.Exchanges;
        }

        // Return combined metrics
        return metrics;
    }

    static SortMetrics MergeSort(int[] array, int startIndex, int endIndex)
    {
        // Initialize metrics structure
        SortMetrics metrics = new SortMetrics();

        // Check if there are at least 2 elements to sort
        if (startIndex < endIndex)
        {
            // Calculate middle point of array
            int middleIndex = startIndex + (endIndex - startIndex) / 2;

            // Recursively sort left half of array
            SortMetrics leftHalfMetrics = MergeSort(array, startIndex, middleIndex);

            // Recursively sort right half of array
            SortMetrics rightHalfMetrics = MergeSort(array, middleIndex + 1, endIndex);

            // Merge the sorted halves
            SortMetrics mergeMetrics = Merge(array, startIndex, middleIndex, endIndex);

            // Combine metrics from all operations
            metrics.Comparisons = leftHalfMetrics.Comparisons + rightHalfMetrics.Comparisons + mergeMetrics.Comparisons;
            metrics.Exchanges = leftHalfMetrics.Exchanges + rightHalfMetrics.Exchanges + mergeMetrics.Exchanges;
        }

        // Return combined metrics
        return metrics;
    }

    static SortMetrics Merge(int[] array, int startIndex, int middleIndex, int endIndex)
    {
        // Initialize metrics structure
        SortMetrics metrics = new SortMetrics();

        // Create temporary arrays for left and right portions
        int[] leftArray = new int[middleIndex - startIndex + 1];
        int[] rightArray = new int[endIndex - middleIndex];

        // Copy data to temporary arrays
        Array.Copy(array, startIndex, leftArray, 0, middleIndex - startIndex + 1);
        Array.Copy(array, middleIndex + 1, rightArray, 0, endIndex - middleIndex);

        // Initialize indices for merging
        int leftArrayIndex = 0;
        int rightArrayIndex = 0;
        int mergedArrayIndex = startIndex;

        // Merge arrays while elements exist in both
        while (leftArrayIndex < leftArray.Length && rightArrayIndex < rightArray.Length)
        {
            // Increment comparison counter
            metrics.Comparisons++;

            // Compare elements from both arrays
            if (leftArray[leftArrayIndex] <= rightArray[rightArrayIndex])
            {
                // Place element from left array
                array[mergedArrayIndex] = leftArray[leftArrayIndex];
                leftArrayIndex++;
            }
            else
            {
                // Place element from right array
                array[mergedArrayIndex] = rightArray[rightArrayIndex];
                rightArrayIndex++;
            }

            // Increment exchange counter
            metrics.Exchanges++;
            mergedArrayIndex++;
        }

        // Copy remaining elements of left array if any
        while (leftArrayIndex < leftArray.Length)
        {
            array[mergedArrayIndex] = leftArray[leftArrayIndex];
            leftArrayIndex++;
            mergedArrayIndex++;
            metrics.Exchanges++;
        }

        // Copy remaining elements of right array if any
        while (rightArrayIndex < rightArray.Length)
        {
            array[mergedArrayIndex] = rightArray[rightArrayIndex];
            rightArrayIndex++;
            mergedArrayIndex++;
            metrics.Exchanges++;
        }

        // Return metrics for merge operation
        return metrics;
    }

    static SortMetrics SelectionSort(int[] array)
    {
        // Initialize metrics structure to track comparisons and exchanges
        SortMetrics metrics = new SortMetrics();

        // Get array length for loop bounds
        int arrayLength = array.Length;

        // Outer loop - moves boundary of unsorted subarray
        for (int currentIndex = 0; currentIndex < arrayLength - 1; currentIndex++)
        {
            // Assume current position has minimum value
            int minimumValueIndex = currentIndex;

            // Inner loop - find minimum element in unsorted array
            for (int searchIndex = currentIndex + 1; searchIndex < arrayLength; searchIndex++)
            {
                // Increment comparison counter
                metrics.Comparisons++;

                // Check if current element is less than current minimum
                if (array[searchIndex] < array[minimumValueIndex])
                {
                    // Update minimum index if found
                    minimumValueIndex = searchIndex;
                }
            }

            // Only perform swap if minimum element isn't already in position
            if (minimumValueIndex != currentIndex)
            {
                // Store current element in temporary variable
                int temporaryValue = array[currentIndex];

                // Place minimum element in current position
                array[currentIndex] = array[minimumValueIndex];

                // Place stored element at minimum's original position
                array[minimumValueIndex] = temporaryValue;

                // Increment exchange counter
                metrics.Exchanges++;
            }
        }

        // Return metrics for this sorting operation
        return metrics;
    }

    static SortMetrics BubbleSort(int[] array)
    {
        // Initialize metrics structure to track comparisons and exchanges
        SortMetrics metrics = new SortMetrics();

        // Get array length for loop bounds
        int arrayLength = array.Length;

        // Outer loop - number of passes through array
        for (int passIndex = 0; passIndex < arrayLength - 1; passIndex++)
        {
            // Inner loop - compare adjacent elements
            for (int compareIndex = 0; compareIndex < arrayLength - passIndex - 1; compareIndex++)
            {
                // Increment comparison counter
                metrics.Comparisons++;

                // Compare adjacent elements
                if (array[compareIndex] > array[compareIndex + 1])
                {
                    // Store larger element in temporary variable
                    int temporaryValue = array[compareIndex];

                    // Move smaller element left
                    array[compareIndex] = array[compareIndex + 1];

                    // Place larger element right
                    array[compareIndex + 1] = temporaryValue;

                    // Increment exchange counter
                    metrics.Exchanges++;
                }
            }
        }

        // Return metrics for this sorting operation
        return metrics;
    }

    static void Shuffle(int[] array)
    {
        // Create new Random object for generating random numbers
        Random randomGenerator = new Random();

        // Loop through each element in the array
        for (int currentIndex = 0; currentIndex < array.Length; currentIndex++)
        {
            // Select a random position in the array
            int randomIndex = randomGenerator.Next(array.Length);

            // Store current element in temporary variable
            int temporaryValue = array[currentIndex];

            // Place random element at current position
            array[currentIndex] = array[randomIndex];

            // Place stored element at random position
            array[randomIndex] = temporaryValue;
        }
    }

    static void Main(string[] args)
    {
        // Display prompt for user input
        Console.WriteLine("Enter the size of array (n):");

        // Read and convert user input to integer
        int arraySize = int.Parse(Console.ReadLine());

        // Initialize metric tracking variables for each sorting algorithm
        SortMetrics selectionSortMetrics = new SortMetrics();
        SortMetrics bubbleSortMetrics = new SortMetrics();
        SortMetrics mergeSortMetrics = new SortMetrics();
        SortMetrics quickSortMetrics = new SortMetrics();

        // Begin loop for 100 trials as specified in requirements
        for (int trialNumber = 0; trialNumber < 100; trialNumber++)
        {
            // Create new array with numbers 1 to n using LINQ
            int[] originalArray = Enumerable.Range(1, arraySize).ToArray();

            // Randomize the array order
            Shuffle(originalArray);

            // Create copy of array and test Selection Sort
            int[] testArray = (int[])originalArray.Clone();
            selectionSortMetrics.AddMetrics(SelectionSort(testArray));

            // Create copy of array and test Bubble Sort
            testArray = (int[])originalArray.Clone();
            bubbleSortMetrics.AddMetrics(BubbleSort(testArray));

            // Create copy of array and test Merge Sort
            testArray = (int[])originalArray.Clone();
            mergeSortMetrics.AddMetrics(MergeSort(testArray, 0, testArray.Length - 1));

            // Create copy of array and test Quick Sort
            testArray = (int[])originalArray.Clone();
            quickSortMetrics.AddMetrics(QuickSort(testArray, 0, testArray.Length - 1));
        }

        // Print header for results section
        Console.WriteLine("\nResults averaged over 100 trials:");

        // Calculate and display average metrics for Selection Sort
        Console.WriteLine($"Selection Sort - Comparisons: {selectionSortMetrics.Comparisons / 100.0}, Exchanges: {selectionSortMetrics.Exchanges / 100.0}");

        // Calculate and display average metrics for Bubble Sort
        Console.WriteLine($"Bubble Sort    - Comparisons: {bubbleSortMetrics.Comparisons / 100.0}, Exchanges: {bubbleSortMetrics.Exchanges / 100.0}");

        // Calculate and display average metrics for Merge Sort
        Console.WriteLine($"Merge Sort     - Comparisons: {mergeSortMetrics.Comparisons / 100.0}, Exchanges: {mergeSortMetrics.Exchanges / 100.0}");

        // Calculate and display average metrics for Quick Sort
        Console.WriteLine($"Quick Sort     - Comparisons: {quickSortMetrics.Comparisons / 100.0}, Exchanges: {quickSortMetrics.Exchanges / 100.0}");
    }
}
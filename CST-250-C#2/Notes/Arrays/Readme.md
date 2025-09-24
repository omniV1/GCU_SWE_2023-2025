# 1. Declaring Arrays

In C#, you declare an array by specifying the data type, followed by a square brackets [], and the array name. 

```C# 
dataType arrayName; 
```

Example: 
```C#
int[] numbers; // Declare an integer an array
string[] names; // Declare a string array
```
The arrays are declared but not initialized. They have no memory allocated yet. 

# 2. Initializing Arrays
After declaring an array, you can initialize it by specifying the size *(number of elements)* or directly assinging values. 

### Option 1: Specify the Size
You allocate memory for the array by specifying its size. 
```C#
int[] numbers = new int[5]; // Array of 5 integers, all initialized to 0
```
### Option 2: Initialize with Values
You can directly assign values during initialization without specifying the size. 
```C#
int[] numbers = {1,2,3,4,5}; // Array of 5 integers
string[] names = {"Alice", "Bob", "Charlie"}; // array of strings
```
### Option 3: Initialize with Values Later
You can declare an array and set its values at different times.
```C#
int[] numbers = new int[3]; // array of 3 integers; 
numbers[0] = 10; 
numbers[1] = 20; 
numbers[2] = 30; 
```

# 3. Accessing Elements in an Array
You can access individual elements of an array using their index. *Arrays in C# are zero-based* ,Which means indexing starts at 0. 
### Example: 
```C#
int[] numbers = {10,20,30,40,50}; 
Console.WriteLine(numbers[0]); // Outputs: 10
Console.WriteLine(numbers[4]); // Outputs: 50
```
### Modifying Elements
you can change elements in the array by assinging new values. 
```C# 
numbers[1] = 25; // Changes the second element to 24
```
# 4. Iterating Through Arrays
To work with all elements in an array, you can use loops. 
### Using for loop: 
```C#
for (int i =0; i < numbers.length; i++)
{
    Console.WriteLine(numbers[i]; )
}
```
### using foreach loop
```C#
foreach (int num in numbers)
{
    Console.WriteLine(num); 
}
```
- *for* loop gives more control (you can modify the array), while *foreach* loop is simpler but doesnt allow modification of the array elements directly. 
  
# 5. Sorting Arrays
C# provides multiple ways to sort arrays, from built-in methods to manual sorting algorithims. 
### 5.1 Using Built-in Array.Sort()
The easiest way to sort an array is using the Array.Sort() method. This sorts the arry in ascending order. 
```C#
int[] numbers = {30,10,50,20,40}; 
Array.Sort(numbers); 

foreach (int num in numbers)
{
    Console.WriteLine(num+"") 
    // Output: 10,20,30,40,50.
}
```
### 5.2 Manual Sorting (Bubble sort)
Heres an example of sorting an array manually using Bubble Sort. 
```C#
int numbers = {30,10,50,20,40}; 

for (int i = 0; i < numbers.Length -1; i++)
{
    for(int j = 0; j < numbers.Length - i -1; j++){
        if (numbers[j] > numbers[j + 1])
        {
            // Swap
            int temp = numbers[j]
            numbers[j] = numbers[j + 1]; 
            numbers[j + 1] = temp; 
        }
    }

}
foreach (int num in numbers)
{
    Console.WriteLine(num + "") 
    // Output: 10,20,30,40,50
}
```
# 6. Multi-Dimensional Arrays
in C#, you can also declare multi-dimensional arrays such as 2D arrays. 
```C#
dataType[,] arrayName = new dataType[rows,columns]; 
```
### Example (2D Array)
```C#
int[,] matrix = new int[3,3]
{
    {1,2,3},
    {4,5,6},
    {7,8,9}, 
}; 
// Access elements 
Console.WriteLine(matrix{1,1}); // Output: 5

// Loop through a 2D array
for (int i =0; i < 3; i++)
{
    for (int j =0; j < 3; i++)
    {
        Console.WriteLine(matrix[i,j] + " ");
    }
    Console.WriteLine(); 
}
```
### Jagged Arrays
A jagged array is an array of arrays, where the inner arrays can have different lengths. 
```C#
int[][] jaggedArray = new int[3][];
jaggedArray[0] = new int[] { 1, 2 };
jaggedArray[1] = new int[] { 3, 4, 5 };
jaggedArray[2] = new int[] { 6 };

foreach (int[] arr in jaggedArray)
{
    foreach (int num in arr)
    {
        Console.Write(num + " ");
    }
    Console.WriteLine();
}
```
# 7. Array Methods
C# provides several useful methods for working with arrays
### 7.1 Array.copy()
you can copy an array or part of it to another array using Array.copy()
```C#
int[] source = { 1, 2, 3, 4, 5 };
int[] destination = new int[5];

Array.Copy(source, destination, 5);
```
### 7.2 Array.Reverse()
Reverses the elements of the array. 
```C#
Array.Reverse(numbers);  // Reverses the `numbers` array
```
### 7.3 Array.Resize()
you can resize an array dynamically using Array.Resize(). 
```C# 
int[] numbers = { 1, 2, 3 };
Array.Resize(ref numbers, 5);  // Resize the array to hold 5 elements
```
# 8. Common Pitfalls with Arrays
- Index Out of Range: Always ensure that when accessing or iterating over an array, you stay within the bounds *(0 to Length-1)* . 
- Fixed size: Once an array is initialized with a size, it cannot be resize(without using *Array.Resize()*), unlike other collection types like *List<T>*.

# 9. Array Alternatives
Sometimes, arrays are too rigid. In C#, *List<T>* is more flexible option. Its a dynamic arry-like collection that automatically resizes when needed. 
```C#
List<int> numbers = new List<int> { 10, 20, 30 };
numbers.Add(40);  // Add new element
numbers.Remove(20);  // Remove an element

foreach (int num in numbers)
{
    Console.Write(num + " ");
}
```
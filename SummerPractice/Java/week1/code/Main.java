package week1.code;

public class Main {
    public static void main(String[] args)
    {
     
        // Variables and data types 
        int number = 10; 
        double decimalNumber = 26.5;
        char letter = 'A';
        String message = "HI I AM OWEN";
        boolean isTrue = true; 

        // Output to the console
        System.out.println("Integer: " + number); 
        System.out.println("Double: " + decimalNumber); 
        System.out.println("Character: " + letter); 
        System.out.println("String: " + message); 
        System.out.println("Boolean: " + isTrue); 

        // Control structure
        if (number > 5) 
        {
            System.out.println("Number is greater than 5"); 
        } 
        else
        {
            System.out.println("Number is 5 or less");
        }
        for (int i = 0; i < 5; i++)
        {
           System.out.println("For Loop: " + i); 
           
        }
        int count = 0; 
        while (count < 5 ) 
        {
            System.out.println("While Loops: " + count); 
            count++; 
        }

        //Methods 
        printMessage("This is a custom method"); 

        // OOP Concepts

        Person person = new Person(); 
        person.setName("Owen Lindsey"); 
        person.setAge(26); 
        person.introduce(); 
    }
 
//Custom method to print a message
public static void printMessage(String msg)
{
    System.out.println(msg); 
}
}
class Person
{
 private String name; 
 private int age; 

 // Gettter for name 
 public String getName()
 {
    return name; 
 }
 
 // setter for name 
 public void setName(String name)
 {
    this.name = name;
 }
// Getter for age
public int getAge()
{
    return age; 
}
// Setter for age
public void setAge(int age)
{
    this.age = age;
}

// Method to introduce the person 
public void introduce()
{
    System.out.println("HI MY NAME IS " + name + " MY AGE IS " + age + " YEARS OLD"); 
}
}
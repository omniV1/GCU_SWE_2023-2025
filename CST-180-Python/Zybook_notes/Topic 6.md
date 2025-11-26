
# 6.1 Derived classes

A class will commonly share attributes with another class, but with some additions or variations. Ex: A store inventory system might use a class called Item, having name and quantity attributes. But for fruits and vegetables, a class Produce might have the attributes name, quantity, and expiration date. Note that Produce is really an Item with an additional feature, so ideally a program could define the Produce class as being the same as the Item class but with the addition of an expiration date attribute.

Such similarity among classes is supported by indicating that a class is derived from another class, as shown below.

![[Pasted image 20251120123255.png]]

The example defines a class named Item. In the script, an instance of Item is created called item1, the instance's attributes are set to Smith Cereal and 9, and the display() method is called. A class named Produce is also defined. That class was derived from the Item class by including the base class Item within parentheses after Produce, i.e., class Produce(Item):. As such, instantiating a Produce instance item2 creates an instance object with the data attributes name and quantity (from Item), plus expiration (from Produce), as well as with the methods set_name(), set_quantity(), and display() from Item, and set_expiration() and get_expiration() from Produce. In the script, item2 has instance data attributes set to Apples, 40, and May 5, 2012. The display() method is called, and then the expiration date is printed using the get_expiration() method.interfaces

All of the class attributes of Item are available to instances of Produce, though instance attributes are not. The __init__ method of Item must be explicitly called in the constructor of Produce, e.g., Item.__init__(self), so that the instance of Produce is assigned the name and quantity data attributes. When an instantiation of a Produce instance occurs, Produce.__init__() executes and immediately calls Item.__init__(). The newly created Produce instance is passed as the first argument (self) to the Item constructor, which creates the name and quantity attributes in the new Item instance's namespace. Item.__init__() returns, and Produce.__init__() continues, creating the expiration attribute. The following tool illustrates:

![[Pasted image 20251120123533.png]]


The term derived class refers to a class that inherits the class attributes of another class, known as a base class. Any class may serve as a base class; no changes to the definition of that class are required. The derived class is said to inherit the attributes of its base class, a concept called inheritance. An instance of a derived class type has access to all the attributes of the derived class as well as the class attributes of the base class by default, including the base class's methods. A derived class instance can simulate inheritance of instance attributes as well by calling the base class constructor manually. The following animation illustrates the relationship between a derived class and a base class.

![[Pasted image 20251120123640.png]]

Item is the base class.
Produce is derived so Produce inherits Item's attributes.

![[Pasted image 20251120123719.png]]

A class diagram depicts a class' name, data members, and methods.
A solid line with a closed, unfilled arrowhead indicates a class is derived from another class.
The derived class shows only additional members.

In the above animation, the +, -, and # symbols refer to the access level of an attribute, i.e., whether or not that attribute can be accessed by anyone (public), only instances of that class (private), or instances derived from that class (protected), respectively. In Python, all attributes are public.privacy. Many languages, such as Java, C, and C++, explicitly require setting access levels on every variable and function in a class, thus UML as a language-independent tool includes the symbols.

Various class derivation variations are possible:

A derived class can itself serve as a base class for another class. In the earlier example, "class Fruit(Produce):" could be added.
A class can serve as a base class for multiple derived classes. In the earlier example, "class Book(Item):" could be added.
A class may be derived from multiple classes. For example, "class House(Dwelling, Property):" could be defined.

# 6.2 Accessing base class attributes


A derived class can access the attributes of all of its base classes via normal attribute reference operations. For example, item1.set_name() might refer to the set_name method attribute of a class from which item1 is derived. An attribute reference is resolved using a search procedure that first checks the instance's namespace, then the classes' namespace, then the namespaces of any base classes.

The search for an attribute continues all the way up the inheritance tree, which is the hierarchy of classes from a derived class to the final base class. Ex: Consider the following class structure in which Motorcycle is derived from MotorVehicle, which is derived from TransportMode.

![[Pasted image 20251120130940.png]]

The above illustrates a program with three levels of inheritance. The scooter and dirt bike variables are instances of the Motorcycle class at the bottom of the inheritance tree. Calling the add_fuel() or drive() methods initiates a search, first in MotorCycle, and then in MotorVehicle. Calling the info() method defined at the top of the inheritance tree, as in scooter.info(), results in searching MotorCycle first, then MotorVehicle, and finally TransportMode.

# 6.3 Overriding class methods

A derived class may define a method having the same name as a method in the base class. Such a member function overrides the method of the base class. The following example shows the earlier Item/Produce example where the Produce class has its own display() method that overrides the display() method of the Item class.
![[Pasted image 20251120131056.png]]

When the derived class defines the method being overwritten, that method is placed in the class's namespace. Because attribute references search the inheritance tree by starting with the derived class and then recursively searching base classes, the method called will always be the method defined in the instance's class.

A programmer will often want to extend, rather than replace, the base class method. The base class method can be explicitly called at the start of the method, with the derived class then performing additional operations:
![[Pasted image 20251120131115.png]]


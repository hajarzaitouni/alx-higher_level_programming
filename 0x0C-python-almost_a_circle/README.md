# Python - Almost a circle
In this project, we have reviewed everything about Python:
* Import
* Exceptions
* Class
* Private attribute
* Getter/Setter
* Class method
* Static method
* Inheritance
* Unittest
* Read/Write file

Moreover, we also learned about:
* `args` and `kwargs`
* Serialization/Deserialization
* JSON

## Tasks
0. If it's not tested it doesn't work

1. Base class
* Write the first class `Base`
	* This class will be the “base” of all other classes in this project. 

2. First Rectangle
* Write the class `Rectangle` that inherits from `Base `

3. Validate attributes
* Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded)

4. Area first
* Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.

5. Display #0
* Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don’t need to handle `x` and `y` here.

6. __str__
* Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

7. Display #1
* Update the class Rectangle by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`

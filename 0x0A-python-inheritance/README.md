# Python - Inheritance
This project is about a new concept in __Python__ called Inheritance.

## General
In this project, we were ablte to:
* distinguish between a superclass, baseclass or parentclass.
* list all attributes and methods of a class or instance.
* Know how to inherit class from another.
* define a class with multiple base classes.
* Know ho to override a method or attribute inherited from the base class.
* Know which attributes or methods are available by heritage to subclasses
* Use `isinstance`, `issubclass`, `type` and `super` built-in functions.

## Tasks
0. Lookup
* Write a function that returns the list of available attributes and methods of an object:

	* Prototype: `def lookup(obj):`

1. My list
* Write a class `MyList` that inherits from `list`:

	* Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)

2. Exact same object
* Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

* Prototype: `def is_same_class(obj, a_class):`

3. Same class or inherit from
* Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

	* Prototype: `def is_kind_of_class(obj, a_class):`

4. Only sub class of
* Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

	* Prototype: `def inherits_from(obj, a_class):`

5. Geometry module
* Write an empty class BaseGeometry.

6. Improve Geometry
* Write a class `BaseGeometry` (based on `5-base_geometry.py`).

	* Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`

7. Integer validator
* Write a class `BaseGeometry` (based on `6-base_geometry.py`).

8. Rectangle
* Write a class `Rectangle` that inherits from BaseGeometry (`7-base_geometry.py`).

9. Full rectangle
* Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

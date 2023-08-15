# Python - Input/Output
This is new project about a new concept in __Python__ called Input/output.

## General:
In this particular project, we were able to:
* open a file.
* write text in a file.
* read the full content of a file.
* read a file line by line.
* use the `with` statement.
* convert a Python data structure to a JSON string.
* convert a JSON string to a Python data structure.

## Tasks:
0. Read file
* Write a function that reads a text file (`UTF8`) and prints it to stdout:

	* Prototype: `def read_file(filename=""):`

1. Write to a file
* Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

	* Prototype: `def write_file(filename="", text=""):`

2. Append to a file
* Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

	* Prototype: `def append_write(filename="", text=""):`

3. To JSON string
* Write a function that returns the JSON representation of an object (string):

	* Prototype: `def to_json_string(my_obj):`

4. From JSON string to Object
* Write a function that returns an object (Python data structure) represented by a JSON string:

	* Prototype: `def from_json_string(my_str):`

5. Save Object to a file
* Write a function that writes an Object to a text file, using a JSON representation:

	* Prototype: `def save_to_json_file(my_obj, filename):`

6. Create object from a JSON file
Write a function that creates an Object from a “JSON file”:

	* Prototype: `def load_from_json_file(filename):`

0x06. Python - Classes and Objects
***ALX Software Engineering Programme Tasks***

# Table of Contents

- [Project Description](#project-description)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Requirements](#requirements)
- [Files](#files)

# Project Description

This project focuses on Object-Oriented Programming (OOP) in Python, specifically on classes and objects. It covers topics such as class attributes, methods, properties, encapsulation, and more. The goal is to create a set of classes that define a square, allowing you to perform various operations on it.

# Learning Objectives

Upon completing this project, I should be able to:

- Understand the fundamentals of Object-Oriented Programming (OOP) in Python.
- Define and use classes and objects.
- Implement private attributes with getter and setter methods.
- Create class methods and instance methods.
- Practice good coding practices and proper documentation.

# Tasks

# 0. My first square

- Create an empty class `Square` that defines a square.

# 1. Square with size

- Expand the `Square` class to include a private instance attribute `size` and allow instantiation with a size value.

# 2. Size validation

- Add validation to the `Square` class to ensure that the size attribute is an integer and is not negative.

# 3. Area of a square

- Implement a method `area` within the `Square` class that calculates and returns the area of the square.

# 4. Access and update private attribute

- Enhance the `Square` class to use properties for getting and setting the size attribute. Implement additional validation in the setter method.

# 5. Printing a square

- Add a method `my_print` to the `Square` class, which prints the square using the `#` character.

# 6. Coordinates of a square

- Extend the `Square` class to include a private instance attribute `position`, which specifies the position of the square when printing.

# 7. Singly linked list (Advanced)

- Create a `Node` class to represent nodes in a singly linked list. Implement a singly linked list in the `SinglyLinkedList` class.

# 8. Print Square instance (Advanced)

- Update the `Square` class to display the square when the instance is printed.

# 9. Compare 2 squares (Advanced)

- Enhance the `Square` class to allow comparisons of squares based on their area.

# 10. ByteCode -> Python #5 (Advanced)

- Create a Python class `MagicClass` that behaves identically to a provided Python bytecode.

# Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use PEP 8 style (pycodestyle version 2.8.*)
- All your files must be executable

# Documentation

- All modules should have documentation. To check the module's documentation, run:
  
> python3 -c 'print(__import__("my_module").__doc__)'

All your classes should have documentation. To check a class's documentation, run:
 
> python3 -c 'print(__import__("my_module").MyClass.__doc__)'
All your functions (inside and outside a class) should have documentation. To check a function's documentation, run:
 
> python3 -c 'print(__import__("my_module").my_function.__doc__)'

and 

> python3 -c 'print(__import__("my_module").MyClass.my_function.


# Files
The following are the project files for the respective tasks:

0-square.py: Defines an empty class Square.
1-square.py: Adds a private instance attribute size and allows instantiation with size.
2-square.py: Validates the size attribute.
3-square.py: Adds a method area to calculate the area of the square.
4-square.py: Implements getter and setter methods for size.
5-square.py: Adds a my_print method to print the square using # characters.
6-square.py: Adds a private instance attribute position and updates the my_print method to consider the position.
100-singly_linked_list.py: Defines a singly linked list with a Node class and a SinglyLinkedList class.
101-square.py: Extends the Square class to display the square when printed.
102-square.py: Allows comparisons of squares based on their area.

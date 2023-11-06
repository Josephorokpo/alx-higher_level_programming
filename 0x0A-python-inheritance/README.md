# 0x0A. Python - Inheritance
***ALX Software Engineering Project***

#Project Description

The project focuses on the concept of inheritance in Python. It covers various aspects of inheritance, such as superclass, subclass, methods and attributes inheritance, and how to override methods and attributes inherited from base classes. It also explores the use of built-in functions like isinstance, issubclass, type, and super. The goal of this project is to deepen student's understanding of object-oriented programming in Python and the power of inheritance.

#Learning Objectives

The following will be well understood upon completing this project:

-Understand why Python programming is awesome.
- Define superclass, base class, and parent class.
- Define a subclass.
- List all attributes and methods of a class or instance.
- Know when an instance can have new attributes.
- Inherit a class from another.
- Define a class with multiple base classes.
- Understand the default class that every class inherits from.
- Override a method or attribute inherited from the base class.
- Recognize which attributes or methods are available to subclasses by inheritance.
- Understand the purpose of inheritance.
- Learn how and when to use isinstance, issubclass, type, and super built-in functions.

#Project Structure/Tasks

The project is divided into several tasks. Each task focuses on a specific aspect of inheritance and object-oriented programming. Here's an overview of the tasks:

Task 0. Lookup

Write a function that returns the list of available attributes and methods of an object:

- Prototype: def lookup(obj):
- Returns a list object
- You are not allowed to import any module

Task 1. My list

Write a class MyList that inherits from list:

- Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type int
- You are not allowed to import any module

Task 2. Exact same object

Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

- Prototype: def is_same_class(obj, a_class):
- You are not allowed to import any module

Task 3. Same class or inherit from

Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

- Prototype: def is_kind_of_class(obj, a_class):
- You are not allowed to import any module

Task 4. Only sub class of

Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

- Prototype: def inherits_from(obj, a_class):
- You are not allowed to import any module

Task 5. Geometry module

Write an empty class BaseGeometry.

- You are not allowed to import any module

Task 6. Improve Geometry

Write a class BaseGeometry (based on 5-base_geometry.py).

- Public instance method: def area(self): that raises an Exception with the message area() is not implemented
- You are not allowed to import any module

7. Integer validator

Write a class BaseGeometry (based on 6-base_geometry.py).

- Public instance method: def area(self): that raises an Exception with the message area() is not implemented
- Public instance method: def integer_validator(self, name, value): that validates value:
 - you can assume name is always a string
 - if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
 - if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
- You are not allowed to import any module

Task 8. Rectangle

Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

- Instantiation with width and height: def __init__(self, width, height):
- width and height must be private. No getter or setter
- width and height must be positive integers, validated by integer_validator

Task 9. Full rectangle

Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

- Instantiation with width and height: def __init__(self, width, height)::
 - width and height must be private. No getter or setter
 - width and height must be positive integers validated by integer_validator
- the area() method must be implemented
- print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>

Task 10. Square #1

Write a class Square that inherits from Rectangle (9-rectangle.py):

- Instantiation with size: def __init__(self, size)::
 - size must be private. No getter or setter
 - size must be a positive integer, validated by integer_validator
- the area() method must be implemented

Task 11. Square #2

Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

- Instantiation with size: def __init__(self, size)::
 - size must be private. No getter or setter
 - size must be a positive integer, validated by integer_validator
- the area() method must be implemented
- print() should print, and str() should return, the square description: [Square] <width>/<height>

12. My integer

Write a class MyInt that inherits from int:

- MyInt is a rebel. MyInt has == and != operators inverted
- You are not allowed to import any module

Task 13. Can I?

Write a function that adds a new attribute to an object if it’s possible:

- Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
- You are not allowed to use try/except
- You are not allowed to import any module

#Project Requirements
- Python scripts should be created.
- Allowed editors are vi, vim, and emacs.
- All files should end with a newline.
- The first line of all Python files should be exactly #!/usr/bin/python3.
- A README.md file must be provided at the root of the project folder.
- Code should follow the PEP 8 style guidelines, checked using pycodestyle (version 2.8.*).
- All files must be executable.
- The length of files will be tested using wc.
- Python test cases should be created, placed in a tests folder, and executed using the command python3 -m doctest ./tests/*.
- All modules, classes, and functions should include proper documentation in accordance with PEP 257.

#Usage
To run the provided Python scripts, execute them in your terminal. For example:

bash
Copy code
./0-main.py

To run the test cases, use the following command:

bash
Copy code
python3 -m doctest ./tests/*

# 0x08. Python - More Classes and Objects
***ALX Software Engineering Programme Tasks***

## Table of Contents

- [Project Details](#project-details)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)

# Project Details

- **Project Number**: 0x08
- **Project Title**: Python - More Classes and Objects
- **By**: Guillaume
- **Weight**: 1
- **Project Start Date**: Oct 30, 2023 6:00 AM
- **Project End Date**: Oct 31, 2023 6:00 AM
- **Checker Release Date**: Oct 30, 2023 12:00 PM
- **Auto Review**: Will be launched at the deadline

# Learning Objectives

After completing this project, learner should be able to:

- Understand the concept of Object-Oriented Programming (OOP) in Python.
- Define and use classes and objects.
- Work with attributes, including public, protected, and private attributes.
- Implement methods within classes, including special methods like `__init__`, `__str__`, and `__repr__`.
- Distinguish between class attributes and object attributes.
- Use class methods and static methods.
- Dynamically create arbitrary new attributes for existing instances of a class.
- Understand the Pythonic way to write getters and setters.
- Explain the difference between `__str__` and `__repr__`.
- Write class methods for creating instances or other class-specific functionality.
- Define the N queens problem and use backtracking to solve it.

# Requirements

- **General**:
  - Allowed editors: vi, vim, emacs
  - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
  - All your files should end with a new line.
  - The first line of all your files should be exactly `#!/usr/bin/python3`.
  - A `README.md` file, at the root of the project folder, is mandatory.
  - Your code should use `pycodestyle` (version 2.8.*) for code style checks.
  - All your files must be executable.
  - The length of your files will be tested using `wc`.

# Tasks

This project consists of multiple tasks related to object-oriented programming. The tasks are as follows:

0. **Simple Rectangle**
   - Create an empty class `Rectangle` that defines a rectangle.
 	- File: 0-rectangle.py

1. **Real Definition of a Rectangle**
   - Extend the `Rectangle` class to include width and height attributes with property getters and setters.
   - Implement instantiation with optional width and height.
	- File: 1-rectangle.py

2. **Area and Perimeter**
   - Add methods to the `Rectangle` class to calculate the area and perimeter of the rectangle.
   - Ensure that the perimeter is 0 if either width or height is 0.
	- File: 2-rectangle.py

3. **String Representation**
   - Implement the `__str__` and `__repr__` methods in the `Rectangle` class to represent the object as a string.
   - Print the rectangle using the `#` character.
	- File: 3-rectangle.py

4. **4. Eval is magic**
   - Write a class Rectangle that defines a rectangle
	- File: 4-rectangle.py

5. **Detect Instance Deletion**
   - Modify the `Rectangle` class to print "Bye rectangle..." when an instance is deleted.
   - Handle the case when an instance is deleted.
	- File: 5-rectangle.py

6. **How Many Instances**
   - Add a class attribute `number_of_instances` to keep track of the number of `Rectangle` instances.
   - Increment and decrement the count during instantiation and deletion.
	- File: 6-rectangle.py

7. **Change Representation**
   - Modify the `Rectangle` class to have a class attribute `print_symbol` for customizing the string representation character.
   - Update `__str__` method to use the `print_symbol`.
	- File: 7-rectangle.py
8. **Compare Rectangles**
   - Add a static method `bigger_or_equal` to the `Rectangle` class that compares two rectangles based on their areas.
	- File: 8-rectangle.py

9. **A Square is a Rectangle**
   - Implement a class method `square` that returns a new `Rectangle` instance with equal width and height.
	- File: 9-rectangle.py

10. **N Queens (Advanced)**
    - Create a Python program that solves the N queens puzzle for an N×N chessboard.
    - Use backtracking to find and print every possible solution to the problem.
	- File: 101-nqueens.py
 


# 0x07. Python - Test-driven development
***ALX Software Engineering Programme Project***

# Description
This project focuses on Test-Driven Development (TDD) in Python. The main objective is to write Python functions that perform various tasks while adhering to TDD principles. Each task involves writing functions and their associated test cases before implementing the actual code.

# Concepts
Key concepts covered in this project include:
- Test-Driven Development (TDD)
- Writing unit tests
- Using the `unittest` module
- Writing function documentation
- Handling edge cases
- Raising exceptions
- Numpy (for advanced tasks)

# Tasks

1. **Integers Addition**
   - Prototype: `def add_integer(a, b=98):`
   - Add two integers. Input values must be integers or floats, and they should be cast to integers if they are floats. Raises `TypeError` if the input types are invalid.

2. **Divide a Matrix**
   - Prototype: `def matrix_divided(matrix, div):`
   - Divide all elements of a matrix by a given number. The matrix must be a list of lists of integers or floats. Raises `TypeError` and `ValueError` for invalid inputs.

3. **Say My Name**
   - Prototype: `def say_my_name(first_name, last_name=""):`
   - Print "My name is <first name> <last name>". Raises `TypeError` for invalid inputs.

4. **Print Square**
   - Prototype: `def print_square(size):`
   - Print a square of "#" characters with the given size. Raises `TypeError` and `ValueError` for invalid inputs.

5. **Text Indentation**
   - Prototype: `def text_indentation(text):`
   - Print the input text with two new lines after each ".", "?", and ":". Raises `TypeError` for invalid inputs.

6. **Max Integer - Unittest**
   - Prototype: `def max_integer(list=[]):`
   - Write unit tests for the `max_integer` function. Uses the `unittest` module.

7. **Matrix Multiplication (Advanced)**
   - Prototype: `def matrix_mul(m_a, m_b):`
   - Multiply two matrices. Validates input matrices and raises exceptions for invalid inputs.

8. **Lazy Matrix Multiplication (Advanced)**
   - Prototype: `def lazy_matrix_mul(m_a, m_b):`
   - Multiply two matrices using the NumPy module. Raises appropriate exceptions for invalid inputs.

9. **CPython #3: Python Strings (Advanced)**
   - Prototype: `void print_python_string(PyObject *p);`
   - Print Python strings and their information using CPython. Demonstrates the interaction between Python and C.

# Requirements
- All Python scripts should be run using Python 3.8.5.
- Scripts must start with `#!/usr/bin/python3`.
- Code should follow PEP 8 style guidelines, and pycodestyle (2.8.*) should be used.
- A `README.md` file must be included.
- Test cases should be provided using the `unittest` module for relevant tasks.
- Tests should cover all possible edge cases and scenarios.

# How to Use
To run the functions, use the provided test scripts and examples in each task's description. For tasks involving CPython, you may need to compile and run the provided test files.


This project was part of the curriculum at ALX Software Engineering Programme

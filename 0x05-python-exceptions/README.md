# 0x05. Python - Exceptions
***ALX Software Engineering Programme Tasks***

# Description
This project focuses on understanding and working with exceptions in Python. I will learn how to handle errors and exceptions, raise custom exceptions, and create Python functions to safely perform operations.

# Learning Objectives
After completing this project, I should be able to explain the following concepts without the help of Google:

- The importance of Python programming
- The difference between errors and exceptions
- What exceptions are and how to use them
- When to use exceptions
- How to correctly handle exceptions
- The purpose of catching exceptions
- How to raise a built-in exception
- When to implement a clean-up action after an exception

# Requirements
- Allowed editors: vi, vim, emacs
- All code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All code files must end with a new line
- The first line of all code files must be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code must follow the PEP 8 style (use `pycodestyle` version 2.8.*)
- All code files must be executable
- The length of code files will be tested using the `wc` command

# Tasks

## 0. Safe list printing
Write a function that prints elements of a list.

- Prototype: `def safe_print_list(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- `x` represents the number of elements to print.
- `x` can be bigger than the length of `my_list`.
- Returns the real number of elements printed.
- You must use `try` and `except`.
- You are not allowed to import any modules.
- You are not allowed to use `len()`.

## 1. Safe printing of an integers list
Write a function that prints an integer with `"{:d}".format()`.

- Prototype: `def safe_print_integer(value):`
- `value` can be any type (integer, string, etc.).
- The integer should be printed followed by a new line.
- Returns `True` if `value` has been correctly printed (it means the value is an integer).
- Otherwise, returns `False`.
- You have to use `try` and `except`.
- You have to use `"{:d}".format()` to print as an integer.
- You are not allowed to import any modules.
- You are not allowed to use `type()`.

## 2. Print and count integers
Write a function that prints the first `x` elements of a list and only integers.

- Prototype: `def safe_print_list_integers(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.).
- All integers must be printed on the same line followed by a new line. Other types in the list must be skipped.
- `x` represents the number of elements to access in `my_list`.
- `x` can be bigger than the length of `my_list`. If it's the case, an exception is expected to occur.
- Returns the real number of integers printed.
- You have to use `try` and `except`.
- You have to use `"{:d}".format()` to print an integer.
- You are not allowed to import any modules.
- You are not allowed to use `len()`.

## 3. Integers division with debug
Write a function that divides two integers and prints the result.

- Prototype: `def safe_print_division(a, b):`
- You can assume that `a` and `b` are integers.
- The result of the division should be printed on the `finally:` section preceded by "Inside result:".
- Returns the value of the division, otherwise, `None`.
- You have to use `try`, `except`, and `finally`.
- You have to use `"{:}".format()` to print the result.
- You are not allowed to import any modules.

## 4. Divide a list
Write a function that divides element by element two lists.

- Prototype: `def list_division(my_list_1, my_list_2, list_length):`
- `my_list_1` and `my_list_2` can contain any type (integer, string, etc.).
- `list_length` can be bigger than the length of both lists.
- Returns a new list (length = `list_length`) with all divisions.
- If two elements can't be divided, the division result should be equal to 0.
- If an element is not an integer or float, print "wrong type".
- If the division can't be done (division by 0), print "division by 0".
- If `my_list_1` or `my_list_2` is too short, print "out of range".
- You have to use `try`, `except`, and `finally`.
- You are not allowed to import any modules.

## 5. Raise exception
Write a function that raises a type exception.

- Prototype: `def raise_exception():`
- You are not allowed to import any modules.

## 6. Raise a message
Write a function that raises a name exception with a message.

- Prototype: `def raise_exception_msg(message="")`
- You are not allowed to import any modules.

## 7. Safe integer print with error message (Advanced)
Write a function that prints an integer.

- Prototype: `def safe_print_integer_err(value):`
- `value` can be any type (integer, string, etc.).
- The integer should be printed followed by a new line.
- Returns `True` if `value` has been correctly printed (it means the value is an integer).
- Otherwise, returns `False` and prints in stderr the error preceded by "Exception:".
- You have to use `try` and `except`.
- You have to use `"{:d}".format()` to print as an integer.
- You are not allowed to use `type()`.

## 8. Safe function (Advanced)
Write a function that executes a function safely.

- Prototype: `def safe_function(fct, *args):`
- You can assume `fct` will be always a pointer to a function.
- Returns the result of the function.
- Otherwise, returns `None` if something happens during the function and prints in stderr the error preceded by "Exception:".
- You have to use `try` and `except`.

## 9. ByteCode -> Python #4 (Advanced)
Write the Python function `def magic_calculation(a, b):` that does exactly the same as the provided Python bytecode.

## 10. CPython #2: PyFloatObject (Advanced)
Create three C functions that print basic info about Python lists, Python bytes, and Python float objects. The information should include the size and the first few bytes of the object.

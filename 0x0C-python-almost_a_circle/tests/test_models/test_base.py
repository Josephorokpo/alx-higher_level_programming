import unittest
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBaseSaveToFile(unittest.TestCase):
    """
    Test cases for the save_to_file method of the Base class.
    """

    def setUp(self):
        """Create instances for testing."""
        self.rectangle1 = Rectangle(10, 5)
        self.rectangle2 = Rectangle(7, 3)
        self.square1 = Square(5)
        self.square2 = Square(2)

    def tearDown(self):
        """Remove test files created during testing."""
        for filename in ['Rectangle.json', 'Square.json']:
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_to_file_rectangle(self):
        """
        Test if save_to_file saves the JSON representation
        of a list of Rectangle objects to a file.
        """
        Rectangle.save_to_file([self.rectangle1, self.rectangle2])
        with open('Rectangle.json', 'r') as file:
            content = file.read()
        expected = '[{"id": 1, "width": 10, "height": 5, "x": 0, "y": 0}, {"id": 2, "width": 7, "height": 3, "x": 0, "y": 0}]'
        self.assertEqual(content, expected)

    def test_save_to_file_square(self):
        """
        Test if save_to_file saves the JSON representation of a list of
        Square objects to a file.
        """
        Square.save_to_file([self.square1, self.square2])
        with open('Square.json', 'r') as file:
            content = file.read()
        expected = '[{"id": 3, "size": 5, "x": 0, "y": 0}, {"id": 4, "size": 2, "x": 0, "y": 0}]'
        self.assertEqual(content, expected)

    def test_save_to_file_empty_list(self):
        """Test if save_to_file saves an empty list to a file."""
        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as file:
            content = file.read()
        self.assertEqual(content, '[]')

    def test_save_to_file_none(self):
        """
        Test if save_to_file saves an empty list to a file
        when list is None.
        """
        Square.save_to_file(None)
        with open('Square.json', 'r') as file:
            content = file.read()
        self.assertEqual(content, '[]')


if __name__ == '__main__':
    unittest.main()

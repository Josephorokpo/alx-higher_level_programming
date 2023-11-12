import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_constructor(self):
        """
        Test if the constructor sets the attributes correctly.
        """
        rectangle = Rectangle(10, 20, 5, 8, 1)

        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 8)
        self.assertEqual(rectangle.id, 1)

    def test_width_setter(self):
        """
        Test if the width setter works as expected.
        """
        rectangle = Rectangle(10, 20)

        rectangle.width = 30
        self.assertEqual(rectangle.width, 30)

        with self.assertRaises(TypeError):
            rectangle.width = "invalid_width"

        with self.assertRaises(ValueError):
            rectangle.width = 0

    def test_height_setter(self):
        """
        Test if the height setter works as expected.
        """
        rectangle = Rectangle(10, 20)

        rectangle.height = 25
        self.assertEqual(rectangle.height, 25)

        with self.assertRaises(TypeError):
            rectangle.height = "invalid_height"

        with self.assertRaises(ValueError):
            rectangle.height = -8

    def test_x_setter(self):
        """
        Test if the x setter works as expected.
        """
        rectangle = Rectangle(10, 20)

        rectangle.x = 15
        self.assertEqual(rectangle.x, 15)

        with self.assertRaises(TypeError):
            rectangle.x = "invalid_x"

        with self.assertRaises(ValueError):
            rectangle.x = -3

    def test_y_setter(self):
        """
        Test if the y setter works as expected.
        """
        rectangle = Rectangle(10, 20)

        rectangle.y = 12
        self.assertEqual(rectangle.y, 12)

        with self.assertRaises(TypeError):
            rectangle.y = "invalid_y"

        with self.assertRaises(ValueError):
            rectangle.y = -7

    def test_area_method(self):
        """
        Test if the area method returns the correct area.
        """
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.area(), 200)

        rectangle.width = 5
        rectangle.height = 8
        self.assertEqual(rectangle.area(), 40)

    def test_display_method(self):
        """
        Test if the display method prints the rectangle correctly
        with x and y.
        """
        rectangle = Rectangle(3, 4, 1, 2)

        # Redirect stdout to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        rectangle.display()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        expected_output = "\n\n ###\n ###\n ###\n ###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_method(self):
        """
        Test if the str method returns the correct string representation.
        """
        rectangle = Rectangle(10, 20, 5, 8, 1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 5/8 - 10/20")


if __name__ == '__main__':
    unittest.main()

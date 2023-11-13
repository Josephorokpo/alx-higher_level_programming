import unittest
from models.rectangle import Rectangle


class TestRectangleUpdateMethod(unittest.TestCase):
    """
    Test cases for the update method of the Rectangle class.
    """

    def test_update_method_no_args(self):
        """
        Test if update method does not modify attributes when
        no arguments are provided.
        """
        rectangle = Rectangle(10, 20, 5, 8, 1)
        rectangle.update()

        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 8)

    def test_update_method_with_args(self):
        """
        Test if update method correctly updates attributes
        with provided arguments.
        """
        rectangle = Rectangle(10, 20, 5, 8, 1)
        rectangle.update(2, 15, 25, 3, 4)

        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 25)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_update_method_partial_args(self):
        """
        Test if update method correctly updates attributes with
        partial arguments.
        """
        rectangle = Rectangle(10, 20, 5, 8, 1)
        rectangle.update(2, 15)

        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 8)

    def test_update_method_extra_args(self):
        """
        Test if update method ignores extra arguments beyond
        the fifth argument.
        """
        rectangle = Rectangle(10, 20, 5, 8, 1)
        rectangle.update(2, 15, 25, 3, 4, 99, "extra")

        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 25)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_update_method_keyword_args(self):
        """
        Test if update method correctly updates attributes with
        keyword arguments.
        """
        rectangle = Rectangle(10, 20, 5, 8, 1)
        rectangle.update(id=2, width=15, height=25, x=3, y=4)

        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 25)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)


if __name__ == '__main__':
    unittest.main()

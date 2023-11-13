import unittest
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of the Square class.
        """
        square = Square(5, 2, 3, 1)
        dictionary = square.to_dictionary()

        self.assertEqual(dictionary, {'id': 1, 'size': 5, 'x': 2, 'y': 3})

    def test_update_method_no_args(self):
        """
        Test if update method does not modify attributes when no
        arguments are provided.
        """
        square = Square(5, 2, 3, 1)
        square.update()

        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_method_with_args(self):
        """
        Test if update method correctly updates attributes
        with provided arguments.
        """
        square = Square(5, 2, 3, 1)
        square.update(2, 8, 4, 7)

        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 7)

    def test_update_method_partial_args(self):
        """
        Test if update method correctly updates attributes
        with partial arguments.
        """
        square = Square(5, 2, 3, 1)
        square.update(2, 8)

        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_update_method_extra_args(self):
        """
        Test if update method ignores extra arguments beyond
        the fourth argument.
        """
        square = Square(5, 2, 3, 1)
        square.update(2, 8, 4, 7, 99, "extra")

        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 7)


if __name__ == '__main__':
    unittest.main()

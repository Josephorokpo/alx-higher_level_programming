import unittest
from models.square import Square


class TestSquareUpdateMethod(unittest.TestCase):
    """
    Test cases for the update method of the Square class.
    """

    def test_update_method_no_args(self):
        """
        Test if update method does not modify attributes when
        no arguments are provided.
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
        square.update(2, 8, 4, 6)

        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 6)

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

    def test_update_method_keyword_args(self):
        """
        Test if update method correctly updates attributes
        with keyword arguments.
        """
        square = Square(5, 2, 3, 1)
        square.update(id=2, size=8, x=4, y=6)

        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 6)


if __name__ == '__main__':
    unittest.main()

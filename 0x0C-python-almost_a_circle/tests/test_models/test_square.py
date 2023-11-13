import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_constructor(self):
        """
        Test if the constructor sets the attributes correctly.
        """
        square = Square(5, 2, 3, 1)

        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_size_setter(self):
        """
        Test if the size setter works as expected.
        """
        square = Square(5, 2, 3, 1)

        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

        with self.assertRaises(TypeError):
            square.size = "invalid_size"

        with self.assertRaises(ValueError):
            square.size = 0

    def test_str_method(self):
        """
        Test if the str method returns the correct string representation.
        """
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")


if __name__ == '__main__':
    unittest.main()

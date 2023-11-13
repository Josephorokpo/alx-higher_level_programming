import unittest
from models.square import Square


class TestSquareSizeGetterSetter(unittest.TestCase):
    """
    Test cases for the size getter and setter of the Square class.
    """

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


if __name__ == '__main__':
    unittest.main()

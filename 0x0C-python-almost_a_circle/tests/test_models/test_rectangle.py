import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """
    Test cases for the Rectangle class methods.
    """

    def test_area(self):
        """
        Test the area method of the Rectangle class.
        """
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_display(self):
        """
        Test the display method of the Rectangle class.
        """
        rectangle = Rectangle(4, 3, 2, 1)
        expected_output = "\n" * 1 + " " * 2 + "####\n" * 3
        with self.assertLogs() as log:
            rectangle.display()
            self.assertEqual(log.output, [])
        self.assertEqual(log.output, [])
        self.assertEqual(expected_output, log.output)

    def test_str(self):
        """
        Test the __str__ method of the Rectangle class.
        """
        rectangle = Rectangle(4, 3, 2, 1, 99)
        self.assertEqual(str(rectangle), "[Rectangle] (99) 2/1 - 4/3")

    def test_update_method(self):
        """
        Test the update method of the Rectangle class.
        """
        rectangle = Rectangle(4, 3, 2, 1, 99)
        rectangle.update(1, 5, 5, 1, 0)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 1/0 - 5/5")

    def test_to_dictionary_method(self):
        """
        Test the to_dictionary method of the Rectangle class.
        """
        rectangle = Rectangle(4, 3, 2, 1, 99)
        expected_dict = {'id': 99, 'width': 4, 'height': 3, 'x': 2, 'y': 1}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()

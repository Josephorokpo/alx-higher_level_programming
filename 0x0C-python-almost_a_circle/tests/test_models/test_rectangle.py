import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    def test_area(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_display(self):
        rectangle = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_representation(self):
        rectangle = Rectangle(4, 8, 2, 3, 7)
        expected_str = "[Rectangle] (7) 2/3 - 4/8"
        self.assertEqual(str(rectangle), expected_str)

    def test_update_method_with_args(self):
        rectangle = Rectangle(10, 20, 5, 8, 1)
        rectangle.update(2, 15, 25, 3, 4)
        expected_str = "[Rectangle] (2) 3/4 - 15/25"
        self.assertEqual(str(rectangle), expected_str)

    def test_update_method_partial_args(self):
        rectangle = Rectangle(10, 20, 5, 8, 1)
        rectangle.update(2, 15)
        expected_str = "[Rectangle] (2) 5/8 - 15/20"
        self.assertEqual(str(rectangle), expected_str)

    def test_to_dictionary(self):
        rectangle = Rectangle(10, 20, 5, 8, 1)
        expected_dict = {'id': 1, 'width': 10, 'height': 20, 'x': 5, 'y': 8}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()

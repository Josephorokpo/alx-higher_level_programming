import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import io
import sys


class TestBaseMethods(unittest.TestCase):
    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(json_string, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_from_json_string(self):
        json_string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        list_dicts = Base.from_json_string(json_string)
        self.assertEqual(list_dicts, [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}])

    def test_create(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**dictionary)
        self.assertNotEqual(r1, r2)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertNotEqual(list_rectangles_input[0], list_rectangles_output[0])
        self.assertEqual(list_rectangles_input[0].to_dictionary(), list_rectangles_output[0].to_dictionary())

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '
                                      '{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]')

    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        with self.subTest():
            Base.draw([], [])
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_draw(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]
        list_squares = [Square(5), Square(7, 9, 1)]
        expected_output = "..."
        self.assert_stdout(expected_output)


if __name__ == "__main__":
    unittest.main()

import unittest
import json
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBaseMethods(unittest.TestCase):

    def test_to_json_string(self):
        # Test to_json_string with valid input
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        json_string = Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()])
        expected_result = json.dumps([r1.to_dictionary(), r2.to_dictionary()])
        self.assertEqual(json_string, expected_result)

        # Test to_json_string with None
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

        # Test to_json_string with empty list
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        # Test from_json_string with valid input
        json_string = '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' \
                      ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
        obj_list = Base.from_json_string(json_string)
        expected_result = [r.to_dictionary() for r in [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]]
        self.assertEqual(obj_list, expected_result)

        # Test from_json_string with None
        obj_list = Base.from_json_string(None)
        self.assertEqual(obj_list, [])

        # Test from_json_string with empty string
        obj_list = Base.from_json_string("")
        self.assertEqual(obj_list, [])

    def test_create(self):
        # Test create with valid input
        r1 = Rectangle(10, 7, 2, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)  # Different instances
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

        # Test create with invalid input
        with self.assertRaises(ValueError):
            Base.create(**{"invalid_key": 42})

    def test_load_from_file(self):
        # Test load_from_file with valid input
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        file_name = "Rectangle.json"
        Rectangle.save_to_file([r1, r2])
        obj_list = Rectangle.load_from_file()
        self.assertEqual(obj_list, [r1, r2])

        # Test load_from_file with non-existent file
        Square.load_from_file()  # This should not raise an exception

    def test_save_to_file(self):
        # Test save_to_file with valid input
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        file_name = "Rectangle.json"
        Rectangle.save_to_file([r1, r2])
        with open(file_name, "r") as file:
            file_content = file.read()
            expected_result = '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' \
                              ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
            self.assertEqual(file_content, expected_result)

        # Test save_to_file with None
        file_name = "Empty.json"
        Rectangle.save_to_file(None)
        with open(file_name, "r") as file:
            file_content = file.read()
            self.assertEqual(file_content, "[]")

        # Test save_to_file with empty list
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            file_content = file.read()
            self.assertEqual(file_content, "[]")


if __name__ == '__main__':
    unittest.main()

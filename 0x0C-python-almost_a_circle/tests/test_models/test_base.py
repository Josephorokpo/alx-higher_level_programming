import unittest
import json
from models.base import Base, Rectangle


class TestBaseSaveToFile(unittest.TestCase):

    def test_save_to_file(self):
        """Test save_to_file method."""
        # Create instances for testing
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]

        # Save instances to file
        Rectangle.save_to_file(list_rectangles)

        # Read from the file
        filename = "Rectangle.json"
        with open(filename, mode="r", encoding="utf-8") as file:
            content = file.read()

        # Convert content to list of dictionaries
        saved_data = json.loads(content)

        # Assert that the saved data is a list with correct length
        self.assertIsInstance(saved_data, list)
        self.assertEqual(len(saved_data), len(list_rectangles))

        # Assert that each dictionary in the list represents
        # the object correctly
        for saved_dict, obj in zip(saved_data, list_rectangles):
            expected_dict = obj.to_dictionary()
            self.assertDictEqual(saved_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()

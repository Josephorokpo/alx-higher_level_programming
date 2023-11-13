import unittest
from models.base import Base


class TestBaseToJsonString(unittest.TestCase):
    """
    Test cases for the to_json_string method of the Base class.
    """

    def test_to_json_string_empty_list(self):
        """Test if to_json_string returns '[]' for an empty list."""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        """Test if to_json_string returns '[]' for None."""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_single_dict(self):
        """
        Test if to_json_string converts a single dictionary
        to a JSON string.
        """
        test_list = [{'id': 1, 'name': 'Alice'}]
        result = Base.to_json_string(test_list)
        expected = '[{"id": 1, "name": "Alice"}]'
        self.assertEqual(result, expected)

    def test_to_json_string_multiple_dicts(self):
        """
        Test if to_json_string converts multiple dictionaries
        to a JSON string.
        """
        test_list = [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'}
        ]
        result = Base.to_json_string(test_list)
        expected = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

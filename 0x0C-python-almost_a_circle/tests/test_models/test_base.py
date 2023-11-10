import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_id_incrementation(self):
        """
        Test if the id attribute is incremented correctly.
        """
        obj1 = Base()
        obj2 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_id_assignment(self):
        """
        Test if the id attribute is assigned correctly when provided.
        """
        obj = Base(100)
        self.assertEqual(obj.id, 100)

    def test_id_type(self):
        """
        Test if the id attribute is an integer.
        """
        obj = Base()
        self.assertIsInstance(obj.id, int)

    def test_documentation(self):
        """
        Test if the documentation is present for the module, class, and method.
        """
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)


if __name__ == '__main__':
    unittest.main()

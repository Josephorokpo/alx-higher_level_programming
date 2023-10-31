import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function.
    """

    def test_empty_list(self):
        """
        Test with an empty list. The result should be None.
        """
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_at_beginning(self):
        """
        Test with the maximum value at the beginning of the list.
        """
        result = max_integer([99, 10, 42, 55])
        self.assertEqual(result, 99)

    def test_max_at_end(self):
        """
        Test with the maximum value at the end of the list.
        """
        result = max_integer([10, 42, 55, 99])
        self.assertEqual(result, 99)

    # Add similar docstrings for other test methods

if __name__ == '__main__':
    unittest.main()




Task 6
tests/100-matrix_mul.txt


import unittest
from matrix_mul import matrix_mul

class TestMatrixMul(unittest.TestCase):

    def test_valid_matrices(self):
        # Test with valid matrices
        m_a = [[1, 2], [3, 4]]
        m_b = [[5, 6], [7, 8]]
        result = matrix_mul(m_a, m_b)
        self.assertEqual(result, [[19, 22], [43, 50]])

    def test_empty_matrices(self):
        # Test with empty matrices
        m_a = []
        m_b = [[]]
        with self.assertRaises(ValueError):
            matrix_mul(m_a, m_b)

    def test_non_rectangle_matrices(self):
        # Test with non-rectangular matrices
        m_a = [[1, 2], [3, 4]]
        m_b = [[5, 6], [7, 8], [9, 10]]
        with self.assertRaises(ValueError):
            matrix_mul(m_a, m_b)

    def test_non_numeric_elements(self):
        # Test with non-numeric elements
        m_a = [[1, 2], [3, 'four']]
        m_b = [['five', 6], [7, 8]]
        with self.assertRaises(TypeError):
            matrix_mul(m_a, m_b)

    def test_multiplication_impossible(self):
        # Test when multiplication is impossible
        m_a = [[1, 2], [3, 4]]
        m_b = [[5, 6]]
        with self.assertRaises(ValueError):
            matrix_mul(m_a, m_b)

if __name__ == '__main__':
    unittest.main()

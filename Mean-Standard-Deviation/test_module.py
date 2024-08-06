import unittest
import numpy as np
from main import convert_to_2d_array, calculate_statistics

class TestMatrixFunctions(unittest.TestCase):
    def setUp(self):
        """Set up the test data."""
        self.flat_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rows = 3
        self.cols = 3

    def test_convert_to_2d_array(self):
        """Test the conversion of a flat list to a 2D array."""
        expected = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        result = convert_to_2d_array(self.flat_list, self.rows, self.cols)
        self.assertEqual(result, expected)
    
    def test_calculate_statistics(self):
        """Test the calculation of statistics."""
        expected = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        result = calculate_statistics(self.flat_list, self.rows, self.cols)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

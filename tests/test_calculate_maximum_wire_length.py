import unittest
import math
from src.calculate_maximum_wire_length import max_cable_length


class TestMaxCableLength(unittest.TestCase):

    def test_equal_heights(self):
        w = 2
        heights = [3, 3, 3]
        result = max_cable_length(w, heights)
        expected = 5.65  # sqrt((3-1)**2 + 2**2) + sqrt((3-1)**2 + 2**2) = 2 * sqrt(8) ≈ 5.65
        self.assertAlmostEqual(result, expected, delta=0.01, msg=f"Expected {expected}, but got {result}")

    def test_low_heights(self):
        w = 100
        heights = [1, 1, 1, 1]
        result = max_cable_length(w, heights)
        expected = 300.00  # Всі опори однакової висоти, максимальна довжина дорівнює сумі відстаней
        self.assertAlmostEqual(result, expected, delta=0.01, msg=f"Expected {expected}, but got {result}")

    def test_varied_heights(self):
        w = 4
        heights = [100, 2, 100, 2, 100]
        result = max_cable_length(w, heights)
        expected = 396.32  # Максимальна довжина для найгіршого випадку
        self.assertAlmostEqual(result, expected, delta=0.01, msg=f"Expected {expected}, but got {result}")


if __name__ == '__main__':
    unittest.main()

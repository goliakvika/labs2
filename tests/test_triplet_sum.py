import unittest
from src.triplet_sum import find_triplet_sum

class TestFindTripletSum(unittest.TestCase):
    def test_example(self):
        # Перевірка на прикладі
        arr = [1, 2, 3]
        target = 6
        self.assertEqual(find_triplet_sum(arr, target), True)

    def test_negative_example(self):
        # Перевірка на прикладі, коли таких чисел немає
        arr = [1, 2, 3]
        target = 10
        self.assertEqual(find_triplet_sum(arr, target), False)

if __name__ == "__main__":
    unittest.main()

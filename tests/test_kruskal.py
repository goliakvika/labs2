import unittest
from src.kruskal import find_min_len_cable_in_the_island

class KruskalAlgorithmTest(unittest.TestCase):
    def test_empty_graph(self):
        find_min_len_cable_in_the_island("C:\\Users\\ViGo\\PycharmProjects\\pythonProject\\labs2p\\src\\islands_empty.csv",
                                         "C:\\Users\\ViGo\\PycharmProjects\\pythonProject\\labs2p\\src\\islands_empty.out")
        with open("C:\\Users\\ViGo\\PycharmProjects\\pythonProject\\labs2p\\src\\islands_empty.out", 'r') as file:
            first_line = file.readline().strip()
        self.assertEqual(first_line, "Graph is empty")

    def test_normal_graph(self):
        find_min_len_cable_in_the_island("C:\\Users\\ViGo\\PycharmProjects\\pythonProject\\labs2p\\src\\islands.csv",
                                         "C:\\Users\\ViGo\\PycharmProjects\\pythonProject\\labs2p\\src\\islands.out")
        with open("C:\\Users\\ViGo\\PycharmProjects\\pythonProject\\labs2p\\src\\islands.out", 'r') as file:
            first_line = file.readline().strip()
        self.assertEqual(int(first_line), 19)

if __name__ == '__main__':
    unittest.main()


import unittest
from src.get_documents import get_order



class TestGetOrder(unittest.TestCase):

    def test_example1(self):
        dependencies = [
            "a b",
            "b c",
            "c d",
            "d e"
        ]
        expected_order = [
            "e",
            "d",
            "c",
            "b",
            "a"
        ]
        self.assertEqual(get_order(dependencies), expected_order)

    def test_example2(self):
        dependencies = [
            "visa foreignpassport"
        ]
        expected_order = [
            "foreignpassport",
            "visa"
        ]
        self.assertEqual(get_order(dependencies), expected_order)

    def test_single_dependency(self):
        dependencies = [
            "b a"
        ]
        expected_order = [
            "a",
            "b"
        ]
        self.assertEqual(get_order(dependencies), expected_order)

if __name__ == '__main__':
    unittest.main()






# Приклад 1
dependencies1 = [
    "visa foreignpassport",
    "visa hotel",
    "visa bankstatement",
    "bankstatement nationalpassport",
    "hotel creditcard",
    "creditcard nationalpassport",
    "nationalpassport birthcertificate",
    "foreignpassport nationalpassport",
    "foreignpassport militarycertificate",
    "militarycertificate nationalpassport"
]
result1 = get_order(dependencies1)
print('\n'.join(result1))

# Приклад 2
dependencies2 = [
    "visa foreignpassport"
]
result2 = get_order(dependencies2)
print('\n'.join(result2))

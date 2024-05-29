import unittest
from src.branch_sums import BinaryTree, branchSums


class TestBranchSums(unittest.TestCase):
    def test_branch_sums(self):
        # Створюємо дерево
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)

        # Очікуємо, що сума лівих листів буде 24
        self.assertEqual(branchSums(root), 24)

        # Додатковий тест на пусте дерево
        self.assertEqual(branchSums(None), 0)

if __name__ == '__main__':
    unittest.main()

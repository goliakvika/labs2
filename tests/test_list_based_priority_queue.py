import unittest
from src.list_based_priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def test_insert(self):
        pq = PriorityQueue()
        pq.insert("Task 1", 2)
        pq.insert("Task 2", 1)
        pq.insert("Task 3", 3)
        self.assertEqual(pq.peek(), "Task 3")

    def test_peek_empty_queue(self):
        pq = PriorityQueue()
        self.assertIsNone(pq.peek())

    def test_remove_highest_priority(self):
        pq = PriorityQueue()
        pq.insert("Task 1", 2)
        pq.insert("Task 2", 1)
        pq.insert("Task 3", 3)
        self.assertEqual(pq.remove_highest_priority(), "Task 3")




pq = PriorityQueue()
pq.insert("Task 1", 3)
pq.insert("Task 2", 1)
pq.insert("Task 3", 2)

print("Highest Priority Task:", pq.peek())

task_completed = pq.remove_highest_priority()
print("Completed Task:", task_completed)

print("New Highest Priority Task:", pq.peek())



if __name__ == '__main__':
    unittest.main()

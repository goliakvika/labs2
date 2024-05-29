class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_before(self, node, new_node):
        new_node.next = node
        new_node.prev = node.prev
        if node.prev:
            node.prev.next = new_node
        node.prev = new_node
        if node == self.head:
            self.head = new_node

    def insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        if node.next:
            node.next.prev = new_node
        node.next = new_node
        if node == self.tail:
            self.tail = new_node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

class PriorityQueue:
    def __init__(self):
        self.list = DoublyLinkedList()

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if not self.list.head:
            self.list.head = new_node
            self.list.tail = new_node
        elif priority > self.list.head.priority:
            self.list.insert_before(self.list.head, new_node)
        else:
            current = self.list.head
            while current.next and priority <= current.next.priority:
                current = current.next
            self.list.insert_after(current, new_node)

    def remove_highest_priority(self):
        if not self.list.head:
            return None
        highest_priority = self.list.head
        self.list.head = self.list.head.next
        if self.list.head:
            self.list.head.prev = None
        return highest_priority.value

    def peek(self):
        if self.list.head:
            return self.list.head.value
        else:
            return None


import unittest
from src import queue


class TestQueue(unittest.TestCase):
    def test_init_node(self):
        node_new = queue.Node(5)
        self.assertEquals(node_new.data, 5)
        node_new1 = queue.Node("abc")
        self.assertEquals(node_new1.data, "abc")
        self.assertEquals(node_new1.next_node, None)

    def test_init_queue(self):
        queue_new = queue.Queue()
        self.assertEquals(queue_new.head, None)
        self.assertEquals(queue_new.tail, None)
        self.assertEquals(queue_new.size, 0)

    def test_enqueue(self):
        queue_new = queue.Queue()
        queue_new.enqueue("data1")
        self.assertEquals(queue_new.head.data, "data1")
        self.assertEquals(queue_new.tail.data, "data1")
        self.assertEquals(queue_new.size, 1)
        queue_new.enqueue("data2")
        self.assertEquals(queue_new.head.data, "data1")
        self.assertEquals(queue_new.tail.data, "data2")
        self.assertEquals(queue_new.size, 2)

    def test_dequeue(self):
        queue_new = queue.Queue()

        queue_new.enqueue('data1')
        queue_new.enqueue('data2')
        queue_new.enqueue('data3')

        self.assertEquals(queue_new.dequeue(),'data1')
        self.assertEquals(queue_new.dequeue(), 'data2')
        self.assertEquals(queue_new.dequeue(), 'data3')
        self.assertEquals(queue_new.dequeue(), None)


    def test_str(self):
        queue_new = queue.Queue()
        queue_new.enqueue("data1")
        queue_new.enqueue("data2")
        self.assertEquals(str(queue_new), "data1\ndata2")

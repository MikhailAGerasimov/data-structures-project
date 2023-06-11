
import unittest
from src import stack


class TestStack(unittest.TestCase):
    def test_init_node(self):
        node_new = stack.Node(5)
        self.assertEquals(node_new.data, 5)
        node_new1 = stack.Node("abc")
        self.assertEquals(node_new1.data, "abc")
        self.assertEquals(node_new1.next_node, None)

    def test_init_stack(self):
        stack_new = stack.Stack()
        self.assertEquals(stack_new.top, None)
        self.assertEquals(stack_new.size, 0)

    def test_push(self):
        stack_new = stack.Stack()
        stack_new.push("lor")
        self.assertEquals(stack_new.size, 1)
        self.assertEquals(stack_new.top.data, "lor")
        stack_new.push(5)
        self.assertEquals(stack_new.size, 2)
        self.assertEquals(stack_new.top.data, 5)
        self.assertEquals(stack_new.top.next_node.data, "lor")


    def test_pop(self):
        stack_new = stack.Stack()
        data = stack_new.pop()
        self.assertEquals(data, None)
        stack_new.push("lor")
        stack_new.push(5)
        data1 = stack_new.pop()
        self.assertEquals(data1, 5)
        self.assertEquals(stack_new.top.data, "lor")


    def test_str(self):
        stack_new = stack.Stack()
        stack_new.push("lor")
        stack_new.push(5)
        self.assertEquals(str(stack_new), "5\nlor")
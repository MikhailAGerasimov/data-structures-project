"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src import linked_list

class TestLL(unittest.TestCase):
    def test_init_node(self):
        node_new = linked_list.Node(5)
        self.assertEquals(node_new.data, 5)
        node_new1 = linked_list.Node("abc")
        self.assertEquals(node_new1.data, "abc")
        self.assertEquals(node_new1.next_node, None)

    def test_init_ll(self):
        ll_new = linked_list.LinkedList()
        self.assertEquals(str(ll_new), "None")
        self.assertEquals(ll_new.head, None)
        self.assertEquals(ll_new.tail, None)
        self.assertEquals(ll_new.size, 0)

    def test_add_ll(self):
        ll_new = linked_list.LinkedList()
        ll_new.insert_beginning({'id': 1})
        ll_new.insert_at_end({'id': 2})
        ll_new.insert_at_end({'id': 3})
        ll_new.insert_beginning({'id': 0})
        self.assertEquals(ll_new.head.data, {'id': 0})
        self.assertEquals(ll_new.tail.data, {'id': 3})
        self.assertEquals(ll_new.size, 4)
        self.assertEquals(str(ll_new), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_to_list(self):
        ll_new = linked_list.LinkedList()
        data_list = ll_new.to_list()
        self.assertEquals(data_list,[])

        ll_new.insert_beginning({'id': 1})
        ll_new.insert_at_end({'id': 2})
        ll_new.insert_at_end({'id': 3})
        ll_new.insert_beginning({'id': 0})
        data_list = ll_new.to_list()
        self.assertEquals(data_list[0], {'id': 0})
        self.assertEquals(data_list[3], {'id': 3})

    def test_get_data_by_id(self):
        ll_new = linked_list.LinkedList()
        data  = ll_new.get_data_by_id(3)
        self.assertEquals(data, {})

        ll_new.insert_beginning({'id': 1})
        ll_new.insert_at_end({'id': 2})
        ll_new.insert_at_end({'id': 3})
        ll_new.insert_beginning({'id': 0})
        data = ll_new.get_data_by_id(3)
        self.assertEquals(data, {'id': 3})

        data = ll_new.get_data_by_id(5)
        self.assertEquals(data, {})

        ll = linked_list.LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

        self.assertRaises(TypeError, ll.get_data_by_id(2))

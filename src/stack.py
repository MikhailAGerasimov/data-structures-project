class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None
        self.size = 0

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data)
        if self.top:
            new_node.next_node = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.size == 0:
            return None
        else:
            del_elem = self.top.data
            self.top = self.top.next_node
            self.size -= 1
            return del_elem

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = ''
        node = self.top
        for i in range(self.size):
            result += str(node.data)
            result += "\n"
            node = node.next_node
        return result[:-1]
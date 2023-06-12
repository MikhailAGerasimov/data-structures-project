class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size = 1
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.size += 1

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.size == 0:
            return None

        data1 = self.head.data
        self.head = self.head.next_node
        self.size -= 1
        return data1

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = ''
        node = self.head
        for i in range(self.size):
            result += str(node.data)
            result += "\n"
            node = node.next_node
        return result[:-1]

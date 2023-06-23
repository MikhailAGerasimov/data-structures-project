class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size = 1
        else:
            temp_node = self.head
            self.head = new_node
            self.head.next_node = temp_node
            self.size += 1

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size = 1
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.size += 1

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string[1:]

    def to_list(self):
        """Возвращает список с данными, содержащимися в односвязном списке `LinkedList`"""
        data_list = []
        node = self.head
        if node is None:
            return data_list
        while node:
            data_list.append(node.data)
            node = node.next_node
        return data_list

    def get_data_by_id(self, data):
        """возвращает первый найденный в `LinkedList` словарь с ключом 'id',
            значение которого равно переданному в метод значению."""
        node = self.head
        if node is None:
            return {}
        while node:
            try:
                if node.data['id'] == data:
                    return node.data
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")
            node = node.next_node
        return {}

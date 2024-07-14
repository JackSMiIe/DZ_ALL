class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Добавить узел в конец списка
    def add_in_tail(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    # Вывести на экран все узлы
    def print_all_nodes(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()

    # Найти узел по значению (первое совпадение)
    def find(self, val):
        current = self.head
        while current is not None:
            if current.value == val:
                return current
            current = current.next
        return None

    # Найти все узлы с переданным значением
    def find_all(self, val):
        found_nodes = []
        current = self.head
        while current is not None:
            if current.value == val:
                found_nodes.append(current)
            current = current.next
        return found_nodes

    # Удалить узел с переданным значением.
    # Если all=False, то учитывается первое совпадение. Иначе удаляются все узлы с данным значением.
    def delete(self, val, all=False):
        current = self.head
        prev = None
        while current is not None:
            if current.value == val:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                if current == self.tail:
                    self.tail = prev
                if not all:
                    return
            else:
                prev = current
            current = current.next

    # Очистить весь список
    def clean(self):
        self.head = None
        self.tail = None

    # Вернуть количество узлов в списке
    def len(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # Вставить узел после указанного
    def insert(self, afterNode, newNode):
        if afterNode is None:
            return
        new_node = Node(newNode)
        current = self.head
        while current is not None:
            if current == afterNode:
                new_node.next = current.next
                current.next = new_node
                if current == self.tail:
                    self.tail = new_node
                return
            current = current.next


linked_list = LinkedList()
linked_list.add_in_tail(1)
linked_list.add_in_tail(2)
linked_list.add_in_tail(3)
linked_list.add_in_tail(2)
linked_list.add_in_tail(4)

print("Все узлы:")
linked_list.print_all_nodes()
print("Длина списка:", linked_list.len())
linked_list.delete(2)
print("Узлы после удаления первого вхождения 2:")
linked_list.print_all_nodes()
linked_list.delete(2, all=True)
print("Узлы после удаления всех вхождений 2:")
linked_list.print_all_nodes()

linked_list.clean()
print("После очистки списка:")
linked_list.print_all_nodes()


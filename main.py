class Node:

    def __init__(self,data):
        self.data = data
        self.next_node = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_start(self,data):

        self.num_of_nodes = self.num_of_nodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        else:
            new_node.next_node= self.head
            self.head = new_node

    def insert_end(self,data):

        self.num_of_nodes = self.num_of_nodes +1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    def size_of_list(self):

        return self.num_of_nodes

    def traverse(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    def remove(self,data):

        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data !=data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node



if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.insert_start(1)
    linked_list.insert_start(2)
    linked_list.insert_end(3)

    linked_list.traverse()

    linked_list.remove(2)
    linked_list.traverse()

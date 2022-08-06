

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """
        Add node at the front.
        Following are the 4 steps to add a node at the front.
        """

        # 1 & 2: Allocate the Node &
        #        Put in the data
        first = Node(new_data)

        # 3. Make next of new Node as head
        first.next = self.head
        # 4. Move the head to point to new Node
        self.head = first

    def insertAfter(self, prev_node, new_data):
        """
        This function will inserts in between like after previous node.
        """
        if prev_node is None:
            print("Node should present in given list")
            return
        # First creates new node
        new_node = Node(new_data)

        # assign previous node next to current node

        new_node.next = prev_node.next

        # Assign prev node next to new node

        prev_node.next = new_node

    def append(self, new_data):
        """
        This will append data at the end.
        """
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(12)
    second = Node(45)
    third = Node(21)
    llist.head.next = second
    second.next = third
    llist.printList()
    llist.push(69)
    llist.push(369)
    print("Linked List after adding new elements at Front")
    llist.printList()
    print("Inserts after specific position")
    llist.insertAfter(second, 99)
    llist.printList()
    llist.append(87)
    llist.printList()

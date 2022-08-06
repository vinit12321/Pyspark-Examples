class Node:
    """
    Node class which uses to describe the Node data with value.
    It will have two attributes like data and next pointer value.
    """

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkdeList:
    """
    Main class will have head and other functions
    """

    def __init__(self) -> None:
        self.head = None

    def printList(self):
        temp = self.head
        print("Printing Linked List")
        while(temp):
            print(temp.data)
            temp = temp.next

    def insert_after(self, data, node_after):
        if node_after is None:
            return

        new_node = Node(data)
        new_node.next = node_after.next

        # assign next node to
        node_after.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def delete_node(self, key):
        temp = self.head

        # First condition is that if your node is head node that you want to delete.
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return

        # traverse the entire linkded list & try to compare node value withhin linked list.
        while(temp is not None):  # checking that temp is not none means last node of linkded list
            if(temp.data == key):
                break  # if its found need to break the loop
            # Tracking previous node in prev variable so that if we found next element to be deleted then we can easily delete those records.
            prev = temp

            temp = temp.next  # Just Iterating the linkde list.

        # if we you wont find any elements in the linked list then delete then return nothing.
        if temp == None:
            return

        # Take previous element where you broke up the code and assign next element to be next element of temp.
        prev.next = temp.next
        temp = None  # at last assign temp to None.


if __name__ == '__main__':
    l1 = LinkdeList()
    l1.head = Node(10)
    second = Node(12)
    third = Node(16)
    l1.head.next = second

    second.next = third
    l1.printList()
    l1.append(69)
    l1.printList()
    l1.delete_node(10)
    l1.printList()

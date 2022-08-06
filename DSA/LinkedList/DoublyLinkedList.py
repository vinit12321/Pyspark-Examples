from dataclasses import dataclass
from unittest.mock import NonCallableMagicMock

from nbformat import current_nbformat


class Node:
    """
    Doubly Linked List have data,Previous node & next node which it should point.
    """
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.prev=None

    
class DoublyLinkedList:
    """
    Doubly Linked List have head & Fornt end i.e start_node & rear node i.e. end_node.
    Using this node,we can add values fron start & end.
    """
    def __init__(self) -> None:
        self.head=None
        self.start_node=None
        self.end_node=None
    

    def append(self,data):
        """
        This function is used to append the data in the doubly linked list.
        """
        if self.end_node is None:    #If its first element in the doubly linked list then end node would be none
            
            self.head=Node(data)     #Creating the new node.
            self.end_node=self.head  #As its first element in the node so would need to assign end node as head.
        else:
            new_node=Node(data)
            self.end_node.next=new_node  # First assigning end node's next element to as new node.
            new_node.prev=self.end_node  # then previpus node is setting it to end node.
            new_node.next=None    #next node of new node is setting as None.
            self.end_node=new_node  #finally end node i.e last node of linked list we are setting as new node.

    
    def display(self,Type="None"):
        if Type=='Left_To_Right':
            print("Printing Dobouly Linked List from left to right")
            current=self.head
            while(current is not None):
                print(current.data)
                current=current.next
        else:
            print("Printing Dobouly Linked List from the Last")
            current=self.end_node
            while(current is not None):
                print(current.data)
                current=current.prev
    


if __name__=='__main__':
    dl=DoublyLinkedList()
    dl.append(1)
    dl.append(3)
    dl.append(4)
    dl.display("Left_To_Right")
    dl.display()

"""

Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a contiguous location; 
the elements are linked using pointers. They includes a series of connected nodes.
Here, each node stores the data and the address of the next node.
"""

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
    
#Linkdean Class
class LinkedList:

    def __init__(self) -> None:
        self.head=None

    
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    


if __name__=='__main__':
    llist=LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(69)
    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''
    llist.head.next=second
    '''
    Now next of first Node refers to second.  So they
    both are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''
    second.next=third
    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''
    llist.printList()

"""
Time Complexity 
Time Complexity	Worst Case	Average Case
Search	O(n)	O(n)
Insert	O(1)	O(1)
Deletion	O(1)	O(1)
Auxiliary Space:  O(n)


"""
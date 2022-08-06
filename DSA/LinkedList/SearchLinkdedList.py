class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
    

class LinkdedList:
    def __init__(self) -> None:
        self.head=None
    

    def push(self,data):
        
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def printList(self):
        temp=self.head
        while(temp):
            print("Data is {}".format(temp.data))

            temp=temp.next
    

    def search(self,key):
        """
        Function is defined to search element in the linkded list.
    
        """
        temp=self.head
        while(temp):
            if(temp.data==key):
                return True
            temp=temp.next
        return False
    

    def getNth(self,index):
        temp=self.head
        count=0
        while(temp):
            if count==index:
                return temp.data
            count+=1
            temp=temp.next
        assert(False)
        return 0

 
if __name__=='__main__':
    li=LinkdedList()
    li.push(10)
    li.push(20)
    li.push(30)
    li.printList()
    
    print("Data is {} in the Linkded List".format("Present" if li.search(30) else "Not Present"))


    print(li.getNth(1))
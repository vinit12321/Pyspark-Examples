class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkdedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def getCount(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            print(temp.data)
            temp = temp.next

        print("Total Count is "+str(count))


if __name__ == '__main__':
    lis = LinkdedList()
    lis.push(10)
    lis.push(30)
    lis.push(69)
    lis.getCount()

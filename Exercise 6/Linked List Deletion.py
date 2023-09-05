class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    def deleteatbegin(self):
        temp = self.head
        self.head = self.head.next
        del temp
    def deleteatend(self):
        ptr1 = self.head.next
        ptr2 = self.head.next.next
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = None
        del ptr2
    def deleteAtGivenPosition(self, position):
        if self.head:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print("\nIndex is out of range.")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next    
    def printLn(self):
        current = self.head
        while current:
            print(current.data,"-> ",end = "")
            current = current.next 
        print(None)    
LL = LinkedList()
noOfNodes = int(input("Enter No Of Nodes:"))
for _ in range(noOfNodes):
    inputdata = int(input())
    LL.insert(inputdata)
LL.printLn()  
LL.deleteatbegin()
position = int(input())
LL.deleteAtGivenPosition(position)  
LL.deleteatend()
LL.printLn()
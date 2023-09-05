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
    def rotate(self):
        ptr1 = self.head.next
        ptr2 = self.head.next.next
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = None
        ptr2.next = self.head
        self.head = ptr2  
        return self.head       
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
k = int(input("enter no of rotations:"))
for _ in range(k):
    LL.rotate()
LL.printLn()    
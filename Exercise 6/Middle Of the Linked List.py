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
    def Middleofthelist(self):
        slowptr = self.head
        fastptr=slowptr.next
        while fastptr and fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
        print("Middle of the linked list",slowptr.data)  
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
LL.Middleofthelist()

class Node:
    def __init__(self,data = None , next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self) -> None:
        self.head = None        
    def insert(self,data):
        newnode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next 
            current.next = newnode
        else:
            self.head = newnode
    def insertatBegin(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    def insertatMiddle(self,data):
        newnode = Node(data)
        slowptr = self.head
        fastptr=slowptr.next
        while fastptr and fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
        print("Middle of the linked list",slowptr.data)
        newnode.next = slowptr.next
        slowptr.next = newnode
    def insertatend(self,data):
        newnode = Node(data)
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode        
    def printLn(self):
        current = self.head    
        while current.next:
            print(current.data,"-> ",end="")
            current = current.next
        print(None)
LL = LinkedList()
noOfNodes = int(input("Enter No Of Nodes:"))
for _ in range(noOfNodes):
    inputdata = int(input())
    LL.insert(inputdata)
LL.printLn() 
print("After Insertion")
LL.insertatBegin(int(input()))
LL.insertatMiddle(int(input()))
LL.printLn()            
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
    def cycle(self):
        p1 = p2 = self.head
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False    
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
print(LL.cycle())

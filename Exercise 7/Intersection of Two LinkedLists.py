class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self) -> None:
        super().__init__()
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
def printLn(head):
    current = head
    while current:
        print(current.data,"-> ",end = "")
        current = current.next 
    print(None)    
class solution:        
    def sortedIntersect(self, a, b):
        dummy = Node()
        tail = dummy
        dummy.next = None

        while (a != None and b != None):
            if (a.data == b.data):
                tail.next = self.insert((tail.next), a.data)
                tail = tail.next
                a = a.next
                b = b.next
            elif  a.data < b.data:
                a = a.next
            else:
                b = b.next;   
        return (dummy.next);       
list1 = LinkedList()
list2 = LinkedList()
noOfNodesofL1 = int(input("Enter No Of Nodes of linked list 1:"))
for _ in range(noOfNodesofL1):
    inputdata = int(input())
    list1.insert(inputdata)
noOfNodesofL2 = int(input("Enter no of nodes for L2:"))
for _ in range(noOfNodesofL2):
    inputdata = int(input())
    list2.insert(inputdata)
head_ref = solution().sortedIntersect(list1,list2)
printLn(head_ref)
    

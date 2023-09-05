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
    def isPalindrome(self):
        p1=p2=self.head
        while p2 and p2.next:
            p2=p2.next.next
            p1=p1.next
        prev=None
        while p1:                     
            nxt=p1.next
            p1.next=prev
            prev=p1
            p1=nxt
        left,right=self.head,prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True        
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
print(LL.isPalindrome())

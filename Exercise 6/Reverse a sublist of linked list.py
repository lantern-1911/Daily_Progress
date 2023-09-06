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
    def reverseBetween(head, m, n):
  
        if (m == n):
            return head
        revs = None
        revs_prev = None
        revend = None
        revend_next = None

        i = 1
        curr = head
      
        while (curr and i <= n):
            if (i < m):
                revs_prev = curr
   
            if (i == m):
                revs = curr
   
            if (i == n):
                revend = curr
                revend_next = curr.next
   
            curr = curr.next
            i += 1
  
        revend.next = None
        revend = reverse(revs)
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            head=prev
            return prev
   
        if (revs_prev):
            revs_prev.next = revend
        else:
            head = revend
   
        revs.next = revend_next
        return head
        
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
LL.reverseBetween(m = int(input()),n=int(input())) 

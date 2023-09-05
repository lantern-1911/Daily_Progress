class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
class LinkedList():
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
    def printLn(self, head):
        current = head
        while current:
            print(current.data,"-> ",end = "")
            current = current.next 
        print(None)    
class Solution(LinkedList):
    def __init__(self):
        super().__init__()
    def mergeTwoLists(self,list1, list2):
        cur = dummy = Node()
        while list1 and list2:               
            if list1.data < list2.data:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next        
list1 = LinkedList()
list2 = LinkedList()
LL3 = LinkedList()
Sol = Solution()
noOfNodesofL1 = int(input("Enter No Of Nodes of linked list 1:"))
for _ in range(noOfNodesofL1):
    inputdata = int(input())
    list1.insert(inputdata)
noOfNodesofL2 = int(input("Enter no of nodes for L2:"))
for _ in range(noOfNodesofL2):
    inputdata = int(input())
    list2.insert(inputdata)
head = Sol.mergeTwoLists(list1,list2)
LL3.printLn(head)    
    

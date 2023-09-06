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
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        next = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head
 
    def addTwoLists(self, first, second):
        curr1 = self.reverse(first)
        curr2 = self.reverse(second)
 
        sum = 0
        carry = 0
        res = None
        prev = None

        while curr1 is not None or curr2 is not None:

            sum = carry + (curr1.data if curr1 else 0) + \
                (curr2.data if curr2 else 0)
 
            carry = (1 if sum >= 10 else 0)
            sum = sum % 10
            temp = Node(sum)
            if res is None:
                res = temp
 
            else:
                prev.next = temp
 
            prev = temp
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        if carry > 0:
            temp.next = Node(carry)

        ans = self.reverse(res)
        return ans
     
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
print(solution().addTwoLists(list1,list2))
    

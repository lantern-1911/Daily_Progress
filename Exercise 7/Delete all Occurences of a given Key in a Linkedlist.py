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
    def deleteAllOccurencesOfAGivenKeyInALinkedList(self, key):
        temp = self.head
        while temp and temp.data == key:
            self.head = temp.next
            temp = self.head
        while temp:
            while temp and temp.data == key:
                prev = temp
                temp = temp.next
            if temp:
                return self.head
            prev.next = temp.next
            temp = prev.next
        return self.head


    def printLn(self,head):
        current = head
        while current:
            print(current.data,"-> ",end = "")
            current = current.next 
        print(None)    
LL = LinkedList()
noOfNodes = int(input("Enter No Of Nodes:"))
for _ in range(noOfNodes):
    inputdata = int(input())
    LL.insert(inputdata)

head_ref = LL.deleteAllOccurencesOfAGivenKeyInALinkedList(key=int(input()))
LL.printLn(head_ref)
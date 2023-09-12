class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self) -> None:
        self.root = None
    def insert(self,root,key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root
    def isValid(self,root):
        def bst(root,min1,max1):
            if not root:
                return True
            
            if(min1!=None and root.val<=min1) or (max1!=None and root.val>=max1):
                return False
            
            if not bst(root.left,min1,root.val) or not bst(root.right,root.val,max1):
                return False
            
            return True
           
        return bst(root,None,None)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)
root = Node(int(input("enter root node:")))
noOfNodes = int(input("enter no of nodes:"))
bst = Tree()
for i in range(noOfNodes):
    root =  bst.insert(root,int(input()))
bst.inorder(root)               
print(bst.isValid(root))
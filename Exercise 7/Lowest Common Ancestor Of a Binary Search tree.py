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
    def lowestCommonAncestorofaBst(self,root,p,q):
            if root.val == p or root.val == q or not root:
                return root
            left = self.lowestCommonAncestorofaBst(root.left,p,q)
            right = self.lowestCommonAncestorofaBst(root.right,p,q)
            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right
root = Node(int(input("enter root node:")))
noOfNodes = int(input("enter no of nodes:"))
bst = Tree()
for i in range(noOfNodes):
    root =  bst.insert(root,int(input()))
p = int(input())
q = int(input())    
root = bst.lowestCommonAncestorofaBst(root,p,q)
print(root.val)               
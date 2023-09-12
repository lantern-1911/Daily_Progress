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
    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        self.length = max(self.length,left+right)
        return max(left,right)+1
    def diameterOfBinaryTree(self, root):
            self.length = 0
            self.depth(root)
            return self.length
root = Node(int(input("enter root node:")))
noOfNodes = int(input("enter no of nodes:"))
bst = Tree()
for i in range(noOfNodes):
    root =  bst.insert(root,int(input()))
print(bst.diameterOfBinaryTree(root))               
from collections import deque
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
    def rightSideView(self, root):
        result = dict()
        
        def dfs(node, level):
            if node is None:
                return
            
            result[level] = node.val
        
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 0)
        
        return  result.values()  
root = Node(int(input("enter root node:")))
noOfNodes = int(input("enter no of nodes:"))
bst = Tree()
for i in range(noOfNodes):
    root =  bst.insert(root,int(input()))
print(bst.rightSideView(root))               
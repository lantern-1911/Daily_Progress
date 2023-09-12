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

class Solution:
    def binaryTreePaths(self, root):
        def dfs(root,path):
            if not root.left and not root.right:
                return result.append(path+str(root.val))
            if root.left:
                dfs(root.left,path+str(root.val)+'->')
            if root.right:
                dfs(root.right,path+str(root.val)+'->')
        result = []
        dfs(root,"")
        return result   
root = Node(int(input("enter root node:")))
noOfNodes = int(input("enter no of nodes:"))
bst = Tree()
for i in range(noOfNodes):
    root =  bst.insert(root,int(input()))
sl = Solution().binaryTreePaths(root=root)
print(sl)
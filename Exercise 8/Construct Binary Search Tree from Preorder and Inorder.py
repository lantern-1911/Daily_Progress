from collections import deque
class Node:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
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
    def leveOrder(self,root):
        if not root:
            return None
        q = deque()
        q.append(root)
        ans = []
        while q:
            l = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    l.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if l:
                ans.append(l)

        return ans   
    
class solution:
    def buildTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        root = Node(preorder[0])
        Tree.insert(self,root = root,key = preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:mid +1], inorder[:mid])
        root.right = self.buildTree(preorder[mid +1:], inorder[mid +1:])
        return root    
preorder = [3,9,20,15,17]
inorder = [9,3,15,20,17]
sl = solution()
root = sl.buildTree(preorder,inorder)
bt = Tree()
print(bt.leveOrder(root))
"""
root = Node(int(input("enter root node:")))
noOfNodes = int(input("enter no of nodes:"))
bst = Tree()
for i in range(noOfNodes):
    root =  bst.insert(root,int(input()))
print(bst.leveOrder(root))               """
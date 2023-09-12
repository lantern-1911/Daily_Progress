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

class Solution:
    def addOneRow(self, root, val, depth):
        if depth == 1:
            newroot = Node(val,root )
            return newroot
        
        
        queue = [(root, 1)]
        while len(queue) > 0:
            node, level = queue.pop(0)
            if level == depth - 1:             
                oldleft = node.left
                oldright = node.right
                newleft = Node(val, oldleft,None)
                newright = Node(val,None, oldright)
                node.left = newleft
                node.right = newright
            
            if node.left:
                queue.append((node.left, level+1))
                
            if node.right:
                queue.append((node.right, level+1))

                
        return root       
root = Node(int(input("enter root node:")))
noOfNodes = int(input("enter no of nodes:"))
bst = Tree()
for i in range(noOfNodes):
    root =  bst.insert(root,int(input()))
sl = Solution()
sl.addOneRow(root,val = int(input()),depth = int(input()))               
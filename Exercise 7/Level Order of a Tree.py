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
root = Node(int(input("enter root node:")))
noOfNodes = int(input("enter no of nodes:"))
bst = Tree()
for i in range(noOfNodes):
    root =  bst.insert(root,int(input()))
print(bst.leveOrder(root))               
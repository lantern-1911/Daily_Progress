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
   def buildTree(self, inorder, postorder) :
        if not inorder or not postorder:
            return None
        root = Node(postorder[-1])
        Tree.insert(self,root=root,key=postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:],postorder[mid:-1])
        return root
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
sl = solution()
root = sl.buildTree(inorder,postorder)
bt = Tree()
print(bt.leveOrder(root))
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for l1 in lists:
            while l1:
                arr.append(l1.val)
                l1 = l1.next
        arr=sorted(arr)
        if arr != []:
            self.head = ListNode()
            self.current = self.head
            for n in arr:
                self.current.next = ListNode(n)
                self.current = self.current.next
            return self.head.next
        else:
            return
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head

        p = dummyHead
        q = dummyHead

        for i in range(n + 1):
            q = q.next

        while q:
            p = p.next
            q = q.next

        delNode = p.next
        p.next = delNode.next
        return dummyHead.next

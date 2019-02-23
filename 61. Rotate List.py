# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        if k == 0:
            return head

        dummyHead = ListNode(0)
        dummyHead.next = head
        cur = dummyHead.next
        length = 1

        while cur.next:
            cur = cur.next
            length += 1
        if length == 1:
            return head
        if length == k:
            return head
        if k > length:
            k = k % length

        n = length - k
        tempEnd = head
        cur.next = dummyHead.next
        while n - 1 != 0:
            tempEnd = tempEnd.next
            n -= 1
        tempFront = tempEnd.next
        tempEnd.next = None
        dummyHead.next = tempFront

        return dummyHead.next


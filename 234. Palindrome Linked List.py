# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        p1 = head
        p2 = head

        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        p1 = p1.next

        prev = None
        # cur = p1

        while p1:
            nexttemp = p1.next
            p1.next = prev

            prev = p1
            p1 = nexttemp

        # while prev:
        #     print(prev.val)
        #     prev = prev.next
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True
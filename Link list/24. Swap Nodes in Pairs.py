# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        first = head
        start = first.next
        while True:
            second = first.next
            temp = second.next
            second.next = first
            if temp is None or temp.next is None:
                first.next = temp
                break
            first.next = temp.next
            first = temp
        return start
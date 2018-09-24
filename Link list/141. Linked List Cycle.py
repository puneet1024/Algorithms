# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        temp = head
        runner = head
        while (runner.next is not None and runner.next.next is not None):
            temp = temp.next
            runner = runner.next.next
            if (runner == temp):
                return True
        return False

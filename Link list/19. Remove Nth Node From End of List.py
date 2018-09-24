# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        temp1 = head
        if head is None or head.next is None:
            return None
        count = 1
        while count <= n:
            temp = temp.next
            count += 1
        if temp == None:
            return temp1.next
        while temp.next is not None:
            temp = temp.next
            temp1 = temp1.next
        temp1.next = temp1.next.next
        return head


#Solution Node 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         if head is None or head.next is None:
#             return None
#         temp = head
#         temp1 = head
#         for i in range(n):
#             temp = temp.next
#         if temp is None:
#             return temp1.next
#         while temp.next is not None:
#             temp = temp.next
#             temp1 = temp1.next
#         temp1.next = temp1.next.next
#         return head


l1 =  ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
s = Solution()
s.removeNthFromEnd(l1,2)
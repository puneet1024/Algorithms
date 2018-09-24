# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tempA = l1
        tempB = l2
        temp3 =head3= ListNode(-1)
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        while tempA is not None and tempB is not None:
            if tempA.val < tempB.val:
                temp3.next = tempA
                tempA = tempA.next
            else:
                temp3.next = tempB
                tempB = tempB.next
            temp3=temp3.next
        if tempA is None:
            temp3.next = tempB
        else:
            temp3.next = tempA
        return head3.next.val

l1 = ListNode([1,2,4])
l2 = ListNode([1,3,4])
s = Solution()
print(s.mergeTwoLists(l1,l2))
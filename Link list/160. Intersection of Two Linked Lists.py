# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tempA,tempB = headA, headB
        la=lb=0
        if tempA == None or tempB == None:
            return None
        while tempA is not None:
            la+=1
            tempA=tempA.next
        while tempB is not None:
            lb+=1
            tempB=tempB.next
        if la > lb:
            while la-lb is not 0:
                headA = headA.next
                la-=1
        else:
            while lb-la is not 0:
                headB = headB.next
                lb-=1
        while headA is not None and headB is not None:
            if headA.val == headB.val:
                return headA
            else:
                headA=headA.next
                headB = headB.next
        return None

l1 = ListNode(3)
l2 = ListNode(3)
s= Solution()
print(s.getIntersectionNode(l1,l2))
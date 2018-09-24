class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = head
        if head is None:
            return None
        while temp.next is not None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        if head.val == val:
            return head.next
        else:
            return  head



l = ListNode([6,1,2,3,4,5,6])
s = Solution()
print(s.removeElements(l,6))

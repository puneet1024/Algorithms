class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        ha = tempa = ListNode(0)
        tempb = head
        hb = first = ListNode(0)
        while (tempb is not None):
            if tempb.val < x:
                tempa.next = tempb
                tempa = tempa.next
            else:
                first.next = tempb
                first = first.next
            tempb = tempb.next
        first.next = None
        tempa.next = hb.next
        while(ha):
            print(ha.next.val)
            ha=ha.next

l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(2)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(2)

s = Solution()
s.partition(l1,3)
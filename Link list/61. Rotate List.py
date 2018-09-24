class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0

        if head == None or k < 0:
            return None
        temp = temp2 = temp3 = head
        length = 0
        while(temp is not None):
            length = length+1
            temp = temp.next
        k = k % length

        while temp3.next is not None:
            temp3 = temp3.next
        while (count < (length-k)-1):
            temp2 = temp2.next
            count+=1
        temp4 = temp2.next
        temp2.next = None
        temp3.next = head
        return temp4.val


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

s = Solution()
print(s.rotateRight(l,2))
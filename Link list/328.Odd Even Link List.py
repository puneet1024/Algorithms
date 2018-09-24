#328. Odd Even Linked List


#Think for 2 cases
# ->1,2,3,4,5,6
# ->1,2,3,4,5,6,7
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = temp1 = head
        temp2 = temp3 = head.next
        length = 0   #check for length, the odd position one has one link list and even position has another link list, and then join them
        stop = 0
        while(temp):
            length+=1
            temp = temp.next
        if length %2 == 0:
            stop = length - 2           #for even length, it needs to run one loop less than the odd
        else:
            stop = length - 1
        for i in range(0,stop):
            if i%2 == 0:
                temp1.next = temp2.next
                temp1 = temp2.next
            else:
                temp2.next = temp1.next
                temp2 = temp1.next
        temp1.next = temp3
        return head.val, head.next.val, head.next.next.val, head.next.next.next.val, head.next.next.next.next.val, head.next.next.next.next.next.val, head.next.next.next.next.next.next.val


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next= ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
l1.next.next.next.next.next.next = ListNode(7)

s = Solution()
print(s.oddEvenList(l1))
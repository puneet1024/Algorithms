# Definition for singly-linked list.
#Find the sum of each individual list , then add both numbers, then convert the number into a list and then convert the list into a linked list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


        def sumlst(node):       #Function to find the sum of the values of each link list
            su = 0
            while (node is not None):
                su = su * 10 + node.val
                node = node.next
            return su

        su = sumlst(l1) + sumlst(l2)        #adding both the sum
        li = []
        for i in str(su):                   #converting the sum into a list
            li.append(int(i))
        head = temp = ListNode(None)
        for d in li:                        #converting the list into a linked list
            temp.next = ListNode(d)
            temp = temp.next
        return head.next.val


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l2 = ListNode(3)
l2.next = ListNode(2)
l2.next.next = ListNode(1)
s = Solution()
print(s.addTwoNumbers(l1,l2))


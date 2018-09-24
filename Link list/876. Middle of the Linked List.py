#Given a non-empty, singly linked list with head node head, return a middle node of linked list.

#If there are two middle nodes, return the second middle node.

#INPUT  - [1,2,3,4,5]
#OUTPUT - [3,4,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        li = []
        if head.next is None:
            li.append(head.val)
        else:
            temp1 = head
            temp2 = head
            while temp2 is not None and temp2.next is not None:
                temp1 = temp1.next
                temp2 = temp2.next.next
            while(temp1 is not None):
                li.append(temp1.val)
                temp1=temp1.next
        return li
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a, b, x = 0, 0, 1
        while l1 != None:
            a += x * l1.val
            x *= 10
            l1 = l1.next
        x = 1
        while l2 != None:
            b += x * l2.val
            x *= 10
            l2 = l2.next
        y = a + b
        if y == 0:
            return ListNode(y)
        prev = None
        head = None
        while y != 0:
            z = y % 10
            y = y//10
            if not head:
                head = ListNode(z)
                prev = head
            else:
                new = ListNode(z)
                prev.next = new
                prev = new
        return head
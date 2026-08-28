# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = None
        curr = None

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a + b + carry
            carry = total // 10

            new_node = ListNode(total % 10)

            if head is None:
                head = new_node
                curr = head
            else:
                curr.next = new_node
                curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head
        
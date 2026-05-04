# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # “We simulate digit-by-digit addition with carry, just like manual addition, using a dummy node to build the result list.”
        dummy = ListNode(0)
        curr = dummy
        carry  = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            #new digit 
            digit = total % 10
            carry = total // 10

            curr.next = ListNode(digit)
            curr = curr.next


            # Move Pointer
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1. FIND THE MID
        fast, slow = head, head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # 2. REVERSE THE SECOND HALF
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 3. MERGE THE 2 LIST
        first, second = head, prev

        while first and second:
            temp1 = first.next
            temp2 = second.next


            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
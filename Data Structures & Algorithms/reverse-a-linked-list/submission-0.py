# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None                     #will become the new head
        curr = head                     #start from head

        while curr:     
            next_node = curr.next       # 1. Store next node

            curr.next = prev            # 2. reverse pointer

            prev = curr                 # 3. move prev forward
            curr = next_node            # 4. move curr forward
        
        return prev                     #new head
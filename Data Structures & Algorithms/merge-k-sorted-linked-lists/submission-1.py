from typing import List, Optional

import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
“At every step, I only need the smallest current node among all linked lists.”
"""
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min heap to always fetch the smallest node

        # Heap stores:

        # (node value, unique index, actual node)

        #

        # We use index because Python cannot compare ListNode objects directly

        min_heap = []

        # ---------------------------------------------------------

        # STEP 1:

        # Push the head of every linked list into the heap

        # ---------------------------------------------------------

        for index, node in enumerate(lists):

            # Ignore empty linked lists

            if node:

                heapq.heappush(min_heap, (node.val, index, node))

        # ---------------------------------------------------------

        # Dummy node helps simplify linked list construction

        # ---------------------------------------------------------

        dummy = ListNode(0)

        # 'tail' always points to the last node

        # in the merged linked list

        tail = dummy

        # ---------------------------------------------------------

        # STEP 2:

        # Keep extracting the minimum node

        # ---------------------------------------------------------

        while min_heap:

            # Pop smallest node from heap

            value, index, node = heapq.heappop(min_heap)

            # Attach this node to the merged list

            tail.next = node

            # Move tail forward

            tail = tail.next

            # -----------------------------------------------------

            # If the popped node has a next node,

            # push it into the heap

            # -----------------------------------------------------
            if node.next:

                heapq.heappush(

                    min_heap,

                    (node.next.val, index, node.next)

                )

            # Head of merged list starts after dummy node

        return dummy.next
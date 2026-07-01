# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def hasCycle(
        self,
        head: Optional[ListNode]
    ) -> bool:
        """
        Detect whether a linked list contains a cycle.

        Floyd's Cycle Detection Algorithm
        (Tortoise and Hare)

        Slow pointer:
            Moves 1 step at a time.

        Fast pointer:
            Moves 2 steps at a time.

        If a cycle exists,
        the fast pointer will eventually
        catch the slow pointer.
        """

        # Both pointers start from the head
        slow_pointer = head
        fast_pointer = head

        # Continue while fast pointer
        # can move two steps.
        while fast_pointer and fast_pointer.next:

            # Move one step
            slow_pointer = slow_pointer.next

            # Move two steps
            fast_pointer = fast_pointer.next.next

            # If both pointers meet,
            # a cycle exists.
            if slow_pointer == fast_pointer:
                return True

        # Fast pointer reached the end,
        # so no cycle exists.
        return False
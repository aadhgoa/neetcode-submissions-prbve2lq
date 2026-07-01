# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self,
        first_list: Optional[ListNode],
        second_list: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted linked list.

        Idea:
        Compare the current node of both lists.
        Always append the smaller node to the merged list.

        Continue until one list is exhausted,
        then append the remaining nodes from the other list.
        """

        # Dummy node simplifies handling the head
        # of the merged linked list.
        dummy_head = ListNode()

        # Always points to the last node
        # of the merged list.
        current = dummy_head

        # Continue while both lists still have nodes.
        while first_list and second_list:

            # Choose the smaller node.
            if first_list.val <= second_list.val:

                current.next = first_list

                # Move to next node
                # in the first list.
                first_list = first_list.next

            else:

                current.next = second_list

                # Move to next node
                # in the second list.
                second_list = second_list.next

            # Move the merged list pointer forward.
            current = current.next

        # At most one list still has nodes.
        #
        # Since both lists are already sorted,
        # we can directly attach the remaining nodes.
        if first_list:
            current.next = first_list

        if second_list:
            current.next = second_list

        # Skip the dummy node and
        # return the actual merged list.
        return dummy_head.next
import heapq

class Solution:
    def isNStraightHand(
        self,
        hand: List[int],
        groupSize: int
    ) -> bool:
        """
        Goal:
        Divide all cards into groups of
        consecutive numbers.

        Greedy Idea:

        Always start forming a group
        from the smallest available card.
        """

        # Total cards must be divisible
        # by the group size.
        if len(hand) % groupSize != 0:
            return False

        # Count frequency of each card
        card_frequency = {}

        for card in hand:
            card_frequency[card] = (
                card_frequency.get(card, 0) + 1
            )

        # Min Heap stores the smallest
        # available card at the top.
        min_heap = list(card_frequency.keys())
        heapq.heapify(min_heap)

        # Continue until every card
        # has been used.
        while min_heap:

            # Smallest remaining card
            first_card = min_heap[0]

            # Try building one complete group
            #
            # Example:
            #
            # first_card = 4
            # groupSize = 3
            #
            # Need:
            # 4, 5, 6
            for current_card in range(
                first_card,
                first_card + groupSize
            ):

                # Missing card
                if current_card not in card_frequency:
                    return False

                # Use one copy
                card_frequency[current_card] -= 1

                # Card completely used
                if card_frequency[current_card] == 0:

                    # Smallest card should
                    # disappear first.
                    #
                    # If another card reaches
                    # zero before the heap's
                    # minimum, ordering has
                    # become invalid.
                    if current_card != min_heap[0]:
                        return False

                    # Remove card from both
                    # frequency map and heap.
                    heapq.heappop(min_heap)
                    del card_frequency[current_card]

        return True
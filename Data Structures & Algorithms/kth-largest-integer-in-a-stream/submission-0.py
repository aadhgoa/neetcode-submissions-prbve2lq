import heapq


class KthLargest:

    def __init__(
        self,
        kth_position: int,
        initial_numbers: List[int]
    ):
        """
        Maintain a Min Heap of size k.

        Heap stores only the k largest
        numbers seen so far.

        Heap top = kth largest element.
        """

        self.kth_position = kth_position

        # Min Heap containing
        # at most k elements
        self.k_largest_numbers = initial_numbers

        heapq.heapify(self.k_largest_numbers)

        # Remove smallest elements
        # until only k remain
        while (
            len(self.k_largest_numbers)
            > self.kth_position
        ):
            heapq.heappop(
                self.k_largest_numbers
            )

    def add(self, new_number: int) -> int:
        """
        Add a new number into stream.
        """

        # Add number into heap
        heapq.heappush(
            self.k_largest_numbers,
            new_number
        )

        # Keep heap size exactly k
        if (
            len(self.k_largest_numbers)
            > self.kth_position
        ):
            heapq.heappop(
                self.k_largest_numbers
            )

        # Heap root is always
        # kth largest element
        return self.k_largest_numbers[0]
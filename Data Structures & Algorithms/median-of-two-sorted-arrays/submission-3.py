class Solution:
    def findMedianSortedArrays(
        self,
        first_array: List[int],
        second_array: List[int]
    ) -> float:
        """
        Find the median of two sorted arrays.

        Key Idea:
        Perform binary search on the smaller array to find a
        partition such that:

            Left Partition <= Right Partition

        Once the partition is correct,
        the median can be computed directly.
        """

        # Always binary search on the smaller array
        if len(first_array) > len(second_array):
            first_array, second_array = second_array, first_array

        first_length = len(first_array)
        second_length = len(second_array)

        left = 0
        right = first_length

        while left <= right:

            # Partition in first array
            partition_first = (left + right) // 2

            # Partition in second array
            #
            # Total elements on the left side
            # should equal half of the combined arrays.
            partition_second = (
                (first_length + second_length + 1) // 2
                - partition_first
            )

            # -------------------------------
            # Elements around the partitions
            # -------------------------------

            left_first = (
                float("-inf")
                if partition_first == 0
                else first_array[partition_first - 1]
            )

            right_first = (
                float("inf")
                if partition_first == first_length
                else first_array[partition_first]
            )

            left_second = (
                float("-inf")
                if partition_second == 0
                else second_array[partition_second - 1]
            )

            right_second = (
                float("inf")
                if partition_second == second_length
                else second_array[partition_second]
            )

            # ------------------------------------
            # Correct partition found
            #
            # Every left element <= every right element
            # ------------------------------------
            if (
                left_first <= right_second
                and
                left_second <= right_first
            ):

                total_length = first_length + second_length

                # Odd number of elements
                if total_length % 2 == 1:
                    return max(
                        left_first,
                        left_second
                    )

                # Even number of elements
                return (
                    max(left_first, left_second)
                    +
                    min(right_first, right_second)
                ) / 2

            # Too many elements taken from first array
            elif left_first > right_second:
                right = partition_first - 1

            # Too few elements taken from first array
            else:
                left = partition_first + 1

        return 0.0
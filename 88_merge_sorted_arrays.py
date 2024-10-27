import time
import tracemalloc

class Solution:
    """
    A class used to merge two sorted arrays.

    Methods
    -------
    merge(nums1, m, nums2, n)
        Merges two sorted arrays nums1 and nums2 into a single sorted array in-place.
    """

    def __init__(self):
        """
        Initializes the Solution class.
        """
        pass

    def __repr__(self):
        """
        Returns a string representation of the Solution class.
        """
        return f'Solution()'

    def merge(self, nums1, m, nums2, n):
        """
        Merges two sorted arrays nums1 and nums2 into a single sorted array in-place.

        Parameters
        ----------
        nums1 : List[int]
            The first sorted array with a size of m + n, where the first m elements denote the sorted elements and the rest are 0s.
        m : int
            The number of valid elements in nums1.
        nums2 : List[int]
            The second sorted array with a size of n.
        n : int
            The number of valid elements in nums2.
        """
        
        # Naive approach: Create a new array and merge elements
        start_time_naive = time.time()
        tracemalloc.start()
        merged = []
        i, j = 0, 0

        # Merge elements from both arrays into the new array
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Append remaining elements from nums1
        while i < m:
            merged.append(nums1[i])
            i += 1

        # Append remaining elements from nums2
        while j < n:
            merged.append(nums2[j])
            j += 1

        # Copy merged elements back to nums1
        for k in range(m + n):
            nums1[k] = merged[k]
        end_time_naive = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Naive approach took {end_time_naive - start_time_naive:.6f} seconds, used {current / 10**6:.6f} MB, peak was {peak / 10**6:.6f} MB, nums1 = {nums1}")

        """
        More ambitious approach: In-place merge from the end
        Start from the end of both arrays and merge in reverse order
        """
        start_time_inplace = time.time()
        tracemalloc.start()
        i, j, k = m - 1, n - 1, m + n - 1

        # While there are elements to be merged
        while j >= 0:
            # If there are elements in nums1 and the current element in nums1 is greater than the current element in nums2
            if i >= 0 and nums1[i] > nums2[j]:
                # Place the element from nums1 at the end of the merged array
                nums1[k] = nums1[i]
                i -= 1
            else:
                # Place the element from nums2 at the end of the merged array
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        end_time_inplace = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"In-place approach took {end_time_inplace - start_time_inplace:.6f} seconds, used {current / 10**6:.6f} MB, peak was {peak / 10**6:.6f} MB, nums1 = {nums1}")

if __name__ == "__main__":
    solution = Solution()
    solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
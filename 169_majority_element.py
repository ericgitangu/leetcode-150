import collections
import time
import tracemalloc
from termcolor import colored

class Solution:
    """
    169. Majority Element - EASY

    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

    Example 1:

    Input: nums = [3,2,3]
    Output: 3

    Example 2:

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

    Constraints:

    n == nums.length
    1 <= n <= 5 * 10^4
    -10^9 <= nums[i] <= 10^9

    Follow-up: Could you solve the problem in linear time and in O(1) space?
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

    def majorityElement(self, nums: list[int]) -> int:
        """
        Finds the majority element in the array nums.

        Parameters
        ----------
        nums : List[int]
            The input array of integers.

        Returns
        -------
        int
            The majority element in the array.
        """
        n = len(nums)
        majority_count = n // 2

        # Naive approach
        start = time.time()
        tracemalloc.start()
        print(colored(f"n: {n}, majority_count: {majority_count} using naive approach", 'green'))
        for num in nums:
            # Count the occurrences of each element
            count = sum(1 for elem in nums if elem == num)
            # Check if the count is greater than the majority count
            if count > majority_count:
                majority_element = num
                break
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(colored(f"Time taken: {end - start} seconds using naive approach/ O(n^2). Majority element is {majority_element}", 'green'))
        print(colored(f"Memory usage: {current / 10**6:.6f} MB, Peak: {peak / 10**6:.6f} MB", 'red'))

        # Sorting approach
        start = time.time()
        tracemalloc.start()
        print(colored(f"n: {n}, majority_count: {majority_count} using sorting approach", 'green'))
        # Sort the array
        nums.sort()
        # The majority element will be at the middle index after sorting
        majority_element = nums[n // 2]
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(colored(f"Time taken: {end - start} seconds using sorting approach/ O(nlogn). Majority element is {majority_element}", 'blue'))
        print(colored(f"Memory usage: {current / 10**6:.6f} MB, Peak: {peak / 10**6:.6f} MB", 'red'))

        # Hashmap approach
        start = time.time()
        tracemalloc.start()
        print(colored(f"n: {n}, majority_count: {majority_count} using hashmap approach", 'green'))
        # Use a hashmap to count the occurrences of each element
        counts = collections.Counter(nums)
        # Find the element with the maximum count
        majority_element = max(counts.keys(), key=counts.get)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(colored(f"Time taken: {end - start} seconds using hashmap approach/ O(n). Majority element is {majority_element}", 'blue'))
        print(colored(f"Memory usage: {current / 10**6:.6f} MB, Peak: {peak / 10**6:.6f} MB", 'red'))

if __name__ == "__main__":
    solution = Solution()
    solution.majorityElement([3,2,3])
    solution.majorityElement([2,2,1,1,1,2,2])

from termcolor import colored


class Solution:
    """
    26. Remove Duplicates from Sorted Array

    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.
    Custom Judge:

    The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }
    If all assertions pass, then your solution will be accepted.

    Example 1:

    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    Example 2:

    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    Constraints:

    1 <= nums.length <= 3 * 10^4
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
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

    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Removes duplicates from the sorted array nums in-place and returns the number of unique elements.

        Parameters
        ----------
        nums : List[int]
            The sorted array from which duplicates need to be removed.

        Returns
        -------
        int
            The number of unique elements in nums.
        """
        # Check if the input list is empty, if so return 0 and the empty list
        if not nums:
            return 0, nums
        
        # Initialize the index for unique elements
        unique_idx = 0
        # Iterate through the list starting from the second element
        for idx in range(1, len(nums)):
            # If the current element is different from the last unique element
            if nums[idx] != nums[unique_idx]:
                # Move the unique index forward and update the value at that position
                unique_idx += 1
                nums[unique_idx] = nums[idx]
        
        # Return the count of unique elements and the list up to the last unique element
        return unique_idx + 1, nums[:unique_idx + 1]

if __name__ == "__main__":
    solution = Solution()
    print(f"Output: {colored(solution.removeDuplicates([1,1,2]), 'green')}")
    print(f"Output: {colored(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]), 'green')}")

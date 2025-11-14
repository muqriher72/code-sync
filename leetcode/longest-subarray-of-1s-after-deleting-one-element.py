class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # O(n) time and space

        n = len(nums)
        
        # store count of consecutive 1s upto i - 1
        left = [0] * (n + 1)

        # store count of consecutive 1s starting from i
        right = [0] * (n + 1)

        # build left array
        # start counting indices at 1 instead of 0
        for i, num in enumerate(nums, 1):
            if num == 1:
                left[i] = left[i-1] + 1
            else:
                left[i] = 0

        # build right array
        for i in range(n-1, -1, -1):
            if nums[i] == 1:
                right[i] = right[i+1] + 1
            else:
                right[i] = 0

        # calculate max length
        max_length = 0
        for i in range(n):
            max_length = max(max_length, left[i] + right[i+1])
        return max_length
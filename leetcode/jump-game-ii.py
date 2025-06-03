class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # greedy problem - dynamic programming

        # enumerate function in Python allows you to
        # loop through values and index 

        jumps = 0
        farthest = 0
        end = 0

        # O(n) time
        # O(1) space

        # go through all elements except last
        for i, num in enumerate(nums[:-1]):
            farthest = max(farthest, i + num)
            if i == end:
                jumps += 1
                end = farthest
        return jumps
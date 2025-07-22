class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # O(n) time and O(1) space

        # store the max amount possible to rob considering the previous house
        # was not and was robbed respectively
        prev_no_rob, prev_robbed = 0, 0

        for cur_house_val in nums:
            temp = max(prev_no_rob, prev_robbed)
            prev_robbed = prev_no_rob + cur_house_val
            prev_no_rob = temp
        return max(prev_no_rob, prev_robbed)
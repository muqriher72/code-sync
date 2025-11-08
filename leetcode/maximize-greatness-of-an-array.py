class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        # two pointers and greedy
        # sorting takes O(n log n) time and two pointer takes O(n) time
        # O(1) space

        # sort array first to ensure we pick the smallest larger value
        nums.sort()

        # track current position in sorted array
        left_pointer = 0

        for curr_val in nums:
            left_pointer += curr_val > nums[left_pointer]
        return left_pointer
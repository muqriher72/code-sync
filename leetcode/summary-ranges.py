class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        # O(n) time and O(n) space

        # Helper function to format the ranges as strings
        def format_range(start, end):
            return str(nums[start]) if start == end else f'{nums[start]}->{nums[end]}'
        
        start_idx = 0

        n = len(nums)

        ranges = []

        while start_idx < n:
            end_idx = start_idx

            # keep incrementing end index by 1 as long as next number is consecutive
            while end_idx + 1 < n and nums[end_idx + 1] == nums[end_idx] + 1:
                end_idx += 1
            
            ranges.append(format_range(start_idx, end_idx))

            start_idx = end_idx + 1

        return ranges
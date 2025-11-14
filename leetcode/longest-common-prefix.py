class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # O(m x n) time where n is num of strings in array
        # and m is the length of the shortest string
        # first we index every char of first string in array
        for i in range(0, len(strs[0])):
            # we then look at individual strings after the first string
            for string in strs[1:]:
                # if the strings after the first string are shorter OR
                # if the character at i does not match the first string
                if len(string) <= i or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
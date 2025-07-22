class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # O(len(t)) time and O(1) space
        
        k = 0

        if not s:
            return True

        for ch in t:
            if ch == s[k]:
                k += 1
            
            if k == len(s):
                return True
        return False
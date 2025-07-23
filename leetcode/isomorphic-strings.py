class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # O(n) time and O(C) space
        
        last_seen_s, last_seen_t = [0] * 256, [0] * 256

        for i, (char_s, char_t) in enumerate(zip(s, t), 1):
            ascii_s, ascii_t = ord(char_s), ord(char_t)

            if last_seen_s[ascii_s] != last_seen_t[ascii_t]:
                return False
            
            last_seen_s[ascii_s] = last_seen_t[ascii_t] = i
        
        return True
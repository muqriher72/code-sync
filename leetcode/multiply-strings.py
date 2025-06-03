class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        '''
        return str(int(num1) * int(num2))
        '''

        # O(m * n) time
        # O(m + n) space

        if num1 == '0' or num2 == '0':
            return '0'

        len_num1, len_num2 = len(num1), len(num2)

        res = [0] * (len_num1 + len_num2)

        for i in range(len(num1)-1, -1, -1): 
            int1 = int(num1[i])
            for j in range(len(num2)-1, -1, -1):
                int2 = int(num2[j])

                res[i + j + 1] += int1 * int2

        # Carry over digits < 9 to next place
        for i in range(len_num1 + len_num2 - 1, 0, -1): # O(m + n)
            res[i - 1] += res[i] // 10 # carry
            res[i] %= 10 # keep last digit
        
        # start index to skip leading zeros
        start_index = 0 if res[0] != 0 else 1

        return "".join(str(digit) for digit in res[start_index:])
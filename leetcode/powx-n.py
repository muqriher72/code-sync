class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        # Approach 1
        # O(log n) time complexity
        # O(log n) space complexity

        '''
        if n == 0:
            return 1

        if x == 0:
            return 0
        
        if n < 0:
            x = 1/x
            n = -n
        
        half = self.myPow(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
        '''

        # Approach 2
        # O(log n) time 
        # O(1) space

        def quick_power(base, exp):
            res = 1.0

            while exp:
                if exp & 1: # checks if exponent is odd i.e. n & 1 = 0 = n % 2 means n = 4 is even
                    res *= base
                base *= base
                # halve the exponent
                exp >>= 1 # right shift exponent by 1 i.e. divide by 2
            return res

        return quick_power(x, n) if n >= 0 else 1 / quick_power(x, -n)
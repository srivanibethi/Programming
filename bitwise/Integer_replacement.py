https://leetcode.com/problems/integer-replacement/#/description
It is enough to examine the last two digits to figure out whether incrementing or decrementing will give more 1's. 
Indeed, if a number ends with 01, then certainly decrementing is the way to go. Otherwise, if it ends with 11, then 
certainly incrementing is at least as good as decrementing (*011 -> *010 / *100) or even better (if there are three or more 1's). 
This leads to the following solution:

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n!=1:
            m = n >> 1
            if n %2 == 0:
                n >>= 1
            elif n == 3 or (m & 1) == 0:
                n -= 1
            else:
                n += 1
            count +=1
        return count

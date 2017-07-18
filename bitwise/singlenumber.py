Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

ALGORITHM:

The two numbers that appear only once must differ at some bit, this is how we can distinguish between them. Otherwise, they will be one of the duplicate numbers.

One important point is that by XORing all the numbers, we actually get the XOR of the two target numbers (because XORing two duplicate numbers always results in 0). Consider the XOR result of the two target numbers; if some bit of the XOR result is 1, it means that the two target numbers differ at that location.

Let’s say the at the ith bit, the two desired numbers differ from each other. which means one number has bit i equaling: 0, the other number has bit i equaling 1.

Thus, all the numbers can be partitioned into two groups according to their bits at location i.
the first group consists of all numbers whose bits at i is 0.
the second group consists of all numbers whose bits at i is 1.

Notice that, if a duplicate number has bit i as 0, then, two copies of it will belong to the first group. Similarly, if a duplicate number has bit i as 1, then, two copies of it will belong to the second group.

by XoRing all numbers in the first group, we can get the first number.
by XoRing all numbers in the second group, we can get the second number.Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res_xor = nums[0]
        for i in nums[1:]:
            res_xor ^= i
        bit_set = res_xor & ~(res_xor-1)
        num1 = 0
        num2 = 0
        for i in nums:
            if (i & bit_set) > 0:
                num1 ^= i
            else:
                num2 ^=i
        return [num1, num2]
        

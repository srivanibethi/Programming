

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(2**len(nums)):
            sub_arr = []
            for j in range(len(nums)):
                if self.bit_set(i, j):
                    sub_arr.append(nums[j])
            res.append(sub_arr)
        return res
    
    def bit_set(self, i, j):
        return i & (1<<j)

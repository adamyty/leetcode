class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range((i+1), len(nums)):
                if (nums[i] + nums[j]) == target:
                    return (i, j)

#debug
#nums = [ 2, 7, 11, 15 ]
#target = 9
"""
leetcode input 19
"""
nums = []
target = 16021
i = 0
while i <= 25196:
    nums.append(i)
    i +=2

s = Solution()
print('nums : ',nums)
print('target : ',target)
print('Anser : ',s.twoSum(nums, target))

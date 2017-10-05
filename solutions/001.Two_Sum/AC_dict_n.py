class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
		#return tuple {index1, index2}
        dictMap = {}
        for index, value in enumerate(nums):
            if (target - value) in dictMap:
                return(dictMap[target-value], index)
            dictMap[value] = index

#debug
nums = [ 2, 7, 11, 15 ]
target = 9
s = Solution()
print('nums : ',nums)
print('target : ',target)
print('Anser : ',s.twoSum(nums, target))

class Solution(object):
    def findDisappearedNumbers(self, nums):
        #Mark numbers that exist
        for n in nums:
            i = abs(n) - 1
            nums[i] = -abs(nums[i])
        res = []
        
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)

        return res
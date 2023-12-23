class Solution(object):
    def twoSum(self, nums, target):
        newdict = {}
        for i in range(len(nums)):
            if nums[i] in newdict:
                return [newdict[nums[i]],i]
            else:
                newdict[target - nums[i]] = i
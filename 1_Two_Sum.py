class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            for j in nums[nums.index(i)+1:]:
                if i+j == target:
                    l1 = nums.index(i)
                    l2 = nums[nums.index(i)+1:].index(j)+nums.index(i)+1
                    res = [l1,l2]
                    return res

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

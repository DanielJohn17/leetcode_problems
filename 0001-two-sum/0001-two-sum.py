class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        length = len(nums)

        for i in range(length):
            num_dict[nums[i]] = i
        
        for i in range(length):
            comp = target - nums[i]

            if comp in num_dict and num_dict[comp] != i:
                return [i, num_dict[comp]]
        
        return []
        
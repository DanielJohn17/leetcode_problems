class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ub = len(nums) - 1
        lb = 0

        while lb <= ub:
            mid = (ub + lb) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lb = mid + 1
            elif nums[mid] > target:
                ub = mid - 1
        return -1


        
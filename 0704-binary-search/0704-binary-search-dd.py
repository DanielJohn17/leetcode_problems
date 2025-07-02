class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        def recursive(left, right):
            if left > right:
                return -1
            
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                return recursive(left, mid - 1)
            if nums[mid] < target:
                return recursive(mid + 1, right)

        return recursive(left, right) 
        
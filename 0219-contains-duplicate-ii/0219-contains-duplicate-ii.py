class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        if k > len(nums) - 1 and len(nums) > len(set(nums)):
            return True

        my_set = set(nums[: k + 1])
        ln = len(nums)

        for i in range(ln - k):
            if len(my_set) != k + 1:
                return True
            
            my_set.discard(nums[i])
            if i + k + 1 < ln:
                my_set.add(nums[i + k + 1])
        
        return False
        
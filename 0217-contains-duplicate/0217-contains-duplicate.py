class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = dict()

        for num in nums:
            if num in duplicate:
                return True
            else:
                duplicate[num] = 1
        return False

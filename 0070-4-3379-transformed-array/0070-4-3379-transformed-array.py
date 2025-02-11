class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        LEN = len(nums)
        
        for i in range(LEN):
            result.append(nums[(i + nums[i]) % LEN])

        return result
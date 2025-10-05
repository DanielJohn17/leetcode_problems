class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        tmp_nums = sorted(nums)[len(nums) - k:len(nums)]
        max_sum = []
        
        for num in nums:
            if num in tmp_nums and len(max_sum) < k:
                tmp_nums.remove(num)
                max_sum.append(num)
        
        return max_sum
        
            
            

        
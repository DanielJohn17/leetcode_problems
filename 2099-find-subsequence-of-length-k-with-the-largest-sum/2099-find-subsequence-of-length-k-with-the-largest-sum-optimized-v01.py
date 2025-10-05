class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        tmp_nums = sorted(nums)[len(nums) - k:len(nums)]
        tmp_hash = Counter(tmp_nums)
        max_sum = []

        for num in nums:
            if num in tmp_hash and tmp_hash[num] > 0:
                tmp_hash[num] -= 1
                max_sum.append(num)

        return max_sum
        
            
            

        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c_major = nums[0]
        freq_major = 1

        for num in nums[1:]:
            if freq_major == 0:
                c_major = num
            
            if num == c_major:
                freq_major += 1
            else:
                freq_major -= 1
        
        return c_major
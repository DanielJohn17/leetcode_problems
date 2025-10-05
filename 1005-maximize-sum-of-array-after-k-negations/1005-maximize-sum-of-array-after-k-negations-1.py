class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums_len = len(nums)
        nums = sorted(nums)
        i = 0
        last_pos = False

        while k > 0:
            if nums[i] < 0:
                nums[i] *= -1
                if not last_pos:
                    i += 1
            else:
                if nums[i] > nums[i - 1]:
                    nums[i - 1] *= -1
                else:
                    nums[i] *= -1
                last_pos = True

            if i > nums_len - 1:
                i = 0
        
            k -= 1

        return sum(nums)
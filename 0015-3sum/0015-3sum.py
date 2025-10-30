class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def two_sum(a, target):
            n = len(a)
            left = 0
            right = n - 1

            while left < right:
                total = a[left] + a[right]
                if total == target:
                    ans.append([a[left], a[right], -target])
                    left += 1
                    right -= 1
                    while left < n and a[left] == a[left - 1]:
                        left += 1
                    while right > 0 and a[right] == a[right + 1]:
                        right -= 1
                    continue

                if total < target:
                    left += 1
                    while left < n and a[left] == a[left - 1]:
                        left += 1
                elif total > target:
                    right -= 1
                    while right > 0 and a[right] == a[right + 1]:
                        right -= 1

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            tmp = nums[i + 1:]
            two_sum(tmp, -nums[i])

        return ans

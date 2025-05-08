class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        ans = []
        for i in nums1:
            d[i] += 1

        for i in nums2:
            if i in d and d[i] > 0:
                d[i] -= 1
                ans.append(i)
        
        return ans
        
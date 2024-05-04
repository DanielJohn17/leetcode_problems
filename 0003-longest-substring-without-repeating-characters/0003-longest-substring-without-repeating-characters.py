class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_set = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in c_set:
                c_set.remove(s[left])
                left += 1
            
            c_set.add(s[right])
            result = max(result, right - left + 1)

        return result
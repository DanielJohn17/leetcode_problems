class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        pref_len = len(prefix)

        for word in strs[1:]:
            while prefix != word[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                
                prefix = prefix[0:pref_len]
        
        return prefix


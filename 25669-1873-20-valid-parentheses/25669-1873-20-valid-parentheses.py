class Solution:
    def isValid(self, s: str) -> bool:
        b = []
        p = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char not in p:
                b.append(char)
            elif not b or b[-1] != p[char]:
                return False
            else:
                b.pop()
                
        return len(b) == 0
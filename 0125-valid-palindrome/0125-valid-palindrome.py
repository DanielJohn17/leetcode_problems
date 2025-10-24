class Solution:
    def isPalindrome(self, s: str) -> bool:

        char_list = []

        for char in s:
            if char.isalnum():
                char_list.append(char)

    
        s = "".join(char_list).lower()

        start = 0
        last = len(s) - 1

        while start <= last:
            if s[start] != s[last]:
                return False
            
            start += 1
            last -= 1
        
        return True
            
        
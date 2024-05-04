class Solution:
    def romanToInt(self, s: str) -> int:
        roman =  {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        num = 0
        last_digit = 0

        for char in s:
            n = roman[char]
            if last_digit < n and last_digit > 0:
                num += (n - last_digit * 2)
            else:
                last_digit = n
                num += n
        
        return num
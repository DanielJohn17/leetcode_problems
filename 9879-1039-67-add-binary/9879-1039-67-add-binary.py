class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1, num2 = 0, 0
        po = 0
        ans = []

        for i in range(len(a) - 1, -1, -1):
            num1 += (int(a[i]) * 2**po)
            po += 1

        po = 0
        for i in range(len(b) - 1, -1, -1):
            num2 += (int(b[i]) * 2**po)
            po += 1
        
        s = num1 + num2

        while s > 0:
            ans.append(str(s % 2))
            s //= 2

        return "".join(ans[::-1]) if ans else "0"
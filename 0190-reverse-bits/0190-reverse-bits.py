class Solution:
    def reverseBits(self, n: int) -> int:
        bit = []

        if n == 0:
            return 0

        while n > 0:
            bit.append(n % 2)
            n = n // 2
        
        if len(bit) < 32:
            for _ in range(32 - len(bit)):
                bit.append(0)
        
        ans = 0
        i = len(bit) - 1
        po = 0

        while i >= 0:
            ans += (bit[i] * 2**po)
            po += 1
            i -= 1
        return ans


        
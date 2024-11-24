class Solution:
    def isHappy(self, n: int) -> bool:
        new_set = set()
        n_str = str(n)
        
        while n_str not in new_set:
            num = 0
            for l in n_str:
                num += int(l) ** 2
            if num == 1:
                return True

            new_set.add(n_str)
            n_str = str(num)
        
        return False
        
        
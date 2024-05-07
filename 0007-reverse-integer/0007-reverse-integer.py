class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        is_pos = True
        if x < 0:
            x *= -1
            is_pos = False

        while x > 0:
            rev = (rev * 10) + (x % 10)
            x //= 10

        if is_pos == False:
              rev *= -1
        if rev > 2147483647 or rev < -2147483648:
            return 0

        return rev
        
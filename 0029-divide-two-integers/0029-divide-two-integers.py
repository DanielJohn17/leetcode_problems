class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        quotient = 0
        sign = 1 if (dividend > 0) == (divisor > 0) else -1

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        while abs_dividend >= abs_divisor:
            temp = abs_divisor
            mul = 1

            while abs_dividend >= temp:
                abs_dividend -= temp
                quotient += mul

                mul += mul
                temp += temp

        output = sign * quotient

        return min(2147483647, max(-2147483648, output))

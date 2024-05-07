class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        idx = 0
        direction = 1

        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[idx].append(char)
            if idx == 0:
                direction = 1
            elif idx == numRows - 1:
                direction = -1
            idx += direction

        for i in range(len(rows)):
            rows[i] = "".join(rows[i])

        return "".join(rows)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1], [1,1]]

        if rowIndex <= 1:
            return triangle[rowIndex]

        for i in range(1, rowIndex):
            temp = [1]
            
            last_row = triangle[i]

            for x in range(len(last_row) - 1):
                temp.append(last_row[x] + last_row[x + 1])
            
            temp.append(1)
            triangle.append(temp)
        
        return triangle[rowIndex]
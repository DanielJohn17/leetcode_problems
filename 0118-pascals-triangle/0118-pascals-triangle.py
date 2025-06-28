class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1], [1,1]]

        for i in range(2, numRows):
            temp = [1]
            
            last_row = triangle[i - 1]

            for x in range(len(last_row) - 1):
                temp.append(last_row[x] + last_row[x + 1])
            
            temp.append(1)
            triangle.append(temp)
        
        return triangle[:numRows]
        
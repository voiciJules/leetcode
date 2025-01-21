class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_location_i = set()
        zero_location_j = set()
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[j][i] == 0:
                    zero_location_i.add(i)
                    zero_location_j.add(j)
        
        for row in zero_location_j:
            for column in range(len(matrix[0])):
                matrix[row][column] = 0

        for row in range(len(matrix)):
            for column in zero_location_i:
                matrix[row][column] = 0
                  
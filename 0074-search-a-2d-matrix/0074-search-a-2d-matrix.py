class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row_index in range(len(matrix)):
            if matrix[row_index][-1] == target:
                return True
            elif matrix[row_index][0] == target:
                return True
            elif matrix[row_index][-1] >= target and matrix[row_index][0] <= target:
                if target in matrix[row_index]:
                    return True
                else:
                    return False

        return False

        # after checking the last number of each list, if the last number is smaller than target, it search the whole number in that list. 


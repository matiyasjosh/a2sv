class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            start, end = 0, len(matrix[0]) - 1
            flag = False

            while start <= end:
                mid = (start + end) // 2
                
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1

        return False
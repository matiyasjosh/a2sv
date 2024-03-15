class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + matrix[row][col]

        self.prefix = prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix[row2 + 1][col2 + 1] - self.prefix[row2 + 1][col1] - self.prefix[row1][col2 + 1] + self.prefix[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
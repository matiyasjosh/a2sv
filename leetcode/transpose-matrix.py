class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans = []
        for col in range(len(matrix[0])):
            lst = []
            for row in range(len(matrix)):
                lst.append(matrix[row][col])
            trans.append(lst)
        return trans
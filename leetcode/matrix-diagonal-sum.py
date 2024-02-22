class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])

        diaSum=0
        r=c=0
        while r<row and c<col:
            diaSum+=mat[r][c]
            r+=1
            c+=1
        
        r,c=0, col-1
        while r<row and col>0:
            if (row*col)%2==0 or r!=c:
                diaSum+=mat[r][c]
            r+=1
            c-=1

        return diaSum
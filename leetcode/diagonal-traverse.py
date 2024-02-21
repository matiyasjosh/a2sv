class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result, midArr = [], []
        if not mat or not mat[0]:
            return []

        m,n = len(mat), len(mat[0])

        for d in range(m+n-1):
            #we have to clear the midArr so that we know which array to reverse
            midArr.clear()
            
            r,c = 0 if d<n else d-n+1, d if d<n else n-1
            while r<m and c>-1:
                midArr.append(mat[r][c])
                r+=1
                c-=1
            
            if d%2==0:
                result.extend(midArr[::-1])
            else:
                result.extend(midArr)

        return result
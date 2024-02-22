class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletedCol = 0
        for j in range(len(strs[0])):
            check = []
            for i in range(len(strs)):
                check.append(strs[i][j])
            srtd = sorted(check)
            if srtd!=check:
                deletedCol+=1
        
        return deletedCol

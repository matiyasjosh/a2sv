class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        val = [i for i in range(1,n+1)]

        i=0
        while len(val)>1:
            i = ((i+k)-1)%len(val)
            val.pop(i)
            
        return val[0]
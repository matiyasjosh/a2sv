class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def combHelp(num):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for index in range(num, n+1):
                # take it part
                comb.append(index)
                combHelp(index + 1)
                comb.pop()

                # #leave it part
                # combHelp(index + 1)

        combHelp(1)
        return res                
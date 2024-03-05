class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        candidates.sort()
        def combHelp(i):
            x = sum(comb)
            if x == target:
                res.append(comb[:])
                return

            for index in range(i, len(candidates)):
                # take it part
                if x + candidates[i] > target:
                    return
                comb.append(candidates[index])
                combHelp(index)
                comb.pop()

        combHelp(0)
        return res   
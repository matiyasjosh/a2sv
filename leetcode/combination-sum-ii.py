class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        candidates.sort()
        def combHelp(i):
            x = sum(comb)
            if x == target:
                if comb not in res:
                    res.append(comb[:])
                return

            prev = -1
            for index in range(i, len(candidates)):
                if prev == candidates[index]:
                    continue
                # take it part
                if x + candidates[i] > target:
                    return
                comb.append(candidates[index])
                combHelp(index + 1)
                comb.pop()
                prev = candidates[index]

        combHelp(0)
        return (res)   
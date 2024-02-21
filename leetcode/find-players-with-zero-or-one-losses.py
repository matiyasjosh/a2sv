from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(lambda:[0,0])
        ans = [[],[]]
        for m in matches:
            d[m[0]][0] += 1
            d[m[1]][1] += 1
        # print(d)
        for k,v in d.items():
            # print(k , v)
            if v[1]==0:
                ans[0].append(k)
            elif v[1]==1:
                ans[1].append(k)
        ans[1].sort()
        ans[0].sort()
        return ans

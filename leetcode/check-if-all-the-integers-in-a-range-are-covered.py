class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans = set()

        for r in ranges:
            ans.update({i for i in range(r[0], r[1]+1)})
        print(ans)
        for i in range(left, right+1):
            if i not in ans:
                return False
        return True
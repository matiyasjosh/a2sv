class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        ans = [''] * len(s)

        for c in s:
            i = int(c[-1])
            n = len(c)
            ans[i - 1] = c[:n-1]

        return " ".join(ans)
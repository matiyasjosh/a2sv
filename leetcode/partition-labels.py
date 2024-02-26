class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i,c in enumerate(s)}

        anchor = j = 0
        ans = []

        for i,c in enumerate(s):
            j = max(j, last[c])
            if i==j:
                ans.append(j-anchor+1)
                anchor = i+1
        
        return ans
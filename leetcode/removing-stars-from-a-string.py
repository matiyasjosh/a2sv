class Solution:
    def removeStars(self, s: str) -> str:
        stacK=[]
        for c in s:
            if c=="*":
                stacK.pop()
            else:
                stacK.append(c)
        return "".join(stacK)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maX = 0
        i=j=0
        count={}
        while j<len(s):
            if s[j] in count:
                count[s[j]]+=1
            else:
                count[s[j]] = 1
            while count[s[j]]>1:
                count[s[i]] -= 1
                i+=1
                
            maX = max(maX, j-i+1)
            j+=1

        return maX 
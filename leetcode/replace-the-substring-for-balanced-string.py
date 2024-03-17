class Solution:
    def balancedString(self, s: str) -> int:
        k = len(s) // 4
        
        wordDict = Counter(s)

        def isBalanced(target):
            for value in wordDict.values():
                if value > target:
                    return False
            return True

        if isBalanced(k):
                return 0
        
        ans = 10 ** 5
        left = 0
        for right in range(len(s)):
            wordDict[s[right]] -= 1

            if isBalanced(k):
                ans = min(ans, right - left + 1)

                while left <= right:
                    wordDict[s[left]] += 1
                    left += 1
                    if isBalanced(k):
                        ans = min(ans, right - left + 1)
                    else:
                        break

        return ans      
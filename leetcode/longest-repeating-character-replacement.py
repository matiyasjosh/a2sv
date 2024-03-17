class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        wordDict = defaultdict(int)
        left = maxRepeating = maxC = 0

        for right in range(len(s)):
            wordDict[s[right]] += 1
            maxC = max(maxC, wordDict[s[right]])

            if (right - left + 1) - maxC > k:
                wordDict[s[left]] -= 1
                if wordDict[s[left]] == 0:
                    del wordDict[s[left]]
                left += 1
            
            maxRepeating = max(maxRepeating, right - left + 1)

        return maxRepeating
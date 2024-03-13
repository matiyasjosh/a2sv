class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = s[:k]
        maxCount = count = 0

        def isVowel(letter):
            return (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u')

        for letter in window:
            if isVowel(letter):
                count += 1

        maxCount = max(maxCount, count)

        for index in range(k, len(s)):
            if isVowel(s[index - k]):
                count -= 1
            if isVowel(s[index]):
                count += 1

            maxCount = max(maxCount, count)

        return maxCount 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        pCounter = Counter(p)
        d = Counter(s[:k])
        answer = []

        if d == pCounter:
            answer.append(0)

        for index in range(k, len(s)):
            d[s[index - k]] -= 1
            if d[s[index - k]] == 0:
                del d[s[index - k]]
            d[s[index]] += 1

            if d == pCounter:
                answer.append(index - k + 1)

        return answer
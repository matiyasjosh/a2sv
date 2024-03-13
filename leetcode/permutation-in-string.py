class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = Counter(s1)
        k = len(s1)

        s2Dict = Counter(s2[:k])

        if s1Dict == s2Dict:
            return True

        for index in range(k, len(s2)):
            s2Dict[s2[index - k]] -= 1

            if s2Dict[s2[index - k]] == 0:
                del s2Dict[s2[index - k]]

            s2Dict[s2[index]] += 1

            if s1Dict == s2Dict:
                return True

        return False
            
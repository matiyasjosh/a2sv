class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cardDict = defaultdict(int)
        minConscutive, left = 10**6, 0

        for right in range(len(cards)):
            cardDict[cards[right]] += 1

            while left < len(cards) and cardDict[cards[right]] > 1:
                minConscutive = min(minConscutive, right - left + 1)
                cardDict[cards[left]] -= 1
                left += 1
        
        return minConscutive if minConscutive != 10**6 else -1
        
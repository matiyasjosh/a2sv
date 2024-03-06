class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)

        while start <= end:
            count = 0
            med = (start + end) // 2

            for pile in piles:
                count += ceil(pile / med)
            
            if count > h:
                start = med + 1
            else:
                end = med - 1
        
        return start
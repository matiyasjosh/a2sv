class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        start, end = 0, 10**9
        houses.sort()
        heaters.sort()

        while start <= end:
            mid = (start + end) // 2
            i = j = 0
            while i < len(houses) and j < len(heaters): 
                if abs(heaters[j] - houses[i]) <= mid:
                    i += 1
                else:
                    j += 1

            if i == len(houses):
                end = mid - 1
            elif j == len(heaters):
                start = mid + 1
            
        return start

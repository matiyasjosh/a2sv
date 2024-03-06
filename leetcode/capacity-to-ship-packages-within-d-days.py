class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def dayCount(target):
            count = 1
            tot = 0
            
            for weight in weights:
                if tot + weight <= target:
                    tot += weight
                else:
                    count += 1
                    tot = weight
            return count

        start, end = max(weights), sum(weights)
        ans = 0

        while start <= end:
            mid = (start + end) // 2
            out = dayCount(mid)

            if out > days:
                start = mid + 1
            else:
                ans = mid
                end = mid - 1

        return ans
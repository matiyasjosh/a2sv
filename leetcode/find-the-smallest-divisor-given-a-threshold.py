class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def helper(m):
            return sum(ceil(num/m) for num in nums)

        start, end = 1 , max(nums)

        while start <= end:
            print(start,end)
            mid = (start + end) // 2
            if helper(mid) > threshold:
                start = mid + 1
            else:
                end = mid - 1
        
        return start

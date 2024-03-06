class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        
        if len(nums) == 2:
            return min(nums[0], nums[1])

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > ans:
                start = mid + 1
            else:
                ans = min(ans, nums[mid])
                end = mid - 1
        
        return ans
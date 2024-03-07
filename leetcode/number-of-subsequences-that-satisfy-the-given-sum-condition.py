class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        right = bisect_right(nums, target - nums[0])
        right = min(right, len(nums)-1)

        left = answer = 0
    
        while left <= right:
            if nums[left] + nums[right] <= target:
                answer = (answer + 2 ** (right - left)) % (10**9 + 7)
                left += 1
            else:
                right -= 1

        return (answer) % (10**9 + 7)



class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxSum = left = suM = 0
        d = defaultdict(int)

        for right in range(len(nums)):
            suM += nums[right]
            d[nums[right]] += 1

            while left < len(nums) and d[nums[right]] > 1:
                d[nums[left]] -= 1
                suM -= nums[left]
                left += 1

            maxSum = max(maxSum, suM)

        return maxSum
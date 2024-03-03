class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        current_sum = sum(nums[:k])

        max_avg = max(max_avg, current_sum / k)

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]

            max_avg = max(max_avg, current_sum / k)

        return max_avg
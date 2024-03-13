class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxConscutive = count = l = 0

        for r in range(len(nums)):
            count += 1 if nums[r] == 0 else 0
            while l < len(nums) and count > k:
                count -= 1 if nums[l] == 0 else 0
                l += 1

            maxConscutive = max(maxConscutive, r - l + 1)

        return maxConscutive

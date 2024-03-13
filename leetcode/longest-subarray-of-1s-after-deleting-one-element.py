class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = r = 0
        longest_subarray = 0
        l = 0

        for r in range(len(nums)):
            count += 1 if nums[r] == 0 else 0
            while l < len(nums) and count > 1:
                count -= 1 if nums[l] == 0 else 0 
                l += 1
            longest_subarray = max(longest_subarray, r - l)
            
        return longest_subarray
                     

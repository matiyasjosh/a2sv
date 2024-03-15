class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = odd = result = 0

        for right in range(len(nums)):
            odd += nums[right] % 2

            while odd > k:
                odd -= nums[left] % 2
                left += 1

            if odd == k:
                curr = left
                while nums[curr] % 2 == 0:
                    result += 1
                    curr += 1

            result += (odd == k)
             
        return result
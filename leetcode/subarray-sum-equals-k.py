class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        sum_count = {0: 1}

        for num in nums:
            sum += num
            diff = sum - k
            if diff in sum_count:
                count += sum_count[diff]
            sum_count[sum] = sum_count.get(sum, 0) + 1

        return count
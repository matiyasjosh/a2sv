class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=float('inf')
        suM=minIndex=0

        for i in range(len(nums)):
            suM+=nums[i]

            while suM>=target:
                    min_len=min(min_len, i-minIndex+1)
                    suM-=nums[minIndex]
                    minIndex+=1

        return min_len if min_len != float('inf') else 0


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0]
        prefix.append(nums[0])
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i])
        print(prefix)
        for i in range(1, len(prefix)):
            if prefix[i - 1] == (prefix[-1] - prefix[i]):
                return i - 1
        
        return -1
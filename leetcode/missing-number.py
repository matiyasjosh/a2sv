from collections import Counter
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = dict()

        for num in nums:
            d[num]=True

        for i in range(len(nums)+1):
            if i not in d:
                return i
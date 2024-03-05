class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        subset = []

        def sub(index):
            if index >= len(nums):
                return
            
            for i in range(index, len(nums)):
                subset.append(nums[i])
                res.append(subset[:])
                sub(i+1)
                subset.pop()
        sub(0)

        return res
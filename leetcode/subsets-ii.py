class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [[]], []
        nums.sort()
        
        def help(idx):
            if idx >= len(nums):
                return
            
            for index in range(idx, len(nums)):
                subset.append(nums[index])
                if subset not in res:
                    res.append(subset[:])
                help(index+1)
                subset.pop()
        
        help(0)
        return res
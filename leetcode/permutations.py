class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, perm = [], []

        def help(idx):
            if len(perm) == len(nums): 
                ans.append(perm[:])
                return
            for index in range(len(nums)):
                if nums[index] in perm:
                    continue
                perm.append(nums[index])
                help(index)
                perm.pop()

        help(0)
        return ans

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        grts = [-1]*n
        stk = []

        for i in range(2*n):
            num = nums[i%n]
            while stk and nums[stk[-1]]<num:
                grts[stk.pop()] = num
            stk.append(i%n)

        return grts
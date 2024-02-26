class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maX = 0
        for i in range(len(nums)-1):
            maX = max(maX, i+nums[i])
            if maX<=i:
                return False
        return True
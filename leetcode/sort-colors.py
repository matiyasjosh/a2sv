class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1,len(nums)):
            while i>0 and nums[i]<nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                i-=1
        
        
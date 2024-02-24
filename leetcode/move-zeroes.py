class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seek = 0

        for num in nums:
            if num!=0:
                nums[seek]=num
                seek+=1

        while seek<len(nums):
            nums[seek]=0
            seek+=1
            
        return nums
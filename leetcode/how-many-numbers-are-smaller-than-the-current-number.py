class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = nums[:]
        temp.sort()
        result = []
        for i in nums:
            result.append(temp.index(i))
        
        return result
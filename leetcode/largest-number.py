class Compare(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        
        nums.sort(key=Compare)

        if nums[0] == "0":
            return "0"

        return "".join(nums)
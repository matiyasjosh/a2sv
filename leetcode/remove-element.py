class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # Pointer for iterating through the array
        j = 0  # Pointer for placing non-val elements

        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1

        return j
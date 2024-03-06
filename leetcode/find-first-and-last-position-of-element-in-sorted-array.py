class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bsearch(nums, target, flag):
            start, end = 0, len(nums) - 1
            dval = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    dval = mid
                    if flag:
                        end = mid - 1
                    else:
                        start = mid + 1

            return dval

        left = bsearch(nums, target, True)
        right = bsearch(nums, target, False)
        return [left, right]
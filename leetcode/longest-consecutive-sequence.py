class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        lrg = 0

        for num in nums:
            if num-1 not in d:
                nexT = num+1
                while nexT in d:
                    nexT+=1
                    
                lrg = max(lrg, nexT-num)
        
        return lrg 
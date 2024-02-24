class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
            n1 = n2 = 0
            while n1<len(nums1) and n2<len(nums2):
                if nums1[n1]==nums2[n2]:
                    return nums1[n1]
                elif nums1[n1]<nums2[n2]:
                    n1+=1
                elif nums1[n1]>nums2[n2]:
                    n2+=1
            return -1
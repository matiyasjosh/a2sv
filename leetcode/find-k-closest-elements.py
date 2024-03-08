class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect_left(arr, x)
        
        
        left, right = index-1, index
        
        for _ in range(k):
            if left >= 0 and (right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x)):
                left -= 1
                
            else:
                right += 1

                
        return arr[left+1: right]
        
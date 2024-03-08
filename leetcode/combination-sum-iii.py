class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        combinations = []

        def helper(index):
            if len(combinations) == k and sum(combinations) == n:
                result.append(combinations[:])
                return
            
            if len(combinations) >= k:
                return


            for idx in range(index, 10):
                combinations.append(idx)
                helper(idx + 1)
                combinations.pop()

        
        helper(1)
        return result
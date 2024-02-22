class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score = [sum(nums)]
        r, l = sum(nums), 0

        for num in nums:
            if num==0:
                l+=1
            else:
                r-=1
            score.append(l+r)

        maX = max(score)

        return [i for i in range(len(score)) if score[i]==maX]
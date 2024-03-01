class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def predict(l,r,f:bool):
            if f:
                if l==r: return nums[l]
                lf=predict(l+1,r,not f)+nums[l]
                rt=predict(l,r-1,not f)+nums[r]
                return max(lf,rt)
            else:
                if l==r: return -nums[l]
                lf=predict(l+1,r,not f)-nums[l]
                rt=predict(l,r-1,not f)-nums[r]
                return min(lf,rt)

        return predict(0,len(nums)-1,True)>=0
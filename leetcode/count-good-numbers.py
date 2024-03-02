class Solution:
    store = {}
    def countGoodNumbers(self, n: int) -> int:
        if n==1: return 5

        if n in self.store:
            return self.store[n]

        if n%2==1:
            self.store[n] = (self.countGoodNumbers(n//2+1)*self.countGoodNumbers(n//2))%(pow(10,9)+7)
        else:
            self.store[n] =  (4*self.countGoodNumbers(n-1))%(pow(10,9)+7)

        return self.store[n]
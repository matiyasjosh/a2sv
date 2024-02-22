class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()

        while n!=1:
            n=str(n)
            suM = 0
            for i in n:
                suM+=pow(int(i),2)
            
            n = suM

            if n in d:
                return False
            
            d.add(n)

        return True
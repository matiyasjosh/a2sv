class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1
        if digits[-1]<10:
            return digits
        else:
            stack=[]
            while digits[-1]>9:    
                n = digits.pop()
                # splitting the two digit num
                while n>0:
                    stack.append(n%10)
                    n//=10
                # add the top element on last elmt of digit and check if it's greater than 9
                if len(digits)<1:
                    digits.append(stack.pop())
                else:
                    digits[-1]+=stack.pop()
                
                if digits[-1]>9: continue
                # if digit is fine then add stack to digits
                while stack:
                    digits.append(stack.pop())

            return digits
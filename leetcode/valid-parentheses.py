class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for brak in s:
            if brak in pairs:
                stack.append(brak)
            elif len(stack)==0 or brak!=pairs[stack.pop()]:
                return False
        return len(stack)==0
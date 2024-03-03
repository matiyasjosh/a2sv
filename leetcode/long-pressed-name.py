class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        og = ty = 0
        while ty<len(typed):
            if og<len(name) and name[og] == typed[ty]:
                og += 1
                ty += 1
            elif ty>0 and typed[ty] == typed[ty-1]:
                ty += 1
            else:
                return False
        
        return og == len(name)

        
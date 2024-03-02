class Solution:
    def decodeString(self, s: str) -> str:
        def decode(start,end):
            res = ""
            digit = ""
            num = count = 0
            initial = -1
            for index in range(start,end):
                if s[index].isdigit():
                    digit += s[index]
                elif s[index] =='[':
                    if count == 0:
                        num = int(digit)
                        initial = index
                    count += 1
                    digit = ""
                elif s[index] == ']':
                    count -= 1
                    if count == 0:
                        res += num* decode(initial+1,index)
                elif count == 0:
                    res += s[index]
            return res
        return decode(0,len(s))
        
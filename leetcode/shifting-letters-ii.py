class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)

        for shift in shifts:
            if shift[-1] == 0:
                prefix[shift[0]] -= 1
                prefix[shift[1] + 1] += 1
            else:
                prefix[shift[0]] += 1
                prefix[shift[1] + 1] -= 1

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i] + prefix[i - 1]

        ans = [0] * len(s)
        for i in range(len(s)):
            ans[i] = chr(ord('a') + (ord(s[i]) - ord('a') + prefix[i]) % 26)

        return ''.join(ans)
class Solution:
    def reverseWords(self, s: str) -> str:
        m = s.split()
        return ' '.join(m[::-1])
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        parent_k = (k + 1) // 2

        parentSymbol = self.kthGrammar(n - 1, parent_k)

        if k % 2 == 0:
            return 1 if parentSymbol == 0 else 0
        else:
            return parentSymbol
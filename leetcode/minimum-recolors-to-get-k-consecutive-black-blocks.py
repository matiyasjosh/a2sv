class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minRecolor = float('inf')
        window = blocks[:k]
        windowDict = Counter(window)

        minRecolor = min(minRecolor, windowDict['W'])

        for index in range(k, len(blocks)):
            windowDict[blocks[index - k]] -= 1
            windowDict[blocks[index]] += 1
            minRecolor = min(minRecolor, windowDict['W'])

        return minRecolor
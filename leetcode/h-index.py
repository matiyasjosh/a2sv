class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        start, end = -1, len(citations)

        while start + 1 < end:
            mid = (start + end) // 2

            if citations[mid] <= len(citations) - mid:
                start = mid
            else:
                end = mid

        return max(citations[start], len(citations) - end) if start != -1 else len(citations)
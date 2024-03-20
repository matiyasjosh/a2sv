class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        ans = []

        return sorted(freq, key = freq.get, reverse=True)[:k]
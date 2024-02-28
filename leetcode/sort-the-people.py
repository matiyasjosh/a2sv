class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair = zip(heights, names)
        ordered = sorted(pair,reverse=True)

        return [name for height,name in ordered]
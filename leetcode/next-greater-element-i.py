class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d= defaultdict(lambda: -1)
        stack = []

        for n in nums2:
            while stack and stack[-1]<n:
                d[stack[-1]] = n
                stack.pop()
            stack.append(n)
        return [d[n] for n in nums1]
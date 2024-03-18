class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer = ""
        left, min_length= 0, float('inf')
        ds, dt= defaultdict(int), Counter(t)
        count = len(dt)

        for right in range(len(s)):
            if s[right] in dt:
                ds[s[right]] += 1
                if ds[s[right]] == dt[s[right]]:
                    count -= 1
            
            while count == 0:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    answer = s[left:right+1]
                
                if s[left] in ds:
                    ds[s[left]] -= 1
                    if ds[s[left]] < dt[s[left]]:
                        count += 1
                left += 1

        return answer

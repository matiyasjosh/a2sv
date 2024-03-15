class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = suM = 0
        frequency = [0] * k
        frequency[0] = 1

        for num in nums:
            suM += num
            remainder = suM % k
            # if remainder < 0:
            #     remainder += k
            count += frequency[remainder]
            frequency[remainder] += 1

        return count
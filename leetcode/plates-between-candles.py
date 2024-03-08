class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        for i, char in enumerate(s):
            if char == '|':
                candles.append(i)

        if len(candles) == 0:
            return [0]

        print(candles)

        # here we used prefix sum so that we can know the numbers
        prefixSum = [0] * len(s)
        count = 0
        for i in range(len(s)):
            if s[i] != '|':
                prefixSum[i] = count + 1
                count += 1
            else:
                prefixSum[i] = count
        
        print(prefixSum)

        answer = []
        for left, right in queries:
            left_candle_idx = min(bisect_left(candles, left), len(candles) - 1)
            right_candle_idx = min(bisect_right(candles, right), len(candles)) 
            print(left_candle_idx, right_candle_idx)

            rightSum = prefixSum[candles[right_candle_idx - 1]] if right_candle_idx != left_candle_idx else prefixSum[candles[right_candle_idx]]
            leftSum = prefixSum[candles[left_candle_idx]]  
            print(rightSum, leftSum)
            count = rightSum - leftSum

            answer.append(count)
        
        return answer


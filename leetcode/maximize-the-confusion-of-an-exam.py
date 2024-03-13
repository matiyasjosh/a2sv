class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = maxConfusion = cnt_t = cnt_f = 0

        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                cnt_t += 1
            else:
                cnt_f += 1

            while min(cnt_t, cnt_f) > k:
                if answerKey[left] == 'T':
                    cnt_t -= 1
                else:
                    cnt_f -= 1
                left += 1

            maxConfusion = max(maxConfusion, right - left + 1)

        return maxConfusion
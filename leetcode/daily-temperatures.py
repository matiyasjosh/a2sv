class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stAck=[]
        ans=[0]*len(temperatures)
        for t in range(len(temperatures)):
            while stAck and temperatures[stAck[-1]]<temperatures[t]:
                ans[stAck[-1]] = t - stAck[-1]
                stAck.pop()

            stAck.append(t)
        return ans

    
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        d = deque(tickets)
        f, time = k, 0

        while d and d[f]!=0:
            sub = d.popleft()
            if sub!=0:
                time+=1
                d.append(sub-1)
            f-=1
            if f<0: 
                f=len(d)-1
 

        return time
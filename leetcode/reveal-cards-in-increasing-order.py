class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q, ans = deque(i for i in range(len(deck))), [0]*len(deck)
        
        for d in deck:
            ans[q.popleft()] = d
            if len(q)>1:
                q.append(q.popleft())

        return ans



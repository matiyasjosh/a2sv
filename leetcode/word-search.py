class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        bk,fw,up,dw = False,False,False,False
        words = list(word)
        path = []
        pos = set()

        def backTrack(i,j):
            nonlocal bk,fw,up,dw

            if ( bk or fw or up or dw):
                return True
            if path and path[-1] != words[len(path)-1]:
                return 

            if (i,j) not in pos and i < len(board) and j<len(board[0]):
                path.append(board[i][j])
                pos.add((i,j))

                if words == path:
                    return True


                if i>0 and (i-1 ,j ) not in pos:
                    up = backTrack(i-1,j)
        
                if j>0 and (i ,j-1 ) not in pos:
                    bk = backTrack(i,j-1) 

                if i<len(board) and (i+1,j ) not in pos:
                    fw = backTrack(i+1,j)

                if j<len(board[0]) and (i,j+1 ) not in pos:
                    dw = backTrack(i,j+1)
                
                path.pop()
                pos.remove((i,j))

            return ( bk or fw or up or dw)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if backTrack(i,j):
                    return True
        
        return False
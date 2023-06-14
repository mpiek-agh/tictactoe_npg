import random
import copy

class AI:
    def __init__(self, round=0, player=0) -> None:
        self.round = round

    def emptyField(self, COL, ROW, board) -> int:
        #nie wiem czy to działa
        empty = []
        for i in range(COL):
            for j in range(ROW):
                if board[i][j]:
                    empty.append((i,j))
        
        return empty


    def randMove(self, board,):
        emptyF = board.emptyField()
        ind = random.randrange(0, len(emptyF), 1)

        return emptyF[ind]    #krotka (kol, wiersz)
    
    def minimax(self, board, maximizing): 
        case = board.termination()  #funkcja kończąca gre po zwycięstwie lub remisie
        
        #wygrywa gracz 1
        if case == 1:
            return 1, None
        #wygrywa gracz 2
        if case == 2:
            return -1, None
        else:
            return 0, None
        
        
        if maximizing:
            pass
        
        elif not maximizing:
            mini = 2
            favMove = None
            emptyFiled = board.emptyField()

            for (i,j) in emptyField:
                tab = copy.deepcopy(board)
                tab.symbol(i, j, player)  #funkcja wstawiająca znak
                game = self.minimax(tab, True)[0]


    def game(self, board):
        if self.round == 0:
            #losowy ruch
            move = self.randMove(board)
        else:
            #minimax
            self.minimax(board, False)
    
        return move

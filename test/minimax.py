import random
import copy
from src.game import Game

class AI:
    def __init__(self, round=1, player=2):
        self.round = round
        self.round = player

    def game(self, board):
        if self.round == 0:
            #losowy ruch
            eval = 'random'
            move = self.randMove(board)
        else:
            #minimax
            game, move = self.minimax(board, False)

        print(f'AI chosen {move}')
    
        return move

    def randMove(self, board):
        emptyF = self.emptyField()
        ind = random.randrange(0, len(emptyF))

        return emptyF[ind]    #krotka (kol, wiersz)

    def emptyField(self, COL, ROW, board):
        #nie wiem czy to działa
        empty = []
        for col in range(COL):
            for row in range(ROW):
                if board[col][row] == ' ':
                    empty.append((col,row))
        
        return empty
    
    def minimax(self, board, maximizing): 
        case = Game.termination()  #funkcja kończąca gre po zwycięstwie lub remisie
        
        #wygrywa gracz 1
        if case == 1:
            return 1, None
        #wygrywa gracz 2
        if case == 2:
            return -1, None
        #remis
        else:
            return 0, None
        
        
        if maximizing:
            maxi = -2
            favMove = None
            emptyFiled = board.emptyField()

            for (i, j) in emptyField:
                tab = copy.deepcopy(board)
                tab = Game.place(i, j)
                game = self.minimax(tab, False)[0]
                if game > maxi:
                    maxi = game
                    favMove = (i, j)
            
            return maxi, favMove
        
        elif not maximizing:
            mini = 2
            favMove = None
            emptyFiled = board.emptyField()

            for (i, j) in emptyField:
                tab = copy.deepcopy(board)
                tab = Game.palce(i, j)
                game = self.minimax(tab, True)[0]
                if game < mini:
                    mini = game
                    favMove = (i, j)
            
            return mini, favMove


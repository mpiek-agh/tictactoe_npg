import random
import copy
from src import Board

class AI:
    def __init__(self, board_size, starting_player, player) -> None:
        self.board_size = board_size
        

    def minimax(self, board, is_maximizning):
        result = self.board.win_check()
        maxi = -2
        favMove = None
        emptyField = self.board.get_free()

        for (i, j) in emptyField:
            tab = copy.deepcopy(board)
            tab = board.place(i, j)
            game = self.minimax(tab, False)[0]
            if game > maxi:
                maxi = game
                favMove = (i, j)
            
        return maxi, favMove
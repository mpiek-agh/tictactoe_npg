from random import randint
from pprint import pp

from src.program_state import ProgramState
from src.board import Board


class Game(ProgramState):
    def __init__(self, board_size, player1, player2, first_player=False):
        self.board_size = board_size
        self.players = (player1, player2)

        # Jeżeli gracz, który ma wykonać pierwszy ruch nie został podany to jest wybierany losowo
        self.curent_player = first_player if first_player else randint(0, 1)

        self.board = Board(self.board_size)

    def player(self):
        # zwraca gracza do którego należy tura
        return self.player[self.curent_player]

    def adv_player(self):
        # zamienia gracza do którego należy tura
        self.curent_player = (self.curent_player + 1) % 2

    def loop(self, scr):
        pass

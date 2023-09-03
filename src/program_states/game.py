from random import randint
import curses
from enum import Enum

from src import ProgramState, Board


class GameState(Enum):
    # stany gry
    MOVE = 1    # gracz wykonuje ruch
    CONFIRM = 2  # gracz potwierdza lub cofa ruch
    END = 3     # gra zakończona


class GameResult(Enum):
    # wyniki gry
    WIN = 1  # wygrana
    TIE = 2  # remis


class Game(ProgramState):
    def __init__(self, board_size, starting_player, undoes, player1, player2):
        self.board_size = board_size
        self.starting_player = starting_player
        self.undoes = undoes
        self.players = [player1, player2]
        self.symbols = [' ', player1.symbol, player2.symbol]

        # Jeżeli gracz, który ma wykonać pierwszy ruch nie został podany to jest wybierany losowo
        self.current_player = self.starting_player if self.starting_player > 0 else randint(
            0, 1)

        self.tui_color = self.players[self.current_player].color

        self.board = Board(self.board_size)

        self.game_state = GameState.MOVE
        self.game_result = GameResult.WIN

        self.board_selection = [0, 0]  # wybór pola na planszy
        self.selection = 0  # wybór pozycji w menu

    def player(self):
        # zwraca gracza do którego należy tura
        return self.players[self.current_player]

    def adv_player(self):
        # zamienia gracza do którego należy tura
        self.current_player = (self.current_player + 1) % 2
        self.tui_color = self.players[self.current_player].color

    def loop(self, scr):
        self.draw(scr)

        while True:
            c = scr.getch()
            if c == ord("q"):
                return "menu", [], {}
            elif c in (ord(" "), ord("\n")):
                if self.game_state == GameState.END:
                    return "menu", [], {}

                elif self.game_state == GameState.CONFIRM:
                    if self.selection == 0:
                        self.game_state = GameState.MOVE

                        winner = self.board.win_check()
                        new_position = self.board.get_random_free()

                        if winner:
                            self.game_result = GameResult.WIN
                            self.game_state = GameState.END
                            self.tui_color = self.players[winner-1].color
                        elif not new_position:
                            self.game_result = GameResult.TIE
                            self.game_state = GameState.END
                            self.tui_color = 1

                        self.board_selection = new_position
                        self.adv_player()

                    if self.selection == 1:
                        pass

                elif self.game_state == GameState.MOVE:
                    if self.board.place(self.board_selection[0], self.board_selection[1], self.current_player+1):
                        self.board.place(
                            self.board_selection[0], self.board_selection[1], self.player())
                        self.game_state = GameState.CONFIRM

                self.draw(scr)
            elif c in (curses.KEY_DOWN, ord("s"), ord("j")):
                if self.game_state == GameState.MOVE:
                    self.board_selection[1] = (
                        self.board_selection[1]+1) % self.board_size
                self.draw(scr)
            elif c in (curses.KEY_UP, ord("w"), ord("k")):
                if self.game_state == GameState.MOVE:
                    self.board_selection[1] = (
                        self.board_selection[1]-1) % self.board_size
                self.draw(scr)
            elif c in (curses.KEY_LEFT, ord("a"), ord("h")):
                if self.game_state == GameState.MOVE:
                    self.board_selection[0] = (
                        self.board_selection[0]-1) % self.board_size
                elif self.game_state == GameState.CONFIRM:
                    self.selection = (self.selection-1) % 2
                self.draw(scr)
            elif c in (curses.KEY_RIGHT, ord("d"), ord("l")):
                if self.game_state == GameState.MOVE:
                    self.board_selection[0] = (
                        self.board_selection[0]+1) % self.board_size
                elif self.game_state == GameState.CONFIRM:
                    self.selection = (self.selection+1) % 2
                self.draw(scr)

    def draw(self, scr):
        scr.clear()
        self.tui_template(scr)

        scr.addstr(1, 2, '                 ',
                   curses.color_pair(self.tui_color))
        scr.addstr(2, 2, '  Standard game  ',
                   curses.color_pair(self.tui_color))
        scr.addstr(3, 2, '                 ',
                   curses.color_pair(self.tui_color))

        if self.current_player == 0:
            scr.addstr(1, 21, self.players[0].name,
                       curses.color_pair(self.tui_color))
            scr.addstr(3, 21, self.players[1].name, curses.color_pair(0))
        else:
            scr.addstr(1, 21, self.players[0].name, curses.color_pair(0))
            scr.addstr(3, 21, self.players[1].name,
                       curses.color_pair(self.tui_color))

        self.draw_board(scr, 2, 9)

        if self.game_state == GameState.CONFIRM:
            scr.addstr(6, 2, "  confirm  ", curses.color_pair(
                self.tui_color) | curses.A_BLINK if self.selection == 0 else curses.color_pair(1))
            scr.addstr(6, 15, "  undo  ", curses.color_pair(self.tui_color) |
                       curses.A_BLINK if self.selection == 1 else curses.color_pair(1))

        elif self.game_state == GameState.END:
            message = "  TIE  " if self.game_result == GameResult.TIE else f"  {self.player().name.upper()} WON  "

            scr.addstr(6, 2, message, curses.color_pair(self.tui_color))
            scr.addstr(6, 4+len(message), "  exit  ",
                       curses.color_pair(self.tui_color) | curses.A_BLINK)

        scr.refresh()

    def draw_board(self, scr, x_pos, y_pos):
        for y in range(self.board_size):
            for x in range(self.board_size):
                color = curses.color_pair(1)
                if y == self.board_selection[1] and x == self.board_selection[0] and self.game_state == GameState.MOVE:
                    color = curses.color_pair(self.tui_color) | curses.A_BLINK
                elif y == self.board_selection[1] and x == self.board_selection[0] and self.game_state == GameState.CONFIRM:
                    color = curses.color_pair(self.tui_color)

                scr.addstr(y_pos+y*4, x_pos+x*9, "       ", color)
                scr.addstr(y_pos+y*4+1, x_pos+x*9,
                           f"   {self.symbols[self.board(x,y)]}   ", color)
                scr.addstr(y_pos+y*4+2, x_pos+x*9, "       ", color)

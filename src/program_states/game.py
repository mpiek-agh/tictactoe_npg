from random import randint
import curses
from enum import Enum

from src import ProgramState, Board


class GameState(Enum):
    # stany gry
    MOVE = 1  # gracz wykonuje ruch
    CONFIRM = 2  # gracz potwierdza lub cofa ruch
    END = 3  # gra zakończona


class GameResult(Enum):
    # wyniki gry
    WIN = 1  # wygrana
    TIE = 2  # remis


class Game(ProgramState):
    def __init__(self, board_size, starting_player, player1, player2):
        self.board_size = board_size
        self.starting_player = starting_player
        self.players = [player1, player2]
        self.symbols = [" ", player1.symbol, player2.symbol]
        self.undoes = [player1.undoes, player2.undoes]

        # Jeżeli gracz, który ma wykonać pierwszy ruch nie został podany to jest wybierany losowo
        self.current_player = (self.starting_player if self.starting_player > 0 else randint(0, 1))

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
                            self.tui_color = self.players[winner - 1].color
                        elif not new_position:
                            self.game_result = GameResult.TIE
                            self.game_state = GameState.END
                            self.tui_color = 1
                        else:
                            self.board_selection = new_position
                            self.adv_player()

                    elif self.selection == 1:
                        if self.undoes[self.current_player] == 0:
                            pass
                        else:
                            self.board.remove(self.board_selection[0], self.board_selection[1])
                            self.undoes[self.current_player] = self.undoes[self.current_player] - 1
                            self.game_state = GameState.MOVE
                        
                elif self.game_state == GameState.MOVE:
                    if self.board.place(self.board_selection[0], self.board_selection[1], self.current_player + 1):
                        self.game_state = GameState.CONFIRM

                self.draw(scr)
            elif c in (curses.KEY_DOWN, ord("s"), ord("j")):
                if self.game_state == GameState.MOVE:
                    self.board_selection[1] = (self.board_selection[1] + 1) % self.board_size
                self.draw(scr)
            elif c in (curses.KEY_UP, ord("w"), ord("k")):
                if self.game_state == GameState.MOVE:
                    self.board_selection[1] = (self.board_selection[1] - 1) % self.board_size
                self.draw(scr)
            elif c in (curses.KEY_LEFT, ord("a"), ord("h")):
                if self.game_state == GameState.MOVE:
                    self.board_selection[0] = (self.board_selection[0] - 1) % self.board_size
                elif self.game_state == GameState.CONFIRM:
                    self.selection = (self.selection - 1) % 2
                self.draw(scr)
            elif c in (curses.KEY_RIGHT, ord("d"), ord("l")):
                if self.game_state == GameState.MOVE:
                    self.board_selection[0] = (self.board_selection[0] + 1) % self.board_size
                elif self.game_state == GameState.CONFIRM:
                    self.selection = (self.selection + 1) % 2
                self.draw(scr)

    def draw(self, scr):
        scr.clear()

        self.draw_header(scr, "Standard Game", 2, 1)
        self.draw_player_names(scr, 21, 1)
        self.draw_confirm_buttons(scr, 2, 6)
        self.draw_end_message(scr, 2, 6)
        self.draw_board(scr, 2, 9)

        self.tui_template(scr)

        scr.refresh()

    def draw_confirm_buttons(self, scr, x, y):
        if self.game_state == GameState.CONFIRM:
            scr.addstr(y, x, "  confirm  ", curses.color_pair(self.tui_color) | curses.A_BLINK if self.selection == 0 else curses.color_pair(1))
            if self.undoes[self.current_player] == 0:
                scr.addstr(y, x+13, "  undo  ", curses.color_pair(self.tui_color) | curses.A_BLINK if self.selection == 1 else curses.color_pair(1))
                scr.addstr(" - you can't undo")
            else:
                scr.addstr(y, x+13, "  undo  ", curses.color_pair(self.tui_color) | curses.A_BLINK if self.selection == 1 else curses.color_pair(1))
                scr.addstr(f" - you have {self.undoes[self.current_player]} undoes")

    def draw_end_message(self, scr, x, y):
        if self.game_state == GameState.END:
            message = ("  TIE  " if self.game_result == GameResult.TIE else f"  {self.player().get_name()} WON  ")

            scr.addstr(y, x, message, curses.color_pair(self.tui_color))
            scr.addstr(y, x + 2 + len(message), "  exit  ", curses.color_pair(self.tui_color) | curses.A_BLINK)

    def draw_header(self, scr, header, x, y):
        scr.addstr(y, x, " "*(len(header)+4), curses.color_pair(self.tui_color))
        scr.addstr(y+1, x, f"  {header}  ", curses.color_pair(self.tui_color))
        scr.addstr(y+2, x, " "*(len(header)+4), curses.color_pair(self.tui_color))

    def draw_player_names(self, scr, x, y):
        scr.addstr(y, x, self.players[0].get_name(), curses.color_pair(0 if self.current_player else self.tui_color))
        scr.addstr(y+2, x, self.players[1].get_name(), curses.color_pair(0 if not self.current_player else self.tui_color))

    def draw_board(self, scr, x_pos, y_pos):
        for y in range(self.board_size):
            for x in range(self.board_size):
                color = curses.color_pair(1)
                if (y == self.board_selection[1] and x == self.board_selection[0] and self.game_state == GameState.MOVE):
                    color = curses.color_pair(self.tui_color) | curses.A_BLINK
                elif (y == self.board_selection[1] and x == self.board_selection[0] and self.game_state == GameState.CONFIRM):
                    color = curses.color_pair(self.tui_color)

                scr.addstr(y_pos + y * 4, x_pos + x * 9, "       ", color)
                scr.addstr(y_pos + y * 4 + 1, x_pos + x * 9, f"   {self.symbols[self.board(x,y)]}   ", color,)
                scr.addstr(y_pos + y * 4 + 2, x_pos + x * 9, "       ", color)

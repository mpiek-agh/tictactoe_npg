from random import randint
import curses
from time import time

from src.program_states import GameState, GameResult, Game


class TimeGame(Game):
    def __init__(self, board_size, starting_player, player1, player2):
        super().__init__(board_size, starting_player, 0, player1, player2)

    def loop(self, scr):
        self.draw(scr)

        elapsed_time = time()

        while True:
            c = scr.getch()
            if c == ord("q"):
                return "menu", [], {}
            elif c in (ord(" "), ord("\n")):
                if self.game_state == GameState.END:
                    return "menu", [], {}

                if self.board.place(self.board_selection[0], self.board_selection[1], self.current_player + 1):
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


            if self.game_state == GameState.MOVE:
                new_elapsed_time = time()
                self.player().time -= new_elapsed_time - elapsed_time
                elapsed_time = new_elapsed_time

                if self.player().time <= 0:
                    self.player().time = 0
                    self.game_state = GameState.END
                    self.game_result = GameResult.WIN
                    self.adv_player()
                    self.draw(scr)

            self.draw_player_times(scr, 16, 1)

    def draw(self, scr):
        scr.clear()

        self.draw_header(scr, "Time Game", 2, 1)
        self.draw_player_names(scr, 25, 1)
        self.draw_end_message(scr, 2, 6)
        self.draw_board(scr, 2, 9)

        self.tui_template(scr)

        scr.refresh()

    def draw_player_times(self, scr, x, y):
        scr.addstr(y, x, f" {self.players[0].time:.2f} ", curses.color_pair(0 if self.current_player else self.tui_color))
        scr.addstr(y+2, x, f" {self.players[1].time:.2f} ", curses.color_pair(0 if not self.current_player else self.tui_color))
        self.clear_cursor(scr)
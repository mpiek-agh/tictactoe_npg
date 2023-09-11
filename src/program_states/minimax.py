import random
import copy
from src import Board
from src.program_states import GameState, GameResult, Game
import curses

from src.scoreboard_managment import update_scoreboard

class AI(Game):
    def __init__(self, board_size, starting_player, player, computer, level=1) -> None:
        self.board_size = board_size
        self.board = Board(board_size)
        super().__init__(board_size, starting_player, 0, player, computer)

        self.level = level

    def random_move(self):
        empty_field = self.board.get_free()
        index = random.randrange(0, len(empty_field))
        return empty_field[index]

    def minimax(self, board, is_maximizning):
        result = self.board.win_check()
        
        if result == 1:
            return 1
        elif result == 2:
            return 2
        elif result != 1 or result != 2:
            return 0


        if is_maximizning:
            max_eval = -100
            best_move = None
            empty_field = self.board.get_free()

            for [x, y] in empty_field:
                test_board = Board(copy.deepcopy(board)) 
                test_board.place(x, y, self.adv_player())
                evaluation = self.minimax(test_board, False)[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = [x, y]

            return best_move
        
        elif not is_maximizning:
            min_eval = 100
            best_move = None
            empty_field = self.board.get_free()

            for [x, y] in empty_field:
                test_board = Board(copy.deepcopy(board)) 
                test_board.place(x, y, self.adv_player())
                evaluation = self.minimax(test_board, True)[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = [x, y]

            return best_move


    def evaluation(self, board):
        if self.level == 0:
            move = self.random_move(board)
        
        else:
            move = self.minimax(board, False)
        
        return move

    def loop(self, scr):
        self.draw(scr)

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
                        update_scoreboard(self.player().name, 'win_computer')
                    elif not new_position:
                        self.game_result = GameResult.TIE
                        self.game_state = GameState.END
                        self.tui_color = 1
                    else:
                        self.board_selection = new_position
                        self.adv_player()    

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

        self.draw_header(scr, "Game with computer", 2, 1)
        self.draw_player_names(scr, 25, 1)
        self.draw_end_message(scr, 2, 6)
        self.draw_board(scr, 2, 9)

        self.tui_template(scr)

        scr.refresh()

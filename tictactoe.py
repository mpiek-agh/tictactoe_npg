from src.game import Game
from src.menu import Menu
import curses


class Tictactoe:
    def __init__(self):
        self.program_states = {
            "game": Game,
            'menu': Menu,
            "quit": None
            # Do implementacji
            # 'game_setup': None,
            # 'game_time': None,
            # 'scoreboard': None,
            # 'players': None,
            # 'add_player': None,
        }

        self.program_state = "menu"

    def loop(self, scr):
        self.curses_init(scr)

        state_args = ()
        state_kwargs = {}

        while True:
            if self.program_state == "quit":
                return

            state = self.program_states[self.program_state](*state_args, **state_kwargs)
            self.program_state, state_args, state_kwargs = state.loop(scr)

    def curses_init(self,scr):
        scr.clear()
        scr.refresh()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_MAGENTA)


def main():
    tictactoe = Tictactoe()
    curses.wrapper(tictactoe.loop)

    # game = Game(5, '%', '@')
    # game.place(0,0)
    # game.adv_player()
    # game.place(4,4)
    # game.adv_player()
    # game.place(3,3)
    # game.print_board()


if __name__ == "__main__":
    main()

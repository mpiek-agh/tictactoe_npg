import curses

from src.program_states.game import Game
from src.program_states.menu import Menu
from src.program_states.help import Help
from src.program_states.game_setup import GameSetup
from src.program_states.minimax import AI
from src.program_states.time_game_setup import TimeGameSetup


class Tictactoe:
    def __init__(self):
        self.program_states = {
            "game": Game,
            "menu": Menu,
            "help": Help,
            "quit": None,
            "game_setup": GameSetup,
            "with_computer": AI,
            'time_game_setup': TimeGameSetup,
            # Do implementacji
            # 'scoreboard': None,
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

            state = self.program_states[self.program_state](
                *state_args, **state_kwargs)
            self.program_state, state_args, state_kwargs = state.loop(scr)

    def curses_init(self, scr):
        scr.clear()
        scr.refresh()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLUE)
        curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_YELLOW)


def main():
    tictactoe = Tictactoe()
    curses.wrapper(tictactoe.loop)


if __name__ == "__main__":
    main()

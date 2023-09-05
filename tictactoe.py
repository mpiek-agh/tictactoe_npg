import curses

from src.program_states import Game, GameSetup, Help, Menu, TimeGameSetup, AI, TimeGame


class Tictactoe:
    def __init__(self):
        self.program_states = {
            "quit": None,
            "menu": Menu,
            "help": Help,

            "game_setup": GameSetup,
            "game": Game,

            'time_game_setup': TimeGameSetup,
            'time_game': TimeGame,

            "with_computer": AI,
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

            state = self.program_states[self.program_state](*state_args, **state_kwargs)
            self.program_state, state_args, state_kwargs = state.loop(scr)

    def curses_init(self, scr):
        scr.clear()
        scr.refresh()
        scr.nodelay(True)

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

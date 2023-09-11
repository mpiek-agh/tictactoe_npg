import curses

from src.program_states import Game, GameSetup, Help, Menu, TimeGameSetup, MinimaxSetup, TimeGame, AI, Scoreboard


class Tictactoe:
    def __init__(self):
        # stany programu (ekrany, widoki)
        # identyfikator: klasa realizująca stan
        self.program_states = {
            "quit": None, # powoduje wyłączenie programu
            "menu": Menu,
            "help": Help,

            "game_setup": GameSetup,
            "game": Game,

            'time_game_setup': TimeGameSetup,
            'time_game': TimeGame,

            "computer_game_setup": MinimaxSetup,
            "with_computer": AI,

            "scoreboard": Scoreboard
        }

        # stan domyślny aktywowany po uruchomieniu programu
        self.program_state = "menu"

    def loop(self, scr):
        self.curses_init(scr)

        state_args = ()
        state_kwargs = {}


        try:
            while True:
                if self.program_state == "quit":
                    return

                # utworzenie klasy stanu z zapewnionymi przez poprzedni stan parametrami
                state = self.program_states[self.program_state](*state_args, **state_kwargs)

                # id kolejnego stanu, argumenty pozycyjne, argumenty nazwane
                self.program_state, state_args, state_kwargs = state.loop(scr)
        except curses.error:
            curses.echo()
            curses.nocbreak()
            curses.endwin()
            print("Your terminal is too small. Make the window bigger or use a smaller font.")

    def curses_init(self, scr):
        scr.clear()
        scr.refresh()
        scr.nodelay(True)

        curses.start_color()

        # definicje kolorów - identyfikowane za pomocą liczby podanej w pierwszym argumencie
        # id o wartości 0 to biała czcionka bez tła
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

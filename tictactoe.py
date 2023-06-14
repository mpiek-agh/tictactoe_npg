from src.game import Game


class Tictactoe:
    def __init__(self):
        self.program_states = {
            "game": Game,
            "quit": None
            # Do implementacji
            # 'menu': None,
            # 'game_setup': None,
            # 'game_time': None,
            # 'scoreboard': None,
            # 'players': None,
            # 'add_player': None,
        }

        self.program_state = "game"

    def loop(self):
        state_args = ()
        state_kwargs = {}

        while True:
            if self.program_state == "quit":
                return

            state = self.program_states[self.program_state](*state_args, **state_kwargs)
            self.program_state, state_args, state_kwargs = state.loop()


def main():
    # tictactoe = Tictactoe()
    # tictactoe.loop()

    game = Game(5, '%', '@')
    game.place(0,0)
    game.adv_player()
    game.place(4,4)
    game.adv_player()
    game.place(3,3)
    game.print_board()


if __name__ == "__main__":
    main()

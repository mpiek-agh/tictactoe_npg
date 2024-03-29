import curses

from src.program_states import GameSetup
from src import Player

class MinimaxSetup(GameSetup):
    def __init__(self):
        super().__init__()

        self.menu_entries = [
            ["board_size", (("3x3", 3), ("4x4", 4), ("5x5", 5), ("6x6", 6)), 4, 0],
            ["starting_player", (("1", 0), ("computer", 1), ("Random", -1)), 7, 2],

            ["computer_symbol", (("X", "X"), ("O", "O"), ("#", "#"), ("$", "$"), ("%", "%"), ("&", "&"), ("M", "M"), ("W", "W"),), 10, 0],

            ["player_name", [["Name", "Player name"]], 13, 0, str],
            ["player_symbol", (("X", "X"), ("O", "O"), ("#", "#"), ("$", "$"), ("%", "%"), ("&", "&"), ("M", "M"), ("W", "W"),), 14, 0],
            ["player_color", (("Cyan", 2), ("Magenta", 3), ("Blue", 4), ("Green", 5), ("Red", 6), ("Yellow", 7),), 15, 1],

            ["play", (("Play", None),), 17, 0],
        ]

        self.next_state = "with_computer"
        self.confirm_entry = 6
    
    def get_loop_return(self):
        player = Player(self.entry_value(3), self.entry_value(4), self.entry_value(5))
        computer = Player("computer", self.entry_value(2), self.entry_value(5))
        return (self.entry_value(0), self.entry_value(1), player, computer)

    def draw_headers(self, scr):
        scr.addstr(1, 2, "  Game with computer  ", curses.color_pair(2))
        scr.addstr(3, 2, "Board size", curses.color_pair(1))
        scr.addstr(6, 2, "Starting player", curses.color_pair(1))
        scr.addstr(9, 2, "Computer", curses.color_pair(1))
        scr.addstr(12, 2, "Player", curses.color_pair(1))

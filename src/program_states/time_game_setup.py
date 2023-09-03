import curses

from src.program_states import GameSetup


class TimeGameSetup(GameSetup):
    def __init__(self):
        super().__init__()

        # Klucz, pozycje w subsekcji z wartościami, wiersz w TUI, wybór
        self.menu_entries = [
            [
                "board_size",
                (("3x3", 3), ("4x4", 4), ("5x5", 5), ("6x6", 6)),
                4,
                0,
            ],
            [
                "starting_player",
                (("1", 0), ("2", 1), ("Random", -1)),
                7,
                2,
            ],
            [
                "time",
                (
                    ("30s", 30),
                    ("60s", 60),
                    ("75s", 75),
                    ("90s", 90),
                    ("105s", 105),
                    ("120s", 120),
                ),
                10,
                1,
            ],
            ["player1_name", [["Name", "Player 1 name"]], 13, 0, str],
            [
                "player1_symbol",
                (
                    ("X", "X"),
                    ("O", "O"),
                    ("#", "#"),
                    ("$", "$"),
                    ("%", "%"),
                    ("&", "&"),
                    ("M", "M"),
                    ("W", "W"),
                ),
                14,
                1,
            ],
            [
                "player1_color",
                (
                    ("Cyan", 2),
                    ("Magenta", 3),
                    ("Blue", 4),
                    ("Green", 5),
                    ("Red", 6),
                    ("Yellow", 7),
                ),
                15,
                1,
            ],
            ["player2_name", [["Name", "Player 2 name"]], 18, 0, str],
            [
                "player2_symbol",
                (
                    ("X", "X"),
                    ("O", "O"),
                    ("#", "#"),
                    ("$", "$"),
                    ("%", "%"),
                    ("&", "&"),
                    ("M", "M"),
                    ("W", "W"),
                ),
                19,
                1,
            ],
            [
                "player2_color",
                (
                    ("Cyan", 2),
                    ("Magenta", 3),
                    ("Blue", 4),
                    ("Green", 5),
                    ("Red", 6),
                    ("Yellow", 7),
                ),
                20,
                2,
            ],
            ["play", (("Play", None),), 22, 0],
        ]

        self.next_state = "time_game"

    def draw_headers(self, scr):
        scr.addstr(1, 2, "  Time game  ", curses.color_pair(2))
        scr.addstr(3, 2, "Board size", curses.color_pair(1))
        scr.addstr(6, 2, "Starting player", curses.color_pair(1))
        scr.addstr(9, 2, "Time", curses.color_pair(1))
        scr.addstr(12, 2, "Player 1", curses.color_pair(1))
        scr.addstr(17, 2, "Player 2", curses.color_pair(1))

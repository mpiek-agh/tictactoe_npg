import curses

from src.program_state import ProgramState


class GameSetup(ProgramState):
    def __init__(self):
        # Klucz, pozycje w subsekcji z wartościami, wiersz w TUI, wybór
        self.menu_entries = [
            [
                "board_size",
                (("3x3", 3), ("4x4", 4), ("5x5", 5), ("6x6", 6), ("7x7", 7)),
                4,
                0,
            ],
            ["player1_name", [["Name", "Player 1 name"]], 7, 0, str],
            [
                "player1_character",
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
                8,
                0,
            ],
            [
                "player1_color",
                (
                    ("White", 1),
                    ("Cyan", 2),
                    ("Magenta", 3),
                    ("Blue", 4),
                    ("Green", 5),
                    ("Red", 6),
                    ("Yellow", 7),
                ),
                9,
                0,
            ],
            ["player2_name", [["Name", "Player 2 name"]], 12, 0, str],
            [
                "player2_character",
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
                13,
                0,
            ],
            [
                "player2_color",
                (
                    ("White", 1),
                    ("Cyan", 2),
                    ("Magenta", 3),
                    ("Blue", 4),
                    ("Green", 5),
                    ("Red", 6),
                    ("Yellow", 7),
                ),
                14,
                0,
            ],
            ["play", (("Play", None),), 16, 0],
        ]

        self.selection = 0

    def loop(self, scr):
        self.draw(scr)

        while True:
            c = scr.getch()
            if c == ord("q"):
                return "menu", [], {}
            elif c in (ord(" "), ord("\n")):
                if self.menu_entries[self.selection][-1] is str:
                    self.menu_entries[self.selection][1][0][1] = ""
                    self.draw(scr)
                    scr.nodelay(False)
                    curses.echo()
                    curses.curs_set(1)
                    self.menu_entries[self.selection][1][0][1] = scr.getstr(
                        self.menu_entries[self.selection][2], 2, 20
                    )

                    scr.nodelay(True)
                    curses.noecho()
                    curses.curs_set(0)

                elif self.selection == 7:
                    setup = {
                        entry[0]: entry[1][entry[3]][1] for entry in self.menu_entries
                    }
                    return "game", [], setup

                self.selection = (self.selection + 1) % len(self.menu_entries)
                self.draw(scr)

            elif c in (curses.KEY_DOWN, ord("s"), ord("j")):
                self.selection = (self.selection + 1) % len(self.menu_entries)
                self.draw(scr)
            elif c in (curses.KEY_UP, ord("w"), ord("k")):
                self.selection = (self.selection - 1) % len(self.menu_entries)
                self.draw(scr)
            elif c in (curses.KEY_LEFT, ord("a"), ord("h")):
                self.menu_entries[self.selection][3] = (
                    self.menu_entries[self.selection][3] - 1
                ) % len(self.menu_entries[self.selection][1])
                self.draw(scr)
            elif c in (curses.KEY_RIGHT, ord("d"), ord("l")):
                self.menu_entries[self.selection][3] = (
                    self.menu_entries[self.selection][3] + 1
                ) % len(self.menu_entries[self.selection][1])
                self.draw(scr)

    def draw(self, scr):
        scr.clear()
        self.tui_template(scr)

        scr.addstr(1, 2, "  Standard game  ", curses.color_pair(2))
        scr.addstr(3, 2, "Board size", curses.color_pair(1))
        scr.addstr(6, 2, "Player 1", curses.color_pair(1))
        scr.addstr(11, 2, "Player 2", curses.color_pair(1))

        for j, row in enumerate(self.menu_entries):
            padding = 2
            if row[-1] is str:
                if j == self.selection:
                    scr.addstr(
                        row[2],
                        padding,
                        row[1][0][1],
                        curses.color_pair(0) | curses.A_UNDERLINE | curses.A_BLINK,
                    )
                else:
                    scr.addstr(row[2], padding, row[1][0][1], curses.color_pair(0))

                continue

            for i, entry in enumerate(row[1]):
                if j == self.selection and i == row[3]:
                    scr.addstr(
                        row[2], padding, entry[0], curses.color_pair(3) | curses.A_BLINK
                    )
                elif i == row[3]:
                    scr.addstr(row[2], padding, entry[0], curses.color_pair(0))
                else:
                    scr.addstr(
                        row[2], padding, entry[0], curses.color_pair(0) | curses.A_DIM
                    )

                padding += len(entry[0]) + 1

        scr.addstr(
            curses.LINES - 1,
            0,
            "Press q to go back, use arrow keys and space to navigate ",
            curses.color_pair(1),
        )

        scr.refresh()

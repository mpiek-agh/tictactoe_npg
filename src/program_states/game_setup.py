import curses

from src import ProgramState, Player


class GameSetup(ProgramState):
    def __init__(self):
        # Klucz, pozycje w subsekcji z wartościami, wiersz w TUI, wybór
        self.menu_entries = [
            ["board_size", (("3x3", 3), ("4x4", 4), ("5x5", 5), ("6x6", 6)), 4, 0],
            ["starting_player", (("1", 0), ("2", 1), ("Random", -1)), 7, 2],
            ["undoes", (("0", 0), ("1", 1), ("2", 2), ("3", 3)), 10, 1],

            ["player1_name", [["Name", "Player 1 name"]], 13, 0, str],
            ["player1_symbol", (("X", "X"), ("O", "O"), ("#", "#"), ("$", "$"), ("%", "%"), ("&", "&"), ("M", "M"), ("W", "W"),), 14, 0],
            ["player1_color", (("Cyan", 2), ("Magenta", 3), ("Blue", 4), ("Green", 5), ("Red", 6), ("Yellow", 7),), 15, 1],

            ["player2_name", [["Name", "Player 2 name"]], 18, 0, str],
            ["player2_symbol", (("X", "X"), ("O", "O"), ("#", "#"), ("$", "$"), ("%", "%"), ("&", "&"), ("M", "M"), ("W", "W"),), 19, 1],
            ["player2_color", (("Cyan", 2), ("Magenta", 3), ("Blue", 4), ("Green", 5), ("Red", 6), ("Yellow", 7),), 20, 2],

            ["play", (("Play", None),), 22, 0],
        ]

        self.selection = 0
        self.next_state = "game"

        # pozycja w menu przy której wciśnięcie spacji spowoduje przejście do kolejnego stanu programu
        self.confirm_entry = 9

    def get_loop_return(self):
        # definiuje co powinna zwrócić funkcja loop
        player1 = Player(self.entry_value(3), self.entry_value(4), self.entry_value(5), 0 ,self.entry_value(2))
        player2 = Player(self.entry_value(6), self.entry_value(7), self.entry_value(8), 0 ,self.entry_value(2))
        return (self.entry_value(0), self.entry_value(1), player1, player2)

    def entry_value(self, entry):
        # zwraca wartość konkretnej pozycji w menu w zależności od wyboru użytkownika
        return self.menu_entries[entry][1][self.menu_entries[entry][3]][1]

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
                    self.menu_entries[self.selection][1][0][1] = scr.getstr(self.menu_entries[self.selection][2], 2, 20)
                    curses.noecho()
                    scr.nodelay(True)

                elif self.selection == self.confirm_entry:
                    return self.next_state, self.get_loop_return(), {}

                self.selection = (self.selection + 1) % len(self.menu_entries)
                self.draw(scr)

            elif c in (curses.KEY_DOWN, ord("s"), ord("j")):
                self.selection = (self.selection + 1) % len(self.menu_entries)
                self.draw(scr)
            elif c in (curses.KEY_UP, ord("w"), ord("k")):
                self.selection = (self.selection - 1) % len(self.menu_entries)
                self.draw(scr)
            elif c in (curses.KEY_LEFT, ord("a"), ord("h")):
                self.menu_entries[self.selection][3] = (self.menu_entries[self.selection][3] - 1) % len(self.menu_entries[self.selection][1])
                self.draw(scr)
            elif c in (curses.KEY_RIGHT, ord("d"), ord("l")):
                self.menu_entries[self.selection][3] = (self.menu_entries[self.selection][3] + 1) % len(self.menu_entries[self.selection][1])
                self.draw(scr)

    def draw_headers(self, scr):
        scr.addstr(1, 2, "  Standard game  ", curses.color_pair(2))
        scr.addstr(3, 2, "Board size", curses.color_pair(1))
        scr.addstr(6, 2, "Starting player", curses.color_pair(1))
        scr.addstr(9, 2, "Number of undoes", curses.color_pair(1))
        scr.addstr(12, 2, "Player 1", curses.color_pair(1))
        scr.addstr(17, 2, "Player 2", curses.color_pair(1))

    def draw(self, scr):
        scr.clear()

        self.draw_headers(scr)

        for j, row in enumerate(self.menu_entries):
            padding = 2
            if row[-1] is str:
                if j == self.selection: 
                    scr.addstr(row[2], padding, row[1][0][1], curses.color_pair(0))
                else:
                    scr.addstr(row[2], padding, row[1][0][1], curses.color_pair(0))

                continue

            for i, entry in enumerate(row[1]):
                if j == self.selection and i == row[3]:
                    scr.addstr(row[2], padding, entry[0], curses.color_pair(1))
                elif i == row[3]:
                    scr.addstr(row[2], padding, entry[0], curses.color_pair(3))
                else:
                    scr.addstr(row[2], padding, entry[0], curses.color_pair(0))

                padding += len(entry[0]) + 1

        self.tui_template(scr)

        scr.refresh()

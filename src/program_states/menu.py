from src.program_state import ProgramState
import curses


class Menu(ProgramState):
    def __init__(self):
        self.menu_entries = (
            ('Player vs player', 'game_setup'),
            ('Timed player vs player', 'timed_game_setup'),
            ('Player vs computer', 'computer_game_setup'),
            ('Players', 'players'),
            ('Scoreboard', 'scoreboard'),
            ('Help', 'help'),
            ('Quit', 'quit'),
        )

        self.selection = 0

    def loop(self, scr):
        self.draw(scr)

        while True:
            c = scr.getch()
            if c == ord('q'):
                return 'quit', [], {}
            elif c in (ord(' '), ord('\n')):
                return self.menu_entries[self.selection][1], (), {}
            elif c in (curses.KEY_DOWN, ord('s'), ord('j')):
                self.selection = (self.selection+1)%len(self.menu_entries)
                self.draw(scr)
            elif c in (curses.KEY_UP, ord('w'), ord('k')):
                self.selection = (self.selection-1)%len(self.menu_entries)
                self.draw(scr)

    def draw(self, scr):
        scr.clear()
        self.tui_template(scr)

        scr.addstr(1, 2, '  TicTacToe  ', curses.color_pair(2))

        for i, entry in enumerate(self.menu_entries):
            if i==self.selection:
                scr.addstr(3+i, 2, entry[0], curses.color_pair(3) | curses.A_BLINK)
            else:
                scr.addstr(3+i, 2, entry[0], curses.color_pair(1))

        scr.refresh()
import curses
import csv

from src import ProgramState

class Scoreboard(ProgramState):
    def __init__(self):
        self.scoreboard = None

        self.selection = 0
    
    def loop(self, scr):
        self.draw(scr)

        while True:
            c = scr.getch()
            if c == ord('q'):
                return 'menu', [], {}
    
    def draw(self, scr):
        scr.clear()

        scr.addstr(1, 2, '  Scoreboard  ', curses.color_pair(2))
        
        self.tui_template(scr)

        scr.refresh()
    
    def read_file(self):
        pass

    def write_file(self):
        pass

    def clear_score(self):
        pass

    def remove_player(self):
        pass

    def clear_file(self):
        pass

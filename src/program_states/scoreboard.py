import curses
import math

from src import ProgramState
from src.scoreboard_managment import read_scoreboard


class Scoreboard(ProgramState):
    def __init__(self):
        self.scoreboard = read_scoreboard()
        self.selection = 0 #wybór pozycji
        self.page = 0
        self.max_rows = curses.LINES - 11

        if len(self.scoreboard) == 0: self.max_page = 1
        else: self.max_page = math.ceil(len(self.scoreboard) / self.max_rows)
    
    def loop(self, scr):
        self.draw(scr)

        while True:
            c = scr.getch()
            if c == ord('q'):
                return 'menu', [], {}
            
            elif c in (ord(" "), ord("\n")):
                if self.selection == 1: self.page = (self.page-1) % self.max_page
                elif self.selection == 0: self.page = (self.page+1) % self.max_page
                self.draw(scr)
                    
            elif c in (curses.KEY_LEFT, ord("a"), ord("h")):
                self.selection = (self.selection - 1) % 2
                self.draw(scr)
            elif c in (curses.KEY_RIGHT, ord("d"), ord("l")):
                self.selection = (self.selection + 1) % 2
                self.draw(scr)
      
    def draw(self, scr):
        scr.clear()

        scr.addstr(1, 2, '  Scoreboard  ', curses.color_pair(2))

        self.draw_confirm_buttons(scr, 2, 3)
        
        self.draw_headers(scr, 2, 5)

        self.draw_scoreboard(scr, 2, 7)
        
        self.draw_page_num(scr, 2, curses.LINES-3)

        self.tui_template(scr)

        scr.refresh()
    
    def draw_confirm_buttons(self, scr, x, y):
        scr.addstr(y, x, " previous page ", curses.color_pair(1) if self.selection == 0 else curses.color_pair(3))
        scr.addstr(y, x + 18, " next page ", curses.color_pair(1) if self.selection == 1 else curses.color_pair(3))

    def draw_scoreboard(self, scr, x, y):
        for i, line in enumerate(self.scoreboard[self.page*self.max_rows:self.page*self.max_rows+self.max_rows]):
            scr.addstr(y+i, x, line['player'], curses.color_pair(0))
            scr.addstr(y+i, 20+x, line['win_pvp'], curses.color_pair(0))
            scr.addstr(y+i, 40+x, line['win_time'], curses.color_pair(0))
            scr.addstr(y+i, 57+x, line['win_computer'], curses.color_pair(0))
            
    def draw_headers(self, scr, x, y):
        scr.addstr(y, x, 'Player name', curses.color_pair(6))
        scr.addstr(y, x+20, 'Wins: Multiplayer', curses.color_pair(6))
        scr.addstr(y, x+40, 'Wins: Timemode', curses.color_pair(6))
        scr.addstr(y, x+57, 'Wins: vs Computer', curses.color_pair(6))

    def draw_page_num(self, scr, x, y):
        scr.addstr(y, x, f'Page {self.page+1} / {self.max_page}', curses.color_pair(0))
        



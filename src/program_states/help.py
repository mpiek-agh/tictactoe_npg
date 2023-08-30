from src.program_state import ProgramState
import curses


class Help(ProgramState):
    def loop(self, scr):
        self.draw(scr)

        while True:
            c = scr.getch()
            if c == ord('q'):
                return 'menu', [], {}

    def draw(self, scr):
        scr.clear()
        self.tui_template(scr)

        scr.addstr(1, 2, '  Help  ', curses.color_pair(2))

        scr.addstr(3, 2, ' w, k, up arrow ', curses.color_pair(1))
        scr.addstr(' - move up through menu entries')

        scr.addstr(4, 2, ' s, j, down arrow ', curses.color_pair(1))
        scr.addstr(' - move down through menu entries')

        scr.addstr(5, 2, ' a, h, left arrow ', curses.color_pair(1))
        scr.addstr(' - move left through menu entries')

        scr.addstr(6, 2, ' d, l, right arrow ', curses.color_pair(1))
        scr.addstr(' - move right through menu entries')

        scr.addstr(8, 2, ' q ', curses.color_pair(1))
        scr.addstr(' - quit, go back')

        scr.addstr(9, 2, ' space, enter ', curses.color_pair(1))
        scr.addstr(' - select, confirm')

        scr.addstr(11, 2, 'For real help, please visit: ')
        scr.addstr('https://findahelpline.com/pl/topics/suicidal-thoughts', curses.COLOR_BLUE | curses.A_UNDERLINE)

        scr.addstr(curses.LINES-1, 0, 'Press q to go back, use arrow keys and space to navigate ', curses.color_pair(1))

        scr.refresh()
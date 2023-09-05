from abc import ABC, abstractmethod
import curses


class ProgramState(ABC):
    @abstractmethod
    def loop(self, scr):
        """
        Funkcja powinna zawierać pętle przyjmującą dane wejściowe od użytkownika
        i wyświetlającą odpowiednią zawartość na ekranie.

        Wartością zwracaną ma być kolejny stan programu wraz z odpowiednimi parametrami
        np. z ekranu ustalania zasad gry przechodzimy do samej gry

        return /stan/, /agrumenty/, /argumenty nazwane/
        return 'game', (3), {Player1: p1, Player2: p2}
        """
        pass

    def tui_template(self, scr):
        scr.addstr(curses.LINES - 1, 0, "Press q to go back, use arrow keys and space to navigate ", curses.color_pair(1))

    def clear_cursor(self, scr):
        # przestawia kursor w prawy dolny róg ekranu
        scr.move(curses.LINES-1, curses.COLS-1)

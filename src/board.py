from pprint import pp
import random


class Board:
    def __init__(self, size):
        self.size = size
        self.new_board()

    def __call__(self, x, y):
        # zwraca wartość z podanej komórki
        # plansza = Board(3)
        # wartość = plansza(x, y)
        return self.board[y][x]

    def new_board(self):
        # nowa plansza
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def get_random_free(self):
        # wybiera losową pustą komórkę
        free_cells = []
        for y in range(self.size):
            for x in range(self.size):
                if not self.board[y][x]:
                    free_cells.append([x, y])

        return random.choice(free_cells) if len(free_cells) > 0 else False

    def get_free(self):
        # zwraca liste pustych komórek
        free_cells = []
        for y in range(self.size):
            for x in range(self.size):
                if not self.board[y][x]:
                    free_cells.append([x, y])

        return free_cells

    def place(self, x, y, player):
        # umieszcza id gracza na określonej pozycji, sprawdza czy pozycja jest dostępna
        if self.board[y][x] == 0:
            self.board[y][x] = player
            return True

        return False

    def remove(self, x, y):
        # usuwa id gracza z podanej komórki
        self.board[y][x] = 0

    def print_board(self):
        # wyświetla planszę w terminalu
        pp(self.board)

    def win_check(self):
        # wygrana w wierszu
        for row in self.board:
            if len(set(row)) == 1 and row[0] != 0:
                return row[0]

        # wygrana w kolumnie
        for col in range(self.size):
            if (len(set(row[col] for row in self.board)) == 1 and self.board[0][col] != 0):
                return self.board[0][col]

        # wygrana na przekątnych
        if (len(set(self.board[i][i] for i in range(self.size))) == 1 and self.board[0][0] != 0):
            return self.board[0][0]

        if (len(set(self.board[i][self.size - i - 1] for i in range(self.size))) == 1 and self.board[0][self.size - 1] != 0):
            return self.board[0][self.size - 1]

        # brak wygranych
        return 0

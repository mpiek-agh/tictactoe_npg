from pprint import pp


class Board:
    def __init__(self, size):
        self.size = size
        self.new_board()

    def new_board(self):
        # nowa plansza
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def place(self, x, y, player):
        self.board[y][x] = player

    def remove(self, x, y):
        self.board[y][x] = 0

    def print_board(self):
        pp(self.board)

    def win_check(self):
        # wygrana w wierszu
        for row in self.board:
            if sum(row) in (self.size, self.size*2): return row[0]

        # wygrana w kolumnie
        for col in range(self.size):
            if sum([row[col] for row in self.board]) in (self.size, self.size*2): return self.board[0][col]

        # wygrana na przekątnych
        if sum([self.board[i][i] for i in range(self.size)]) in (self.size, self.size*2): return self.board[0][0]

        if sum([self.board[i][self.size-i-1] for i in range(self.size)]) in (self.size, self.size*2): return self.board[0][self.size-1]

        # brak wygranych
        return 0

    def termination(self):
        # wartość znaku musi byc przypisana do gracza, żeby minimax mógł stwierdzić który gracz wygrał
        # wygrywającaj kolumna

        if self.board_size == 3:
            for col in range(self.board_size):
                if self.board[0][col] == self.board[1][col] == self.board[2][col] != 0:
                    return self.board[0][col]
            # wygrywający wiersz
            for row in range(self.board_size):
                if self.board[row][0] == self.board[row][1] == self.board[row][2] != 0:
                    return self.board[row][0]
            # wygrywająca przekątna

            if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
                return self.board[0][col]

            if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
                return self.board[0][col]

            return 0  # brak wygranych
        elif self.board_size == 4:
            for col in range(self.board_size):
                if (
                    self.board[0][col]
                    == self.board[1][col]
                    == self.board[2][col]
                    == self.board[3][col]
                    != 0
                ):
                    return self.board[0][col]
            # wygrywający wiersz
            for row in range(self.board_size):
                if (
                    self.board[row][0]
                    == self.board[row][1]
                    == self.board[row][2]
                    == self.board[row][3]
                    != 0
                ):
                    return self.board[row][0]
                # wygrywająca przekątna

            if (
                self.board[0][0]
                == self.board[1][1]
                == self.board[2][2]
                == self.board[3][3]
                != 0
            ):
                return self.board[0][col]

            if (
                self.board[0][3]
                == self.board[1][2]
                == self.board[2][1]
                == self.board[3][0]
                != 0
            ):
                return self.board[0][col]

            return 0  # brak wygranych
        elif self.board_size == 5:
            for col in range(self.board_size):
                if (
                    self.board[0][col]
                    == self.board[1][col]
                    == self.board[2][col]
                    == self.board[3][col]
                    == self.board[4][col]
                    != 0
                ):
                    return self.board[0][col]
            # wygrywający wiersz
            for row in range(self.board_size):
                if (
                    self.board[row][0]
                    == self.board[row][1]
                    == self.board[row][2]
                    == self.board[row][3]
                    == self.board[row][4]
                    != 0
                ):
                    return self.board[row][0]
                # wygrywająca przekątna

            if (
                self.board[0][0]
                == self.board[1][1]
                == self.board[2][2]
                == self.board[3][3]
                == self.board[4][4]
                != 0
            ):
                return self.board[0][col]

            if (
                self.board[0][4]
                == self.board[1][3]
                == self.board[2][2]
                == self.board[3][1]
                == self.board[4][0]
                != 0
            ):
                return self.board[0][col]

            return 0  # brak wygranych

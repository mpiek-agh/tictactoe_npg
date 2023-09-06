from dataclasses import dataclass


@dataclass
class Player:
    name: str = "Player"
    symbol: str = " "
    color: int = 0
    time: float = 0
    undoes: int = 0

    def get_name(self):
        # zwraca nazwę gracza upewniając się że po wprowadzeniu w terminalu nie jest typu bytes
        if type(self.name) is bytes:
            return self.name.decode('utf-8')

        return self.name

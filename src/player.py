from dataclasses import dataclass


@dataclass
class Player:
    name: str = "Player"
    symbol: str = " "
    color: int = 0
import csv
import pathlib
from enum import Enum

# Nazwa pliku CSV
scoreboard_data = pathlib.Path('data/scoreboard_data.csv')
scoreboard_data_headers =  ['players']

class fileoperationtype(Enum):
    WRITING = 'w'
    APPEND = 'a'

def save_scoreboard(data, mode: fileoperationtype):
    with open(scoreboard_data, mode.value, newline='') as file:
        writer = csv.DictWriter(file, fieldnames = scoreboard_data_headers)
        if mode == fileoperationtype.WRITING:
            writer.writeheader()


        writer.writerow(data)


def read_scoreboard():
    with open(scoreboard_data, 'r', newline='') as file:
       reader = csv.DictReader(file, fieldnames = scoreboard_data_headers)
       return list(reader)
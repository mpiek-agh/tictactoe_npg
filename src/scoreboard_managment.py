import csv
import pathlib
from typing import Dict


# Ścieżka do pliku CSV
scoreboard_path = pathlib.Path('src/csv_files/scoreboard.csv')
scoreboard_data_headers =  ['player', 'win_pvp', 'win_time', 'win_computer']


def save_scoreboard(data):
    with open(scoreboard_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = scoreboard_data_headers)

        writer.writeheader()

        for row in data: writer.writerow(row)

def read_scoreboard():
    try:
        with open(scoreboard_path, 'r', newline='') as file:
            reader = csv.DictReader(file, fieldnames = scoreboard_data_headers)
            return list(reader)[1:]
    except FileNotFoundError:
        save_scoreboard([])
        return []

def search_scoreboard(player_name, data):
    for i, dict in enumerate(data):
        if dict['player'] == player_name:
            return i
    return False

def update_scoreboard(player_name, win_header):
    data = read_scoreboard()
    idx = search_scoreboard(player_name, data)

    if idx is False:
        player = {'player': player_name, 'win_pvp': 0, 'win_time': 0, 'win_computer': 0,}
        player[win_header] = 1
        data.append(player)
    else:
        data[idx][win_header] = int(data[idx][win_header]) + 1

    save_scoreboard(data)
    
#def clear_score(self):
#    pass

#def remove_player(self):
#    pass

#def clear_file(self):
#    pass
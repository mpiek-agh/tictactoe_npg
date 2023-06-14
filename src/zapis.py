import csv
from enum import Enum
class fileoperationtype(Enum):
    WRITING = 'w'
    APPEND = 'a'

def zapisz_do_csv(gracze, nazwa_pliku, tryb: fileoperationtype):
    with open(nazwa_pliku, tryb.value, newline='') as plik_csv:
        pola = ['Gracz', 'Znak', 'Kolor']  # Przykładowe pola gracza

        writer = csv.DictWriter(plik_csv, fieldnames=pola)
        if tryb == fileoperationtype.WRITING:
            writer.writeheader()

        for gracz in gracze:
            writer.writerow(gracz)

def dodaj_gracza(gracze, nazwa_gracza, znak, kolor, plik_csv):
    nowy_gracz = {'Gracz': nazwa_gracza, 'Znak': znak, 'Kolor': kolor}
    gracze.append(nowy_gracz)
    zapisz_do_csv([nowy_gracz], plik_csv, fileoperationtype.APPEND)

def odczytaj_plik(nazwa_pliku):
    with open(nazwa_pliku, 'r', newline='') as plik_csv:
        odczytani_gracze = []
        linie = plik_csv.readlines()

    for idx, l in enumerate(linie):
        if idx == 0:
            continue
        dane = l.strip().split(",")
        gracz = {"Gracz": dane[0], "Znak": dane[1], "Kolor": dane[2]}
        odczytani_gracze.append(gracz)
  
    return odczytani_gracze

# Nazwa pliku CSV
plik_csv = 'gracze.csv'

# Przykładowa lista graczy
lista_graczy = [
    {'Gracz': 'Kamil', 'Znak': 'O', 'Kolor': 'Czerwony'},
    {'Gracz': 'Kacper', 'Znak': 'X', 'Kolor': 'Niebieski'},
    {'Gracz': 'Adam', 'Znak': 'Y', 'Kolor': 'Zielony'}
]



# Dodawanie nowych graczy
#dodaj_gracza(lista_graczy, 'Michal', 'X', 'Czerwony', plik_csv)
#dodaj_gracza(lista_graczy, 'Anna', 'O', 'Niebieski', plik_csv)

test = odczytaj_plik(plik_csv)
print(test)

# Wywołanie funkcji zapisującej do pliku CSV
#zapisz_do_csv(lista_graczy, plik_csv, fileoperationtype.WRITING)

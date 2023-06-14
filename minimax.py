import random
import copy

class GraZKompem:
    def __init__(self, runda=0, gracz=0) -> None:
        self.runda = runda

    def pustePola(self, KOL, WIER, plansza) -> int:
        #nie wiem czy to działa
        puste = []
        for kol in range(KOL):
            for wier in range(WIER):
                if plansza[kol][wier]:
                    puste.append((kol,wier))
        
        return puste


    def ruchLosowy(self, plansza):
        pustePola = plansza.pustePola()
        indeks = random.randrange(0, len(pustePola), 1)

        return pustePola[indeks]    #krotka (kol, wiersz)
    
    def minimax(self, plansza, maximizing): 
        case = plansza.koniecGry()  #funkcja kończąca gre po zwycięstwie lub remisie
        
        #wygrywa gracz 1
        if case == 1:
            return 1, None
        #wygrywa gracz 2
        if case == 2:
            return -1, None
        else:
            return 0, None
        
        
        if maximizing:
            pass
        
        elif not maximizing:
            mini = 2
            ruchKorzystny = None
            pustePola = plansza.pustePola()

            for (kol,wier) in pustePola:
                tab = copy.deepcopy(plansza)
                tab.znak(kol, wier, gracz)  #funkcja wstawiająca znak
                gra = self.minimax(tab, True)[0]


    def gra(self, plansza):
        if self.runda == 0:
            #losowy ruch
            ruch = self.ruchLosowy(plansza)
        else:
            #minimax
            self.minimax(plansza, False)
    
        return ruch

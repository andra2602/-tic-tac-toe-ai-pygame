import time

import pygame, sys, copy, math


ADANCIME_MAX=6

# === MENIU START ===
def meniu_start(ecran):
    pygame.font.init()
    font_mare = pygame.font.SysFont("timesnewroman", 36, bold=True)
    font_mic = pygame.font.SysFont("timesnewroman", 24)

    clock = pygame.time.Clock()
    alegere_algoritm = None
    alegere_simbol = None

    butoane_alg = [
        {"label": "Minimax", "rect": pygame.Rect(50, 80, 200, 50)},
        {"label": "Alpha-Beta", "rect": pygame.Rect(50, 150, 200, 50)}
    ]

    butoane_simbol = [
        {"label": "Play as X", "rect": pygame.Rect(50, 250, 200, 50)},
        {"label": "Play as 0", "rect": pygame.Rect(50, 320, 200, 50)}
    ]

    buton_start = pygame.Rect(75, 390, 150, 50)
    buton_info = pygame.Rect(260, 10, 30, 30)


    while True:
        ecran.fill((30, 30, 30))
        titlu = font_mare.render("X & 0", True, (255, 255, 255))
        titlu_rect = titlu.get_rect(center=(ecran.get_width() // 2, 30))
        ecran.blit(titlu, titlu_rect)

        mouse_pos = pygame.mouse.get_pos()

        # Algoritm buttons
        for b in butoane_alg:
            activ = (alegere_algoritm == b["label"])
            culoare = (167, 211, 255) if activ else (100, 180, 255) if b["rect"].collidepoint(mouse_pos) else (70, 130, 180)
            pygame.draw.rect(ecran, culoare, b["rect"], border_radius=10)
            pygame.draw.rect(ecran, (0, 0, 0), b["rect"], 2, border_radius=10)
            text = font_mic.render(b["label"], True, (0, 0, 0))
            text_rect = text.get_rect(center=b["rect"].center)
            ecran.blit(text, text_rect)

        # Simbol buttons
        for b in butoane_simbol:
            activ = (alegere_simbol == ('x' if "X" in b["label"] else '0'))
            culoare = (255, 255, 150) if activ else (255, 215, 100) if b["rect"].collidepoint(mouse_pos) else (200, 160, 80)
            pygame.draw.rect(ecran, culoare, b["rect"], border_radius=10)
            pygame.draw.rect(ecran, (0, 0, 0), b["rect"], 2, border_radius=10)
            text = font_mic.render(b["label"], True, (0, 0, 0))
            text_rect = text.get_rect(center=b["rect"].center)
            ecran.blit(text, text_rect)

        # Buton start game (doar dacă ambele sunt alese)
        if alegere_algoritm and alegere_simbol:
            culoare_start = (115, 243, 115) if buton_start.collidepoint(mouse_pos) else (42, 216, 42)
            pygame.draw.rect(ecran, culoare_start, buton_start, border_radius=10)
            pygame.draw.rect(ecran, (0, 0, 0), buton_start, 2, border_radius=10)
            text_start = font_mic.render("Start game", True, (0, 0, 0))
            text_rect = text_start.get_rect(center=buton_start.center)
            ecran.blit(text_start, text_rect)

        # Buton Info
        pygame.draw.circle(ecran, (180, 180, 180), buton_info.center, 15)
        font_info = pygame.font.SysFont("arial", 20, bold=True)
        text_info = font_info.render("i", True, (0, 0, 0))
        text_info_rect = text_info.get_rect(center=buton_info.center)
        ecran.blit(text_info, text_info_rect)


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buton_info.collidepoint(event.pos):
                    afiseaza_info_algoritmi(ecran)

                for b in butoane_alg:
                    if b["rect"].collidepoint(event.pos):
                        alegere_algoritm = b["label"]
                for b in butoane_simbol:
                    if b["rect"].collidepoint(event.pos):
                        alegere_simbol = 'x' if "X" in b["label"] else '0'

                if alegere_algoritm and alegere_simbol and buton_start.collidepoint(event.pos):
                    return alegere_algoritm, alegere_simbol

        clock.tick(30)
# adaugă buton de revenire în meniu în timpul gameului
def afiseaza_info_algoritmi(ecran):
    overlay = pygame.Surface((302, 460))
    overlay.set_alpha(230)  # mai transparent
    overlay.fill((10, 10, 10))
    ecran.blit(overlay, (0, 0))

    font_titlu = pygame.font.SysFont("timesnewroman", 28, bold=True)
    font_text = pygame.font.SysFont("timesnewroman", 20)

    lines = [
        "About the algorithms",
        "",
        "Minimax: search all moves,",
        "but it can be slower.",
        "",
        "Alpha-Beta: skip unnecessary moves,",
        "faster, same result.",
        "",
        "Click anywhere to close."
    ]

    y_start = 60
    spacing = 30
    for i, linie in enumerate(lines):
        font = font_titlu if i == 0 else font_text
        color = (255, 255, 255) if i == 0 else (210, 210, 210)
        text = font.render(linie, True, color)
        rect = text.get_rect(center=(151, y_start + i * spacing))
        ecran.blit(text, rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return


def deseneaza_buton_back(display, mouse_pos=None):
    if mouse_pos is None:
        mouse_pos = pygame.mouse.get_pos()

    buton_rect = pygame.Rect(10, 410, 100, 40)

    # Culori în funcție de stare
    if buton_rect.collidepoint(mouse_pos):
        culoare_fundal = (220, 120, 120)  # hover - roșu mai deschis
        culoare_text = (0, 0, 0)          # text negru pe fundal deschis
    else:
        culoare_fundal = (160, 60, 60)    # normal - roșu mai închis
        culoare_text = (255, 255, 255)    # alb pe fundal închis

    # Desen buton
    pygame.draw.rect(display, culoare_fundal, buton_rect, border_radius=10)
    pygame.draw.rect(display, (0, 0, 0), buton_rect, width=2, border_radius=10)

    # Text
    font = pygame.font.SysFont("timesnewroman", 20, bold=True)
    text = font.render('Back', True, culoare_text)
    text_rect = text.get_rect(center=buton_rect.center)
    display.blit(text, text_rect)

    return buton_rect

def deseneaza_buton_restart(display, mouse_pos=None, click=False):
    if mouse_pos is None:
        mouse_pos = pygame.mouse.get_pos()

    buton_rect = pygame.Rect(100, 310, 120, 50)

    # Determină culoarea de fundal și culoarea textului
    if click and buton_rect.collidepoint(mouse_pos):
        culoare_fundal = (30, 90, 150)     # click - albastru închis
        culoare_text = (255, 255, 255)     # alb
    elif buton_rect.collidepoint(mouse_pos):
        culoare_fundal = (100, 180, 255)   # hover - albastru deschis
        culoare_text = (0, 0, 0)           # text negru pe fundal deschis
    else:
        culoare_fundal = (70, 130, 180)    # normal - steel blue
        culoare_text = (255, 255, 255)     # alb

    # Desenează butonul cu colțuri rotunjite și contur
    pygame.draw.rect(display, culoare_fundal, buton_rect, border_radius=10)
    pygame.draw.rect(display, (0, 0, 0), buton_rect, width=2, border_radius=10)

    # Textul
    font = pygame.font.SysFont("timesnewroman", 25, bold=True)
    text = font.render('Restart', True, culoare_text)
    text_rect = text.get_rect(center=buton_rect.center)
    display.blit(text, text_rect)

    return buton_rect



def elem_identice(lista):
    return lista[0] * (lista[0] != Infogame.GOL and all(elem == lista[0] for elem in lista[1:]))


class Infogame:
    """
    Clasa care defineste gameul. Se va schimba de la un game la altul.
    """
    NR_COLOANE=3
    JMIN=None
    JMAX=None
    GOL='#'

    @classmethod
    def initializeaza(cls, display, NR_COLOANE=3, dim_celula=100):
        cls.display=display
        cls.dim_celula=dim_celula
        cls.x_img = pygame.image.load('assets/ics.png')
        cls.x_img = pygame.transform.scale(cls.x_img, (dim_celula, math.floor(dim_celula*cls.x_img.get_height()/cls.x_img.get_width())))
        cls.zero_img = pygame.image.load('assets/zero.png')
        cls.zero_img = pygame.transform.scale(cls.zero_img, (dim_celula,math.floor(dim_celula*cls.zero_img.get_height()/cls.zero_img.get_width())))
        cls.celuleGrid=[] #este lista cu patratelele din grid
        for linie in range(NR_COLOANE):
            cls.celuleGrid.append([])
            for coloana in range(NR_COLOANE):
                patr = pygame.Rect(coloana*(dim_celula+1), linie*(dim_celula+1), dim_celula, dim_celula)
                cls.celuleGrid[linie].append(patr)



    def deseneaza_grid(self, marcaj=None): # tabla de exemplu este ["#","x","#","0",......]

        for linie in range(Infogame.NR_COLOANE):
            for coloana in range(Infogame.NR_COLOANE):
                if marcaj==(linie,coloana):
                    #daca am o patratica selectata, o desenez cu rosu
                    culoare=(255,0,0)
                else:
                    #altfel o desenez cu alb
                    culoare=(255,255,255)
                pygame.draw.rect(self.__class__.display, culoare, self.__class__.celuleGrid[linie][coloana]) #alb = (255,255,255)
                if self.matr[linie][coloana]=='x':
                    self.__class__.display.blit(self.__class__.x_img,(coloana*(self.__class__.dim_celula+1),linie*(self.__class__.dim_celula+1)+ (self.__class__.dim_celula-self.__class__.x_img.get_height())//2))
                elif self.matr[linie][coloana]=='0':
                    self.__class__.display.blit(self.__class__.zero_img,(coloana*(self.__class__.dim_celula+1),linie*(self.__class__.dim_celula+1)+(self.__class__.dim_celula-self.__class__.zero_img.get_height())//2))
        pygame.display.update()



    def __init__(self, tabla=None):
        if tabla:
            self.matr=tabla
        else:
            self.matr = [[Infogame.GOL] * Infogame.NR_COLOANE for _ in range(Infogame.NR_COLOANE)]

    @classmethod
    def jucator_opus(cls, jucator):
        return '0' if jucator=='x' else 'x'


    def final(self):
        rez = elem_identice(self.matr[0]) \
              or elem_identice(self.matr[1]) \
              or elem_identice(self.matr[2]) \
              or elem_identice([self.matr[0][0], self.matr[1][0], self.matr[2][0]]) \
              or elem_identice([self.matr[0][1], self.matr[1][1], self.matr[2][1]]) \
              or elem_identice([self.matr[0][2], self.matr[1][2], self.matr[2][2]]) \
              or elem_identice([self.matr[0][0], self.matr[1][1], self.matr[2][2]]) \
              or elem_identice([self.matr[0][2], self.matr[1][1], self.matr[2][0]])
        if rez:
            return rez
        remiza = True
        for linie in self.matr:
            for elem in linie:
                if elem == Infogame.GOL:
                    remiza = False
        if remiza:
            return "remiza"
        return False

    def mutari(self, jucator):#jucator = simbolul jucatorului care muta
        lMutari = []
        for i, linie in enumerate(self.matr):
            for j,elem in enumerate(linie):
                if elem == Infogame.GOL:
                    tablaNoua = copy.deepcopy(self.matr)
                    tablaNoua[i][j] = jucator
                    lMutari.append(Infogame(tablaNoua))
        return lMutari


    #linie deschisa inseamna linie pe care jucatorul mai poate forma o configuratie castigatoare
    #practic e o linie care nu conține simbolul jucatorului opus
    def linie_deschisa(self, lista, jucator):
        return not Infogame.jucator_opus(jucator) in lista


    def linii_deschise(self, jucator):
        return self.linie_deschisa(self.matr[0], jucator) \
              + self.linie_deschisa(self.matr[1], jucator) \
              + self.linie_deschisa(self.matr[2], jucator) \
              + self.linie_deschisa([self.matr[0][0], self.matr[1][0], self.matr[2][0]], jucator) \
              + self.linie_deschisa([self.matr[0][1], self.matr[1][1], self.matr[2][1]], jucator) \
              + self.linie_deschisa([self.matr[0][2], self.matr[1][2], self.matr[2][2]], jucator) \
              + self.linie_deschisa([self.matr[0][0], self.matr[1][1], self.matr[2][2]], jucator) \
              + self.linie_deschisa([self.matr[0][2], self.matr[1][1], self.matr[2][0]], jucator)

    #restAdancime = cat mai are pana ajunge la adancimea maxima
    def estimeaza_scor(self, restAdancime):
        if self.final()==Infogame.JMAX:
            return 100+restAdancime
        elif self.final()==Infogame.JMIN:
            return -100-restAdancime
        elif self.final()=="remiza":
            return 0
        else:
            return self.linii_deschise(Infogame.JMAX)-self.linii_deschise(Infogame.JMIN)

    def sirAfisare(self):
        sir="  |"
        sir+=" ".join([str(i) for i in range(self.NR_COLOANE)])+"\n"
        sir+="-"*(self.NR_COLOANE+1)*2+"\n"
        for i in range(self.NR_COLOANE): #itereaza prin linii
                sir+= str(i)+" |"+" ".join([str(x) for x in self.matr[i]])+"\n"
        return sir

    def __str__(self):
        return self.sirAfisare()

    def __repr__(self):
        return self.sirAfisare()



class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de game
    Functioneaza cu conditia ca in cadrul clasei Infogame sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Infogame sa fie definita si o metoda numita mutari() care ofera lista cu configuratiile posibile in urma mutarii unui jucator
    """
    def __init__(self, tabla_game, j_curent, adancime, parinte=None, estimare=None):
        self.tabla_game=tabla_game
        self.j_curent=j_curent

        #adancimea in arborele de stari
        self.adancime=adancime

        #estimarea favorabilitatii starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.estimare=estimare

        #lista de mutari posibile din starea curenta
        self.mutari_posibile=[]

        #cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa=None


    def mutari(self):
        l_mutari=self.tabla_game.mutari(self.j_curent)
        juc_opus=Infogame.jucator_opus(self.j_curent)
        l_stari_mutari=[Stare(mutare, juc_opus, self.adancime-1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari


    def __str__(self):
        sir= str(self.tabla_game) + "(Current game:"+self.j_curent+")\n"
        return sir



""" Algoritmul MinMax """

def min_max(stare):
    if stare.tabla_game.final() or stare.adancime == 0:
        stare.estimare = stare.tabla_game.estimeaza_scor(stare.adancime)
        return stare
    mutariCuEstimare= [min_max(mutare) for mutare in stare.mutari()]
    if stare.j_curent == Infogame.JMAX:
        stare.stare_aleasa = max(mutariCuEstimare, key = lambda x: x.estimare)
    else:
        stare.stare_aleasa = min(mutariCuEstimare, key = lambda x: x.estimare)
    stare.estimare = stare.stare_aleasa.estimare
    return stare


def alpha_beta(alpha, beta, stare):
    if stare.tabla_game.final() or stare.adancime == 0:
        stare.estimare = stare.tabla_game.estimeaza_scor(stare.adancime)
        return stare

    if stare.j_curent == Infogame.JMAX:
        stare.estimare = float('-inf')
        for mutare in stare.mutari():
            mutareCuEstimare = alpha_beta(alpha, beta, mutare)
            if stare.estimare < mutareCuEstimare.estimare:
                stare.estimare = mutareCuEstimare.estimare
                stare.stare_aleasa = mutareCuEstimare
                if alpha < mutareCuEstimare.estimare:
                    alpha = mutareCuEstimare.estimare
                    if beta <= alpha:
                        break
    else:
        stare.estimare = float('inf')
        for mutare in stare.mutari():
            mutareCuEstimare = alpha_beta(alpha, beta, mutare)
            if stare.estimare > mutareCuEstimare.estimare:
                stare.estimare = mutareCuEstimare.estimare
                stare.stare_aleasa = mutareCuEstimare
                if beta > mutareCuEstimare.estimare:
                    beta = mutareCuEstimare.estimare
                    if beta <= alpha:
                        break
    stare.estimare = stare.stare_aleasa.estimare
    return stare

def afis_daca_final(stare_curenta):
    final = stare_curenta.tabla_game.final()
    if final:
        if final == "remiza":
            mesaj = "It's a draw!"
        else:
            mesaj = f"{final} has won!"

        # Mai întâi: desenăm butonul (ca fundal)
        deseneaza_buton_restart(Infogame.display)

        # Apoi: desenăm textul peste
        font = pygame.font.SysFont(None, 40)
        text = font.render(mesaj, True, (255, 255, 255))
        text_rect = text.get_rect(center=(Infogame.display.get_width() // 2, 380))
        Infogame.display.blit(text, text_rect)

        pygame.display.update()
        return True
    return False



def main():
    pygame.init()
    ecran = pygame.display.set_mode((302, 460))
    pygame.display.set_caption("X & 0")

    algoritm, simbol = meniu_start(ecran)  # START aici

    ecran.fill((0, 0, 0))  # curăță complet ecranul
    pygame.display.update()

    Infogame.JMIN = simbol
    Infogame.JMAX = '0' if simbol == 'x' else 'x'
    tip_algoritm = '1' if algoritm == "Minimax" else '2'

    tabla_curenta = Infogame()
    print("Initial board")
    print(str(tabla_curenta))
    stare_curenta = Stare(tabla_curenta, 'x', ADANCIME_MAX)

    Infogame.initializeaza(ecran)
    de_mutat = False
    tabla_curenta.deseneaza_grid()
    deseneaza_buton_restart(ecran)

    while True :
        if (stare_curenta.j_curent==Infogame.JMIN):
        #muta jucatorul
            #[MOUSEBUTTONDOWN, MOUSEMOTION,....]
            #l=pygame.event.get()
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                buton_restart = deseneaza_buton_restart(ecran, mouse_pos, click=False)
                buton_back = deseneaza_buton_back(ecran, mouse_pos)
                pygame.display.update()

                if event.type== pygame.QUIT:
                    pygame.quit() #inchide fereastra
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN: #click
                    if buton_back.collidepoint(event.pos):
                        pygame.draw.rect(ecran, (0, 0, 0), (0, 360, 302, 100))
                        return main()
                    pos = pygame.mouse.get_pos()#coordonatele clickului
                    # Verificare dacă s-a dat click pe butonul de restart
                    if buton_restart.collidepoint(event.pos):
                        print("Restart game")
                        pygame.draw.rect(ecran, (0, 0, 0), (0, 360, 302, 100))  # curăț toată zona de jos
                        tabla_curenta = Infogame()
                        stare_curenta = Stare(tabla_curenta, 'x', ADANCIME_MAX)
                        tabla_curenta.deseneaza_grid()
                        deseneaza_buton_restart(ecran)
                        de_mutat = False
                        continue

                    for linie in range(Infogame.NR_COLOANE):
                        for coloana in range(Infogame.NR_COLOANE):

                            if Infogame.celuleGrid[linie][coloana].collidepoint(pos):#verifica daca punctul cu coord pos se afla in dreptunghi(celula)
                                ###############################

                                if stare_curenta.tabla_game.matr[linie][coloana] == Infogame.JMIN:
                                    if (de_mutat and linie==de_mutat[0] and coloana==de_mutat[1]):
                                        #daca am facut click chiar pe patratica selectata, o deselectez
                                        de_mutat=False
                                        stare_curenta.tabla_game.deseneaza_grid()
                                    else:
                                        de_mutat=(linie, coloana)
                                        #desenez gridul cu patratelul marcat
                                        stare_curenta.tabla_game.deseneaza_grid(de_mutat)
                                elif stare_curenta.tabla_game.matr[linie][coloana] == Infogame.GOL:
                                    if de_mutat:
                                        #### eventuale teste legate de mutarea simbolului
                                        stare_curenta.tabla_game.matr[de_mutat[0]][de_mutat[1]]=Infogame.GOL
                                        de_mutat=False
                                    #plasez simbolul pe "tabla de game"
                                    stare_curenta.tabla_game.matr[linie][coloana]=Infogame.JMIN
                                    stare_curenta.tabla_game.deseneaza_grid()
                                    #afisarea starii gameului in urma mutarii utilizatorului
                                    print("\nThe board after the player's move")
                                    print(str(stare_curenta))


                                    #testez daca gameul a ajuns intr-o stare finala
                                    #si afisez un mesaj corespunzator in caz ca da
                                    if (afis_daca_final(stare_curenta)):
                                        break


                                    #S-a realizat o mutare. Schimb jucatorul cu cel opus
                                    stare_curenta.j_curent=Infogame.jucator_opus(stare_curenta.j_curent)


        #--------------------------------
        else: #jucatorul e JMAX (calculatorul)
            #Mutare calculator

            #preiau timpul in milisecunde de dinainte de mutare
            t_inainte=int(round(time.time() * 1000))
            if tip_algoritm=='1':
                stare_actualizata=min_max(stare_curenta)
            else: #tip_algoritm==2
                stare_actualizata=alpha_beta(-500, 500, stare_curenta)
            stare_curenta.tabla_game=stare_actualizata.stare_aleasa.tabla_game
            print("The board after computer's move")
            print(str(stare_curenta))

            stare_curenta.tabla_game.deseneaza_grid()
            #preiau timpul in milisecunde de dupa mutare
            t_dupa=int(round(time.time() * 1000))
            print("The computer \"thought\" for "+str(t_dupa-t_inainte)+" milliseconds.")

            if afis_daca_final(stare_curenta):
                # așteaptă click pe butonul de restart sau back
                while True:
                    for event in pygame.event.get():
                        mouse_pos = pygame.mouse.get_pos()
                        buton_restart = deseneaza_buton_restart(ecran, mouse_pos, click=False)
                        buton_back = deseneaza_buton_back(ecran, mouse_pos)
                        pygame.display.update()

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if buton_restart.collidepoint(event.pos):
                                print("Restart game")
                                pygame.draw.rect(ecran, (0, 0, 0), (0, 360, 302, 100))  # curăț zona de jos
                                tabla_curenta = Infogame()
                                stare_curenta = Stare(tabla_curenta, 'x', ADANCIME_MAX)
                                tabla_curenta.deseneaza_grid()
                                deseneaza_buton_restart(ecran)
                                break
                            elif buton_back.collidepoint(event.pos):
                                pygame.draw.rect(ecran, (0, 0, 0), (0, 360, 302, 100))
                                return main()
                    else:
                        continue
                    break

            #S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent=Infogame.jucator_opus(stare_curenta.j_curent)


if __name__ == "__main__" :
    main()
    while True :
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()

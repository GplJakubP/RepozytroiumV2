class Graf:
    def __init__(self, liczba_wierzcholkow):
        self.liczba_wierzcholkow = liczba_wierzcholkow
        self.macierz_sasiedztwa = [[0] * liczba_wierzcholkow for _ in range(liczba_wierzcholkow)]
    def dodaj_krawedz(self, zrodlo, cel, waga=1):
        if 0 <= zrodlo < self.liczba_wierzcholkow and 0 <= cel < self.liczba_wierzcholkow:
            self.macierz_sasiedztwa[zrodlo][cel] = waga
    def wyswietl_macierz_sasiedztwa(self):
        print("Macierz sąsiedztwa:")
        for wiersz in self.macierz_sasiedztwa:
            print(wiersz)
    def wyswietl_liste_sasiedztwa(self):
        print("Lista sąsiedztwa:")
        for wierzcholek in range(self.liczba_wierzcholkow):
            sasiedzi = [str(indeks) for indeks, waga in enumerate(self.macierz_sasiedztwa[wierzcholek]) if waga != 0]
            if sasiedzi:
                print(f"Wierzchołek {wierzcholek} -> {', '.join(sasiedzi)}")
            else:
                print(f"Wierzchołek {wierzcholek} -> Brak sąsiadów")
    def wyswietl_graf(self):
        print("Interpretacja graficzna grafu:")
        for zrodlo in range(self.liczba_wierzcholkow):
            for cel, waga in enumerate(self.macierz_sasiedztwa[zrodlo]):
                if waga != 0:
                    print(f"Wierzchołek {zrodlo} --- {waga} --> Wierzchołek {cel}")
def utworz_graf():
    liczba_wierzcholkow = int(input("Podaj liczbę wierzchołków w grafie: "))
    graf = Graf(liczba_wierzcholkow)
    while True:
        print("Wybierz opcję:")
        print("1. Dodaj krawędź")
        print("2. Wyświetl macierz sąsiedztwa")
        print("3. Wyświetl listę sąsiedztwa")
        print("4. Wyświetl interpretację graficzną grafu")
        print("5. Zakończ program")
        wybor = input("Wybierz opcję (1-5): ")
        if wybor == "1":
            zrodlo = int(input("Podaj wierzchołek źródłowy: "))
            cel = int(input("Podaj wierzchołek docelowy: "))
            waga = int(input("Podaj wagę krawędzi (opcjonalne): "))
            graf.dodaj_krawedz(zrodlo, cel, waga)
        elif wybor == "2":
            graf.wyswietl_macierz_sasiedztwa()
        elif wybor == "3":
            graf.wyswietl_liste_sasiedztwa()
        elif wybor == "4":
            graf.wyswietl_graf()
        elif wybor == "5":
            break
        else:
            print("Nieprawidłowy wybór. Wybierz opcję od 1 do 5.")
print("Program do tworzenia grafu.")
rodzaj_grafu = input("Podaj rodzaj grafu (skierowany/nieskierowany/ważony/inny): ")

utworz_graf()

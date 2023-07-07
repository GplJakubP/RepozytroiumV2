from heapq import heappop, heappush


class Graf:
    def __init__(self, liczba_wierzcholkow):
        self.liczba_wierzcholkow = liczba_wierzcholkow
        self.lista_sasiedztwa = [[] for _ in range(liczba_wierzcholkow)]

    def dodaj_krawedz(self, zrodlo, cel, waga):
        self.lista_sasiedztwa[zrodlo].append((cel, waga))

    def najkrotsza_droga(self, zrodlo):
        odleglosci = [float('inf')] * self.liczba_wierzcholkow
        odleglosci[zrodlo] = 0
        kolejka = [(0, zrodlo)]
        poprzednicy = [None] * self.liczba_wierzcholkow

        while kolejka:
            d, v = heappop(kolejka)

            if d > odleglosci[v]:
                continue

            for u, waga in self.lista_sasiedztwa[v]:
                nowa_odleglosc = odleglosci[v] + waga
                if nowa_odleglosc < odleglosci[u]:
                    odleglosci[u] = nowa_odleglosc
                    poprzednicy[u] = v
                    heappush(kolejka, (odleglosci[u], u))

        return odleglosci, poprzednicy

    def odtworz_najkrotsza_droge(self, zrodlo, cel):
        odleglosci, poprzednicy = self.najkrotsza_droga(zrodlo)
        droga = []
        aktualny = cel
        while aktualny is not None:
            droga.append(aktualny)
            aktualny = poprzednicy[aktualny]
        droga.reverse()
        return droga


def wczytaj_graf():
    liczba_wierzcholkow = int(input("Podaj liczbę wierzchołków w grafie: "))
    graf = Graf(liczba_wierzcholkow)

    liczba_krawedzi = int(input("Podaj liczbę krawędzi w grafie: "))

    for _ in range(liczba_krawedzi):
        zrodlo = int(input("Podaj wierzchołek źródłowy: "))
        cel = int(input("Podaj wierzchołek docelowy: "))
        waga = int(input("Podaj wagę krawędzi: "))
        graf.dodaj_krawedz(zrodlo, cel, waga)

    return graf


def przyklad_dzialania():
    graf = Graf(5)

    graf.dodaj_krawedz(0, 1, 4)
    graf.dodaj_krawedz(0, 2, 1)
    graf.dodaj_krawedz(2, 1, 2)
    graf.dodaj_krawedz(1, 3, 1)
    graf.dodaj_krawedz(2, 3, 5)
    graf.dodaj_krawedz(3, 4, 3)

    return graf


def main():
    print("Program do wyznaczania najkrótszej drogi w grafie.")
    print("1. Wybierz przykładowy graf")
    print("2. Wprowadź własne dane")

    wybor = input("Wybierz opcję (1-2): ")

    if wybor == "1":
        graf = przyklad_dzialania()
    elif wybor == "2":
        graf = wczytaj_graf()
    else:
        print("Nieprawidłowy wybór.")
        return

    zrodlo = int(input("Podaj wierzchołek początkowy: "))
    cel = int(input("Podaj wierzchołek docelowy: "))

    najkrotsza_droga = graf.odtworz_najkrotsza_droge(zrodlo, cel)
    if najkrotsza_droga:
        print(f"Najkrótsza droga z wierzchołka {zrodlo} do wierzchołka {cel}:")
        print(" -> ".join(str(w) for w in najkrotsza_droga))
    else:
        print(f"Nie istnieje droga z wierzchołka {zrodlo} do wierzchołka {cel}.")


if __name__ == "__main__":
    main()

# def print_Imię_wiek(imie, wiek=18):
#   print("imie", imie , "wiek", wiek)

# print_Imię_wiek("Jakub", 20)
# print_Imię_wiek("Andrzej", 40)
# print_Imię_wiek("Mateusz", 23)
# print_Imię_wiek(wiek=70, imie="Jan")
# print_Imię_wiek("Dacjan")

"""
def oblicz(x,y):
   return x+y,x-y

print(oblicz(1,2))
krotka=oblicz(2,4)
print(krotka[0],krotka[1])
l1,l2=oblicz(3.5,0.6)
print(l1,l2)
"""

"""
def find(lista, wartosc):
    new_list = []
    for i in range(len(lista)):
        if lista[i] == wartosc:
            new_list.append(i)
    return new_list
l1 = [1, 2, 1, 1, 3, 5]
wartosc_szukana = 1
lista_indeksow = find(l1, wartosc_szukana)
print(lista_indeksow)
"""
"""
def sum_of_values(dict1):
    wynik = 0
    for i in dict1.values():
        wynik += i
    return wynik
dict1 = {'data1':10, 'data2':-4, 'data3':2}
dict2 = {'data1':15, 'data2':-2, 'data3':1, 'data4':87}
print(sum_of_values(dict1))
print(sum_of_values(dict2))

"""
"""
def potega(L1, L2):
    L3 = []
    if len(L1)!=len(L2):
        return None
    for i in range(len(L1)):
        L3.append(L1[i]**L2[i])
    return L3
wynik = potega([4, 3, 5, 6], [2, 7, 3, 4])
print(wynik)
"""

def dodawanie(x,y):
    wynik = x+y
    return wynik
def odejmowanie(x,y):
    wynik = x-y
    return wynik
def mnożenie(x,y):
    wynik = x*y
    return wynik
def dzielenie(x,y):
    if y == 0:
        return "błąd dzielenie"
    else: wynik = x/y
    return wynik
kalkulator = {"+":dodawanie, "-":odejmowanie, "*":mnożenie, "/":dzielenie}
d="/"
L1=2
L2=0

print(kalkulator[d](L1,L2))


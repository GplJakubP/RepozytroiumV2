
print ("""

1 dodawanie
2 odejmowanie
3 mnożenie
4 dzielenie
5 potęgowanie 
""")
z=int(input('Jaką operację chcesz wykonać? '))
if z>=6 or z<=0:
    print("Niepoprawna operacja")
    exit()
x=float(input('Podaj x : '))
y=float(input('Podaj y : '))
if z==1:
    w=x+y
elif z==2:
    w=x-y
elif z==3:
    w=x*y
elif z==4:
    if y==0:
        print('nie poprawne dane ')
        exit()
    w=x/y
elif z==5:
    w=x**y
print(f'Wynik = {w}')
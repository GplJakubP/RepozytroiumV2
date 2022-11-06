a=int(input('Podaj wiek: '))
if a<4:
    cena=0
elif a<=18:
    cena=10
else: cena=20
print(f'Cena= {cena}zł')

lidzba1 = int(input("lidzba 1"))
lidzba2 = int(input("lidzba 2"))

if(lidzba1 > lidzba2):
    wieksza = lidzba1
    mniejsza = lidzba2
else:
    wieksza = lidzba2
    mniejsza = lidzba1

while(mniejsza <= wieksza):
    print(mniejsza , end=' ')
    mniejsza = mniejsza + 1


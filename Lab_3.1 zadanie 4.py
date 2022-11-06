lidzba1 = int(input("lidzba 1"))
lidzba2 = int(input("lidzba 2"))

if(lidzba1 > lidzba2):
    wieksza = lidzba1
    mniejsza = lidzba2
else:
    wieksza = lidzba2
    mniejsza = lidzba1

while(mniejsza <= wieksza):
    if mniejsza%2 == 1:
        mniejsza += 1
        continue
    print(mniejsza , end=' ')
    mniejsza = mniejsza + 1


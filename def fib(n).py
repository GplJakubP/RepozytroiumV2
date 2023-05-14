def fib(n):
    if n == 0: return 0
    elif n==1: return 1
    elif n>1:
        Fib = [0,1]
        i = 2 
        while (i<=n):
            Fib.append(Fib[i-1]+Fib[i-2])
            i +=1
    return Fib[i-1]
n= int(input("Podaj n : "))
if (n>=0):print(fib(n))
else: print("Podany został zły argument ")
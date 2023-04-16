"""

def NWD_iter(a,b):
    while a!=b:
        if a>b: a= a-b;
        else: b= b-a;
    return a

"""

"""

def NWD(a,b):
    if a!=b:
        if a>b: return NWD(a-b,b)
        else: return NWD(a,b-a)
    return a
    
"""


"""

def nwd(a,b):
    while b!=0:
        temp = b:
        b = a % b
        a = temp
    return a
    
"""
"""
def nwd(a,b):
    if b!=0:
        return nwd(b,a%b)
    return a
"""


"""
Dla każdego z nich zrób schemat blokowy 
"""

def maxkiv(lista:list[int|float])->tuple[int, int|float]:
    """
    Maximum kiválasztás progtétele.
    visszatérési érték:
        [0]: index
        [1]: érték
    """
    max_ertek=lista[0]
    max_index=0
    for i in range(1,len(lista)):
        if lista[i]>max_ertek:
            max_ertek=lista[i]
            max_index=i
    return max_index, max_ertek

print(maxkiv([2,3,4,2]))

def paros_e(adat:int)->bool:
    return adat%2==0

def megszamlalas(lista:list, t)->int:
    c=0
    for i in range(len(lista)):
        if t(lista[i]):
            c+=1
    return c

print(megszamlalas( t=paros_e, lista=[1,2,3,4,5]))

def osszegzes_osszeadassal(lista:list)->int:
    s=0
    for i in range(len(lista)):
        s+=lista[i]
    return s
def osszegzes_szorzassal(lista:list)->int:
    s=lista[0]
    for i in range(1,len(lista)):
        s*=lista[i]
    return s
print(osszegzes_osszeadassal([2,3,4]))
print(osszegzes_szorzassal([2,3,4]))

def osszeadas(num1, num2):
    return num1+num2

def szorzas(num1, num2):
    return num1*num2

def osszegzes(lista:list, f)->int:
    s=lista[0]
    for i in range(1,len(lista)):
        s=f(s,lista[i])
    return s

print(osszegzes([2,3,4], osszeadas))
print(osszegzes([2,3,4], szorzas))

def szerkesztheto_e(a:int,b:int,c:int)->bool:
    return a<b+c and b<a+c and c<b+a

class NEM_SZERKESZTHETO(Exception):
    pass

def heron(a:int,b:int,c:int):
    if szerkesztheto_e(a,b,c):
        s = (a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**0.5
    else:
        raise NEM_SZERKESZTHETO

try:
    print(f"Háromszög területe: {heron(2,3,4)}")
except NEM_SZERKESZTHETO:
    print("Nem szerkeszthető a háromszög")
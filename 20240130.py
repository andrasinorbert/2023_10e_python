# Kis érdekesség, felületesen:
class Ember:
    def __init__(self, nev, kor):
        self.nev=nev
        self.kor=kor

    def kiir(self):
        return self.nev+" "+str(self.kor)
x= Ember("János", 24)
print(type(x))
print(x.kiir())

# Mai anyag:

def osszegzes(lista:list, f)->int:
    s=lista[0]
    for i in range(1,len(lista)):
        s=f(s,lista[i])
    return s

def osszeadas(num1, num2):
    return num1+num2

def szorzas(num1, num2):
    return num1*num2

print(osszegzes([2,3,4], osszeadas))
print(osszegzes([2,3,4], lambda num1,num2:num1+num2))
print(osszegzes([2,3,4], lambda num1,num2:num1*num2))

hatvany= lambda num1, num2: num1**num2
print(hatvany(2,3))

negyzet=lambda num:hatvany(num, 2)

print(negyzet(5))
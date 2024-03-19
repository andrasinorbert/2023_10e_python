"""
1. Fájl átnevezése: osztály_név.py

Feladatok:
1. A beolvas fv-ben valósítsd meg, hogy a paraméterben megadott fájlt beolvassa, és térjen vissza a szám listával az átalakítások után
2. A feladat1,2 stb fv-ben valósítsd meg a kért eljárásokat! A fájl beolvasásához használd a beolvas() függvényedet!
3. feladat1(): számold ki a fájlokban található számok összegét a tanult prog tétel segítségével!
4. feladat2(): számold ki a fájlokban található számok átlagát a tanult prog tétel segítségével!
5. feladat3(): számold ki a fájlokban található számok minimumát a tanult prog tétel segítségével!
6. feladat4(): számold ki a fájlokban található számok maximumát a tanult prog tétel segítségével!

Input fájlok használata:
feladat1() -> input1
feladat2() -> input2
feladat3() -> input3
feladat4() -> input3

Kiírások:
feladat1: [eredmény]
feladat2: [eredmény]
feladat3: [eredmény]
feladat4: [eredmény]
A ": " után csak az eredmény szerepeljen

A dolgozat python fájlját küldd el a andrasi.norbert@puskas.hu-ra az alábbi tárggyal:
[osztály][filebeolvasas1] név 
"""
def beolvas(filename:str, kezdosor:int=0, vege:int=0):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    
    szamok=[]
    for i in range(kezdosor,len(sorok)-vege):
        szamok.append(int(sorok[i].strip()))
    return szamok
def feladat1():
    szamok=beolvas("input1")
    sum=0
    for i in range(len(szamok)):
        sum+=szamok[i]
    print(f"feladat1: {sum}")
def feladat2():
    szamok=beolvas("input2", 2)
    sum=0
    for i in range(len(szamok)):
        sum+=szamok[i]
    print(f"feladat2: {sum/len(szamok)}")
def feladat3():
    szamok=beolvas("input3", 1,1)
    min=szamok[0]
    for i in range(1,len(szamok)):
        if szamok[i]<min:
            min=szamok[i]
    print(f"feladat3: {min}")
def feladat4():
    szamok=beolvas("input3", 1,1)
    max=szamok[0]
    for i in range(1,len(szamok)):
        if szamok[i]>max:
            max=szamok[i]
    print(f"feladat3: {max}")

feladat1()
feladat2()
feladat3()
feladat4()
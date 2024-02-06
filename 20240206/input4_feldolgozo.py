import own_func as of

sorok=of.beolvas("input4")

print(sorok)

szamok=of.strListToCleanToIntList(sorok,1,1)
print(szamok)

# 1. feladat: elemek összege
s=0
for i in range(len(szamok)):
    s+= szamok[i]
print(f"számok összege: {s}")

# 2. feladat: hány darab számunk van?
print(f"{len(szamok)} darab számunk van")

# 3. feladat: számok szorzata
s=1
for i in range(len(szamok)):
    s*= szamok[i]
print(f"számok szorzata: {s}")

# 4. feladat: legnagyobb szám
max=szamok[0]
for i in range(1,len(szamok)):
    if max<szamok[i]:
        max=szamok[i]
print(f"legnagyobb szám: {max}")

# 5. feladat: 3. szám értéke
print(f"A harmadik szám értéke: {szamok[2]}")

# 6. feladat: páratlan számok közül a legkisebb

# min=float('inf')
min = 2**1024-1
print(min)
for i in range(len(szamok)):
    if min>szamok[i] and szamok[i]%2==1:
        min=szamok[i]
if min == 2**1024-1:
    print("Nem volt páratlan szám")
else:
    print(f"A legkiebb ptlan szám: {min}")
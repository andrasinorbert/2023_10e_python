file=open("input1")
sorok=file.readlines()
file.close()

print(sorok)

szamok=[]
for i in range(len(sorok)):
    print(f"1: ({sorok[i]})")
    egysor=sorok[i].strip()
    print(f"2: ({egysor}) tipus: {type(egysor)}")
    szam=int(egysor)
    print(f"3: ({szam}) tipus: {type(szam)}")
    szamok.append(szam)

print(szamok)


szamok=[]
for i in range(len(sorok)):
    szamok.append(int(sorok[i].strip()))
print(szamok)
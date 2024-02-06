file=open("input3")
sorok=file.readlines()
file.close()

szamok=[]
for i in range(1,len(sorok)-1):
    szamok.append(int(sorok[i].strip()))
print(szamok)
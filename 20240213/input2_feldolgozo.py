import own_func as of

sorok=of.beolvas("input2")

adatok=sorok[0].split(" ")
szamok=of.strListToCleanToIntList(adatok,1,1)
print(szamok)

szamok=of.stringSzetszedo(sorok[0]," ",1,1)
print(szamok)

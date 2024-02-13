import own_func as of

def atlag(szamlista:list):
    s=0
    for i in range(len(szamlista)):
        s+= szamlista[i]
    return s/len(szamlista)

sorok=of.beolvas("input1")
szamok=of.strListToCleanToIntList(sorok,2,2)
print(atlag(szamok))


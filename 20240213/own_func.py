def beolvas(filename:str)->list[str]:
    file=open(filename)
    sorok=file.readlines()
    file.close()
    return sorok

def strListToCleanToIntList(strLista:list[str], elsosor:int=0, n:int=0)->list[int]:
    """
    elsosor: Hány sort hagyjon ki az elejéről
    n: Hátulról ennyivel nem fog foglalkozni
    """
    szamok=[]
    for i in range(elsosor, len(strLista)-n):
        szamok.append(int(strLista[i].strip()))
    return szamok

def stringSzetszedo(
        szoveg:str,
        separator:str=" ",
        elsosor:int=0,
        n:int=0,
        adatelvalaszto_separator=None):
    adatok=szoveg.split(separator)
    if adatelvalaszto_separator is not None:
        adatok[i]=adatok[i].split(adatelvalaszto_separator)
    return strListToCleanToIntList(adatok,elsosor, n)

def atlag(szamlista:list):
    s=0
    for i in range(len(szamlista)):
        s+= szamlista[i]
    return s/len(szamlista)
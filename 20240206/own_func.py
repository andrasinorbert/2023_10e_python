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
file=open("input2")
sorok= file.readlines()
file.close()

szamok=[]
for i in range(1,len(sorok)):
    szamok.append(int(sorok[i].strip()))

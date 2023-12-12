f=open("2023_10e_python/20231205/input.txt", "r")
l=f.readlines()
f.close()

print(l)
for i in range(len(l)):
    l[i]=l[i].strip()
print(l)

print(l[0])

s=0
for i in range(1,len(l)):
    s+=int(l[i])
print(f"összeg: {s}")
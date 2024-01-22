class XNemString(Exception):
    pass

def print_banner(x:str,y:str="*")->None:
    """
    x: szöveg
    y: banner karakter, hossza=1
    """
    #if type(x)!=type("str"): return -1
    if type(x)!=type("str"): raise XNemString
    if len(y)>1: return -2

    print(y*30)
    print(y*((30-len(x))//2), end="")
    print(x, end="")
    print(y*((30-len(x))//2), end="")
    if len(x)%2==0: print()
    else: print(y)
    print(y*30)

# print_banner("hello")
    
try:
    print_banner(6)
except XNemString:
    print("ERROR")


x=print_banner("hello", "hu")
if x==-1: print("X: nem szöveg!")
if x==-2: print("2. paraméter túl hosszú!")

print_banner(y="4", x="Hello")
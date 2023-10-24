def b(n:int):
    n = bin(n)[2:]
    if len(n)<8:
        n = "0"*(8-len(n))+n
    return n

for _ in range(int(input())):
    n1,n2 = input().split("/")
    n1 = "".join([ b(int(i)) for i in n1.split(".") ])
    n2 = "".join([ b(int(i)) for i in n2.split(".") ])
    n3 = [ str(int(n1[i]) and int(n2[i])) for i in range(len(n1)) ]
    n4 = [ str(int(int(n1[i]) or (not int(n2[i])))) for i in range(len(n1)) ]
    out1 = []
    out2 = []
    for i in range(0,len(n3),8):
        out1.append(str(int("".join(n3[i:i+8]),2)))
        out2.append(str(int("".join(n4[i:i+8]),2)))
    print(".".join(out1),end="/")
    print(".".join(out2))

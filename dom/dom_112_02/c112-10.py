in1 = list(input())
in2 = list(input())

k = 0
for i in range(len(in1)):
    for j in range(i):
        a = [ ii for ii in in1 ]
        a[i],a[j] = a[j],a[i]
        if a==in2:
            k=1
            break
    if k:
        break
print(k)
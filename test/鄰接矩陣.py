"""
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1
"""
import pprint
n = int(input())

lst = [ [0]*9 for i in range(n) ]

def dfs(x,n=0):
    r = 0
    for i in range(len(lst[x])):
        if lst[x][i] == 1:
            dfs(x,n+1)
            #dfs(i, n.copy())
    if r==0:
        return n


for i in range(n):
    a = list(map(int, input().split()))
    if a[1] != -1:
        lst[a[0]][a[1]] = 1
    if a[2] != -1:
        lst[a[0]][a[2]] = 1
import pprint

for i in range(n):
    num=0
    ans=[]
    for k in lst[i]:
        if k==1:
            num+=1

    print(i)
    dfs(i)



lst = []

while 1:
    n = int(input())
    if not n:
        break
    for i in range(n):
        lst.append(list(map(int,input().split())))



"""
1
10 20 30
2
6 8 10
5 5 5
7
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
6 6 6
7 7 7
5
31 41 59
26 53 58
97 93 23
84 62 64
33 83 27
0
"""

while 1:
    try:
        tw = int(input())
        n = int(input())
        wl = 0

        for i in range(n):
            l,w = list(map(int,input().split()))
            wl += l*w
        print(wl//tw)
    except:
        break
"""
40
23
1 2
2 17
2 10
21 48
16 4
2 2
21 31
21 1
16 1
2 1
21 17
2 3
16 2
16 39
16 38
16 5
16 2
16 10
1 96
2 12
1 3
21 4
2 56
29
26
15 5
5 42
15 1
15 27
7 55
7 14
5 5
15 6
5 1
1 2
1 32
7 1
1 1
5 21
1 1
5 1
1 8
1 5
1 28
15 7
1 20
1 1
15 20
1 39
1 3
15 4
"""
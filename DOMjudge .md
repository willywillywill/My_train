# DOMjudge

CLASS-1: DOM
CLASS-2: 解題

## DOM_10

- A：計算英文單字出現的總次數
    
    ```python
    n1 = input().lower()
    n = 0
    k = 0
    l = 0
    while 1:
        n2 = list(map(str, input().split()))
        for i in n2:
            if "EOF"==i:
                l = 1
                break
    
            if "." in i:
                i = i.replace(".","")
            if "," in i:
                i = i.replace(",","")    
            if ";" in i:
                i = i.replace(";","")
    
            if i.lower()==n1:
                n+=1
            k+=1
        if l:
            break
    print("%d,%d"%(n,k))
    
    """
    the
    The villagers of Little Hangleron still called it the Riddle House, even though it had been many
    years since the Riddle family had lived there. It stood on a hill overlooking the village, some of its
    windows boarded, tiles missing from its roof, and ivy spreading unchecked over its face.
    EOF
    
    are
    Each cell in a Bigtable can contain multiple versions of the same data; these versions are indexed by
    timestamp.
    
    Bigtable timestamps are integers.
    EOF
    """
    ```
    
- B：關鍵字排名
    
    ```python
    dit = {}
    l=0
    while 1:
        n2 = list(map(str, input().split()))
        for i in n2:
            i = i.lower()
            if "eof"==i:
                l=1
                break
            dit[i] = dit.get(i, 0)+1
        if l:
            break
    
    lst = list(dit.items())
    lst.sort(key=lambda x:x[1],reverse=True)
    for i in range(3):
        print(lst[i][1], end="," if i!=2 else "")
    
    """
    Google Google Google Google Google Bible Bible Bible Bible Google Google Google Google
    Google Bible Bible Bible Bible Website Analysis
    
    SEO SEO SEO SEO SEO SEO SEO Quality Windows Windows Windows Yahoo Yahoo Word
    Word Yahoo
    EOF
    
    Google Google Google Google Google Linux Linux Linux Linux Google Google Google Google
    Google Web Analysis SEO SEO SEO SEO Windows Windows Windows Windows Yahoo Yahoo
    Time time yahoo Yahoo
    EOF
    """
    ```
    
- C：樹的高度
    
    ```python
    """ *Dit-tree*
    
    def dfs(x):
        for i in range(n):
            if lst[i][x]:
                d[i] = d[x]+1
                dfs(i)
    for _ in range(int(input())):
        if _>0:
            input()
        n = int(input())
        lst = [[ 0 for j in range(n) ] for i in range(n)]
        for i in range(n-1):
            m = list(map(int, input().split(',')))
            lst[m[0]][m[1]] = 1
        d = [ 1 for i in range(n) ]
        dfs(0)
        print(max(d))
    """
    """ *Matrix-tree*
    def dfs(i):
        if i in dit:
            for j in range(1,n):
                if j in dit[i]:
                    val[j] = val[i]+1
                    dfs(j)
    
    for _ in range(int(input())):
        if _>0:
            input()
        n = int(input())
        dit = {}
        for _ in range(n-1):
            a,b = map(int, input().split(","))
            if b not in dit:
                dit[b] = [a]
            else:
                dit[b].append(a)
        val = [1 for i in range(n)]
        dfs(0)
        print(max(val))
    """
    
    ```
    
- D：樹和樹葉節點
    
    ```python
    def dfs(x, px):
        global ans
        for i in range(len(tree)):
            if 1 not in tree[x][:i]+tree[x][i+1:]:
                vv[x]=1
            if tree[x][i] and i!=px:
                v[i] +=1
                if v[i]>1:
                    ans = 1
                    break
                dfs(i,x)
    
    for _ in range(int(input())):
        in1 = list(map(str, input().split()))
        in1 = [ list(map(int, i.split(","))) for i in in1 if i!="0,0" ]
        if not in1:
            print(0)
            continue
        st = set()
        for i in in1:
            st.add(i[0])
            st.add(i[1])
    
        tree = [[ 0 for i in range(max(st)+1) ] for j in range(max(st)+1)]
    
        for i in in1:
            tree[i[0]][i[1]] = 1
            tree[i[1]][i[0]] = 1
            
        v = [0]*len(tree)
        vv = [0]*len(tree)
        ans = 0
    
        dfs(0,0)
        if ans:
            print("F")
        else:
            print(sum([ i for i in vv if i==1 ])-1)
    
    """
    5
    6,8 5,3 5,2 6,4 5,6 1,2 2,0 0,0
    8,1 1,3 6,2 8,10 7,5 1,4 7,8 7,6 8,0 0,0
    3,8 6,8 6,4 5,3 5,6 8,2 2,0 0,0
    0,0
    1,0 0,0
    
    4
    4,3 2,3 2,1 1,0 0,0
    1,1 0,0
    1,2 2,3 4,0 0,0
    1,2 2,3 3,1 4,5 5,0 0,0
    """
    ```
    
- E：身分證
    
    ```python
    id = {
        "T":[],"O":[],"F":[]
    }
    lst = list("ABCDEFGHJKLMNPQRSTUVXYWZI")
    dit = {}
    for i,j in enumerate(lst):
        dit[j] = str(10+i)
    lst = [1,9,8,7,6,5,4,3,2,1,1]
    
    for _ in range(int(input())):
        in1 = list(input())
        if int(in1[1])>2:
            id["F"].append(in1)
            continue
        id_v = in1.copy()
        d = in1.pop(0)
        in1.insert(0,dit[d[0]][1])
        in1.insert(0,dit[d[0]][0])
    
        for i in range(len(in1)):
            in1[i] = int(in1[i])*lst[i]
    
        if sum(in1) % 10 == 0:
            if id_v in id["T"]:
                id["O"].append(id_v)
            else:
                id["T"].append(id_v)
        else:
            id["F"].append(id_v)
        
    print("%d,%d,%d"%(len(id["T"]),len(id["O"]),len(id["F"])))
    """
    8
    M123456789
    A123456789
    A323456783
    M123456789
    M123456789
    M123456789
    Y123456788
    A223344556
    
    4
    R102345678
    A108881111
    A108881111
    B101111111
    """
    ```
    
- F：編碼
    
    ```python
    dit = {
        "00":"A",
        "01":"B",
        "100":"0",
        "101":"1",
        "1100":"2",
        "1101":"3",
        "11100":"4",
        "11101":"5",
        "111100":"6",
        "111101":"7",
        "111110":"8",
        "111111":"9"
    }
    
    for i in range(int(input())):
        in1 = input()
        lst = []
        n = 0
        while n < len(in1):
            for i in range(n,len(in1)):
                for j in dit:
                    if j==in1[n:i+1]:
                        lst.append(dit[j])
                        n=i+1
        if "A" in lst:
            k1 = lst.index("A")
            V_ = lst[k1-1:]
            S_ = lst[:k1-1]
        else:
            k1 = lst.index("B")
            V_ = lst[k1-1:]
            S_ = lst[:k1-1]
        print("%s,%s"%("".join(S_),"".join(V_)))
    
    """
    4
    1111001111011111101111111000010001
    101110011101110111000010101
    11100110111001011110001
    111011100110111100110100
    """
    ```
    
- G：進制轉換
    
    ```python
    h = {
        "0000":"0",
        "0001":"1",
        "0010":"2",
        "0011":"3",
        "0100":"4",
        "0101":"5",
        "0110":"6",
        "0111":"7",
        "1000":"8",
        "1001":"9",
        "1010":"A",
        "1011":"B",
        "1100":"C",
        "1101":"D",
        "1110":"E",
        "1111":"F"
    }
    o = {
        "000":"0",
        "001":"1",
        "010":"2",
        "011":"3",
        "100":"4",
        "101":"5",
        "110":"6",
        "111":"7"
    }
    
    for _ in range(int(input())):
        in1 = input()
        t16 = (4-(len(in1)%4))*"0"+in1 if len(in1)%4 else in1
        t8 = (3-(len(in1)%3))*"0"+in1 if len(in1)%3 else in1
    
        t16 = [ t16[i:i+4] for i in range(0,len(t16),4) ]
        t8 = [ t8[i:i+3] for i in range(0,len(t8),3) ]
    
        t16 = [ h[i] for i in t16 ]
        t8 =  [ o[i] for i in t8 ]
    
        print("%s,%s"%("".join(t16), "".join(t8)))
    
    """
    3
    010010011
    00011110001
    11001100
    
    2
    00110111
    11011110
    """
    ```
    
- H：撲克牌遊戲
    
    ```python
    lst = []
    for _ in range(int(input())):
        m = list(map(int,input().split()))
        for i in range(len(m)):
            if m[i] in [1,14,27,40]:
                m[i] = 1
            elif ((m[i]%14)+(m[i]//14)) > 10:
                m[i] = 10
            else:
                m[i] = (m[i]%14)+(m[i]//14)
        lst.append(m)
    
    for i in lst:
        sum_v = 0
        for j in i:
            if sum_v == 21:
                continue
            if j==1:
                sum_v += 1 if sum_v+11 > 21 else 11
            else:
                sum_v += j
        if sum_v > 21:
            print("F")
        else:
            print(sum_v)
    """
    5
    3 44
    6 12 1
    26 25 2
    14 27
    40 43
    
    3
    15 18 2
    14 21
    1 13 26
    """
    ```
    

## DOM_103

- A：
- B：
- C：
- D：
- E：
- F：
- G：
- H：

## DOM_104

- F 題 string 解
- H 題 生成樹 ****Kruskal****
- [https://blog.csdn.net/weixin_42216109/article/details/98593821](https://blog.csdn.net/weixin_42216109/article/details/98593821)

## DOM_105

- 計算字數
    
    ```python
    def st(in1):
        for i in list(".,;!"):
            in1 = in1.replace(i, "")
        return in1
    
    for _ in range(int(input())):
        in1 = list(map(str, st(input()).split()))
        print(len(in1))
    
    """
    3
    ThiV iV a Vample file.
    Hello World!!
    Hi!
    """
    ```
    
- 摩斯電碼
    
    ```python
    dit = {
        "-----":0,
        ".----":1,
        "..---":2,
        "...--":3,
        "....-":4,
        ".....":5,
        "-....":6,
        "--...":7,
        "---..":8,
        "----.":9
    }
    
    for _ in range(int(input())):
        in1 = input().replace(" ","")
        for i in range(0,len(in1),5):
            print(dit[in1[i:i+5]], end="")
        print()
    
    """
    3
    .---- ..--- ...--
    ....- ..... -....
    --... ---.. ----. 
    
    2
    .---- .---- -----
    ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.
    """
    ```
    
- 網段 ID
    
    ```python
    for _ in range(int(input())):
        in1 = input().split("/")
        in2 = list(map(int,in1[1].split(".")))
        in1 = list(map(int,in1[0].split(".")))
        k = [ str(in1[i] & in2[i]) for i in range(len(in1)) ]
        print(".".join(k))
    ```
    
- GCD
    
    ```python
    import math
    
    for _ in range(int(input())):
        in1 = list(map(int, input().split(",")))
        k = 0
        for i in range(len(in1)):
            for j in range(len(in1)):
                if i!=j:
                    k = max(k, math.gcd(in1[i],in1[j]))
        print(k)
    ```
    
- Heap tree or Binary tree
    
    ```python
    for _ in range(int(input())):
        in1 = list(map(int, input().split(",")))
        k1=1  # 1 -> yes 
        k2=1 
        k3=1
        for i in range(len(in1)):  
            if 2*i+1 < len(in1):   # Max Heap Tree
                if in1[i] < in1[2*i+1]:
                    k1=0
            if 2*i+2 < len(in1):
                if in1[i] < in1[2*i+2]:
                    k1=0
    
            if 2*i+1 < len(in1):   # Min Heap Tree
                if in1[i] > in1[2*i+1]:
                    k2=0
            if 2*i+2 < len(in1):
                if in1[i] > in1[2*i+2]:
                    k2=0
            
            if 2*i+1 < len(in1):   # BST
                if in1[i] < in1[2*i+1]:
                    k3=0
            if 2*i+2 < len(in1):
                if in1[i] > in1[2*i+2]:
                    k3=0
            
        if k1 or k2:
            print("H")
        elif k3:
            print("B")
        else:
            print("F")
    
    """
    4
    16,14,13,4,8,6,5,10,1
    16,14,10,13,4,6,5,1,8
    7,4,12,1,5,8,10
    9,6,12,2,8,11,15,1,3,7 
    
    """
    ```
    
- in-order and pre-order to post-order
    
    ```python
    class node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
    def buildTree(preorder, inorder):
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = node(inorder[idx])
            root.left = buildTree(preorder, inorder[:idx])
            root.right = buildTree(preorder, inorder[idx+1:])
            return root
    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            res.append(str(root.data))
    for _ in range(int(input())):
        in_lst = list(map(int, input().split(",")))
        pre_lst = list(map(int, input().split(",")))
        res = []
    
        root = buildTree(pre_lst, in_lst)
        postorder(root)
        print(",".join(res))
    ```
    
- LCS
    
    ```python
    for _ in range(int(input())):
        s1 = "0"+input().strip()
        s2 = "0"+input().strip()
    
        lst = [[0 for j in range(len(s1))] for i in range(len(s2))]
        for i in range(1,len(s2)):
            for j in range(1,len(s1)):
                if s2[i]==s1[j]:
                    lst[i][j] = lst[i-1][j-1]+1
                else:
                    lst[i][j] = max(lst[i-1][j], lst[i][j-1])
        
    
        print(lst[-1][-1])
    
    """
    2
    ACCGATGCAGCGCTC
    CCGATGA
    abcdghxy
    aedfhrz
    
    2
    13567
    24680
    ab12
    Abc1
    """
    ```
    
- Huffman Coding
    
    ```python
    class node:
        def __init__(self,data, s=None, left=None, right=None):
            self.s = s
            self.data = data
            self.left = left
            self.right = right
    
    def dfs(root, lst, lr=None):
        global st
        if root:
            if lr!=None:
                lst.append(lr)
            if root.s:
                lst.append(root.s)
            dfs(root.left, lst.copy(), lr=0)
            dfs(root.right, lst.copy(), lr=1)
        else:
            st.add(tuple(lst))
    
    str_text = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    for _ in range(int(input())):
        in1 = list(map(int, input().split(",")))
        data = [ [str_text[i],in1[i]] for i in range(len(in1)) ]
        nodes = [ node(i[1],i[0]) for i in data ]
        # bottom-up
        while len(nodes) > 1:
            n = []
            for i in range(2):
                k = [ i.data for i in nodes ]
                idx = k.index(min(k))
                k.pop(idx)
                n.append(nodes.pop(idx))
    
            root = node(n[0].data + n[1].data)
            root.left = n[0]
            root.right = n[1]
            nodes.append(root)
        root = nodes[0]
        st = set()
        dfs(root,[])
        lst = sorted(list(st), key=lambda x:x[-1])
        out = [ str(len(lst[i][:-1])) for i in range(len(lst)) ]
        print(",".join(out))
    
    """
    2
    2,3,6,8,13,15,19
    4,8,5
    
    3
    26,25,20,15,10,5
    4,3,5,6
    2,1 
    """
    ```
    

## DOM_106

- s or S number
    
    ```python
    def del_s(str1):
        str1.replace(",","")
        str1.replace(";","")
        str1.replace("!","")
        str1.replace(".","")
        return str1
    
    for _ in range(int(input())):
        s = list(map(str, input().split()))
    
        n = 0
        for i in s:
            i = del_s(i)
            if "S" in i or "s" in i:
                n+=1
        print(n)
    
    """
    3
    This is a sample file.
    Hello WoUld!!
    SOS! 
    """
    ```
    
- 羅馬數字to整數
    
    ```python
    dit = {
        "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
    }
    def f(x):
        if in1[x] > in1[x-1]:
            in1[x] = in1[x]-in1[x-1]
            del in1[x-1]
        if x < len(in1)-1:
            f(x+1)
    
    for _ in range(int(input())):
        in1 = input()
        in1 = [ dit[i] for i in in1 ] 
        if len(in1) > 1:
            f(1)
            print(sum(in1))
        else:
            print(in1[0])
    
    """
    8
    IX
    VI 
    XI
    XVII
    CCLXVIII
    MMMCC
    DCCVII
    MMCDLXIX 
    """
    ```
    
- 信用卡卡號
    
    ```python
    """
    5
    1234567891234563
    4013735633800642
    5181271099000017
    5241150318192904
    5241150313182900 
    
    3
    1234567891234561
    4013735633800643
    5181271099000014
    """
    def f(num):
        i,num = num
        i = 2 if i % 2 == 0 else 1
        num = str(int(num) * i)
        num = int(num[0])+int(num[1]) if len(num) > 1 else int(num)
        return num
    
    for _ in  range(int(input())):
        in1 = list(map(f, enumerate(input().strip())))
        print( "F" if sum(in1)%10 else "T")
    ```
    
- 幾A幾B
    
    ```python
    import itertools
    
    for _ in range(int(input())):
        in1 = list(map(str, input().split(",")))
        lst = list(itertools.permutations(in1[0],len(in1[0])))
        r1,r2 = lst[int(in1[1])-1],lst[int(in1[2])-1]
        A = 0
        B = 0
        for i in range(len(r1)):
            for j in range(len(r2)):
                if r1[i] == r2[j]:
                    if i==j:
                        A+=1
                    else:
                        B+=1
        print(str(A)+"A"+str(B)+"B")
    
    """
    3
    12,1,2
    123,1,2
    123,2,5
    
    4
    1234,15,9
    1234,3,4
    1234,1,24
    1234,1,1 
    """
    ```
    
- 網段廣播位置
    
    ```python
    for _ in range(int(input())):
        in1 = list(map(str, input().split("/")))
        r1 = list(map(int, in1[0].split(".")))
        r2 = list(map(int, in1[1].split(".")))
        r3 = []
        for i in r2:
            a = list(bin(i))[2:]
            if a==["0"]:
                a = list("00000000")
            for j in range(len(a)):
                a[j] = "0" if a[j]=="1" else "1" 
            r3.append(int("".join(a),2))
    
        out = []
        for i in range(4):
            b = r1[i]&r2[i]|r3[i]
            out.append(str(b))
        print(".".join(out))
    
    """
    5
    139.175.153.252/255.255.0.0
    10.104.69.0/255.255.255.192
    192.15.156.205/255.255.255.224
    192.168.10.65/255.255.255.224
    10.240.168.19/255.255.192.0 
    """
    ```
    
- 大數排序
    
    ```python
    """
    4
    222222222222222222222222222, 555555555555555555555555555, 111111111111111, 44444444444444444444444444444444444444444444444444444, 33333333333333333333333333333333333333333333
    123456789, 123456787, 123456788
    3333333333333333333333333, 1111111111111111111111111, 2469135802469135802469135308641975308641975308642
    44444444444444444444444444444444444444444444444444444, 111111111111111, 222222222222222222222222222, 33333333333333333333333333333333333333333333
    
    3
    4, 2, 1, 5
    1, 2, 3, 4, 5, 6
    7, 6, 5, 4, 3, 2
    """
    for _ in range(int(input())):
        in1 = list(map(int, input().split(",")))
        k = in1.copy()
        in1.sort()
        out = []
        while k:
            d = k.pop(0)
            out.append(str(in1.index(d)+1))
        print(", ".join(out))
    ```
    
- 樹判斷  - don`t know
    
    ```python
    """ !!!
    這題跟zerojudge b517是否為樹類似
    我的想法是先判斷這張圖是不是樹，不是樹的話，再去看他有沒有形成迴圈
    要符合樹的條件有以下兩點：
    1. 節點(node)-1 == 邊(edge) 的數量
    2. DFS拜訪完的節點數量 == 輸入時出現過的節點數量
    """
    
    def dfs(x, px): #判斷是否為樹函式
        visited.append(x)
        for i in range(20):
            if path[x][i]==1 and i!=px and i not in visited:
                dfs(i, x)
    
    def Cycle(x, px): #尋找形成迴圈的所有節點
        global start
        visited_cyc.append(x)
        for i in range(20):
            if path[x][i]==1 and i==start and i!=px and i in visited_cyc:
                visited_cyc.append(i)
            if path[x][i]==1 and i!=px and i not in visited_cyc:
                Cycle(i, x)
                
    for _ in range(int(input())):
        s=input().split()
        path=[[0 for _ in range(20)] for _ in range(20)]
        node=[0]*20 #紀錄出現過的節點
        edge=0 #紀錄邊的數量
        root=None
        for i in s:
            a, b=map(int, i.split(","))
            if root==None:
                root=a
        
            path[a][b]=1; path[b][a]=1
            node[a]=1; node[b]=1
            edge+=1
        
        node_num=node.count(1) #設為1的即為出現過的節點
        is_tree=True #是否為樹
        visited=[]
        dfs(root, root)
        
        #這邊用來判斷符不符合樹的條件
        if node_num-1!=edge or len(visited)!=node_num:
            is_tree=False
        
        #如果是樹就直接輸出T
        if is_tree:
            print("T")
        else:
            cycle=[]
            """
            如果visited==node_num，代表符合第二點條件，
            那就不可能是森林，所以必定有形成迴圈的情況。
            """
            if len(visited)==node_num:
                for i in range(20):
                    if node[i]==1:
                        start=i #紀錄第一個走訪的節點
                        visited_cyc=[]
                        Cycle(i, i)
                        #如果重複走到第一個節點，代表此節點是迴圈節點之一
                        if visited_cyc.count(i)>1:
                            cycle.append(i)
                print(*cycle, sep=", ")
            
            #否則就是森林，直接輸出F
            else:
                print("F")
    ```
    
- 後序運算式
    
    ```python
    for _ in range(int(input())):
        in1 = input().split()
        in1 = list(in1)
        out = []
        while in1:
            k = in1.pop(0)
            if k in "+-*/":
                a1 = out.pop(-2)
                a2 = out.pop(-1)
                out.append(str(int(eval(a1+k+a2))))
            else:
                out.append(k)
        print(out[0])
    
    """
    3
    3 5 +
    9 2 3 5 + * +
    6 3 / 1 4 - * 3 + 8 -
    
    3
    2 3 + 4 *
    2 3 4 + * 5 *
    2 123 -
    """
    ```
    

## DOM_107

- s and S number
    
    ```python
    def del_s(str1):
        str1 = str1.replace(",","")
        str1 = str1.replace(";","")
        str1 = str1.replace("!","")
        str1 = str1.replace(".","")
        return str1
    
    for _ in range(int(input())):
        s = list(map(del_s, input().split()))
        n = [ i for i in s if "s" in i.lower()]
        print(str(len(s))+","+str(len(n)))
    
    """
    3
    This is a sample file.
    Hello WoUld!!
    SOS! 
    """
    ```
    
- 井字棋
    
    ```python
    """
    3
    122
    110
    102
    211
    220
    201
    111
    220
    201
    
    4
    122
    110
    201
    212
    122
    121
    121
    021
    002
    121
    000
    000
    """
    
    for _ in range(int(input())):
        lst = []
        for i in range(3):
            lst.append(list(map(int, input())))
        a1 = [[ lst[ii][i] for ii in range(len(lst)) ] for i in range(3) ]
        a2 = [ lst[i]  for i in range(3) ]
        a3 = [ lst[i][i] for i in range(len(lst)) ]
        a4 = [ lst[i][abs(i-2)] for i in range(len(lst)) ]
    
        out = 0
        if not out:
            for i in a1:
                if i[0] == i[1] == i[2]:
                    out = i[0]
        if not out:
            for i in a2:
                if i[0] == i[1] == i[2]:
                    out = i[0]
        if not out:
            out = a3[0] if a3[0] == a3[1] == a3[2] else 0
        if not out:
            out = a4[0] if a4[0] == a4[1] == a4[2] else 0
        if out:
            print(out)
        else:
            print(3)
    ```
    
- 快樂數字
    
    ```python
    for _ in range(int(input())):
        n = input()
        in1 = list(n)
        for _ in range(int(n)):
            in1 = [ int(i)**2 for i in in1 ]
            in1 = [str(sum(in1))]
            in1 = [[ j for j in i ] for i in in1 ]
            in1 = [ j for i in in1 for j in i ]
            if in1[0]=="1" and len(in1)==1:
                print("T")
                break
        else:
            print("F")
    
    """
    8
    68
    49
    14
    65
    213
    9437
    100000
    99999
    """
    ```
    
- 排列
    
    ```python
    import itertools
    
    for _ in range(int(input())):
        in1 = list(map(int,input().split(",")))
        k = in1[-1]
        in1 = in1[1:in1[0]+1]
        lst = list(itertools.permutations(in1, len(in1)))
        lst.sort()
        for i in lst[k-1]:
            print(i,end="")
        print()
    
    """
    4
    2,0,2,1
    3,0,3,9,1
    3,0,3,9,6
    4,4,5,6,7,24
    """
    ```
    
- 大數承冪運算
    
    ```python
    for _ in range(int(input())):
        in1 = list(map(int,input().split(",")))
        p = str(in1[0]**in1[1])
        print(len(p))
    ```
    
- mod
    
    ```python
    f = lambda a,b,m: (a+b)%m == (a-b)%m
    
    for _ in range(int(input())):
        in1 = list(map(int, input().split()))
        a_min,a_max,b_min,b_max,c_min,c_max = in1
        
        n=0
        for i in range(a_min,a_max+1):
            for j in range(b_min,b_max+1):
                for k in range(c_min,c_max+1):
                    if f(i,j,k):
                        n+=1
        print(n)
        
    
    """
    4
    1 2 2 4 3 4
    1 2 2 4 6 7
    3 4 2 4 6 7
    5 9 10 12 2 9 
    
    5
    1 1 1 1 1 1
    1 2 1 2 1 2
    1 5 1 5 1 2
    1 5 1 5 3 4
    1 5 1 5 1 4
    """
    ```
    
- 數最長路徑
    
    ```python
    # DFS Bottom-up
    
    class node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    def buildTree(i):
        root = node(in1[i])
        nodes.add(root)
        if 2*i+1 < len(in1):
            if in1[2*i+1] != "null":
                root.left = buildTree(2*i+1)
        if 2*i+2 < len(in1):
            if in1[2*i+2] != "null":
                root.right = buildTree(2*i+2)
        return root
    def dfs(root,n):
        if not root.left and not root.right:
            return 1
        k1,k2 = 0,0
        if root.left:
            k1 = dfs(root.left, n)+1
        if root.right:
            k2 = dfs(root.right, n)+1
        return max(k1,k2)
    def del_s(s):
        s = s.replace("[","")
        s = s.replace("]","")
        return s
    
    for _ in range(int(input())):
        nodes = set()
        in1 = list(map(str, del_s(input()).split(",")))
        buildTree(0)
        out = 0
        for i in nodes:
            if i.left and i.right:
                out = max(out,dfs(i.left,0)+dfs(i.right,0))
            elif i.left:
                out = max(out, dfs(i.left,0))
            elif i.right:
                out = max(out, dfs(i.right,0))
        print(out)
    
    """
    5
    [6,5,7]
    [1,2,3,4,5]
    [1,2,3,4,6,null,7]
    [1,2,3,4,5,6,7,8,9,10]
    [1,2,3,4,5,6,7,8,null,null,null,null,null,null,15]
    
    4
    [6,null,7]
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    [1,2,99,null,null,3]
    [99,2,3,4,null,6,7,8,null,null,null,12]
    """
    ```
    
- 循環排列
    
    ```python
    def del_s(s):
        s = s.replace("[","")
        s = s.replace("]","")
        return s
    def dfs(n,l):
        a1,a2 = in1[n]
        if a1 in l:
            return
        l.append(a1)
        if a1==a2:
            st1.append(a1)
            return 
        else:
            st1.append(a1)
            dfs(a2-1, l.copy())    
    
    for _ in range(int(input())):
        in1 = list(map(int, del_s(input()).split(",")))
        in2 = in1.copy()
        in1 = [ [i+1,in1[i]] for i in range(len(in1)) ]
        o = []
        for i in range(len(in2)):
            st1 = []
            dfs(i,[])
            o.append(st1)
    
        out = []
        for i in range(len(o)):
            if set(o[i]) not in [ set(ii) for ii in out ]:
                out.append(o[i])
    
        print(out)
    
    """
    4
    [1, 6, 7, 4, 2, 3, 5, 8]
    [1, 6, 3, 4, 7, 2, 5, 8]
    [1, 6, 5, 4, 7, 3, 2, 8]
    [1, 6, 8, 4, 7, 3, 5, 2]
    
    [[1], [2, 6, 3, 7, 5], [4], [8]]
    [[1], [2, 6], [3], [4], [5, 7], [8]]
    [[1], [2, 6, 3, 5, 7], [4], [8]]
    [[1], [2, 6, 3, 8], [4], [5, 7]]
    """
    ```
    

## DOM_108

- 統計答案得分
    
    ```python
    for _ in range(int(input())):
        in1 = input()
        out = 0
        b = 0
        for i in in1:
            if i == "O":
                b+=1
                out += b
            else:
                b=0
        print(out)
    
    """
    5
    OOXXOXXOOO
    OOXXOOXXOO
    OXOXOXOXOXOX
    OOOOOOOOOO
    OOOOXOOOOX
    
    """
    ```
    
- 保齡球計分
    
    ```python
    # like Fib !!!
    
    def f(i):
        if in1[i] == "/":
            n = 0
            if len(in1) > i+1:
                n += 10 if in1[i+1] == "X" else f(i+1)
            return (10-f(i-1))+n
        elif in1[i] == "X":
            n = 0
            if len(in1) > i+1:
                n += 10 if in1[i+1] == "X" else f(i+1)
            if len(in1) > i+2:
                if in1[i+2] == "X":
                    n += 10
                elif in1[i+2] == "/":
                    n += 10-f(i+1)
                else:
                    n += f(i+2)   
            return 10+n
        else:
            return int(in1[i])   
    for _ in range(int(input())):
        in1 = list(map(str, input().split()))    
        d = [ [0,0] for i in range(10)]
        k = in1.copy()
        for i in range(9):
            l = in1.pop(0)
            if l=="X":
                d[i] = [" ",l]
            else:
                d[i][0] = l
                d[i][1] = in1.pop(0)
        d[-1] = [ i for i in in1 ]
        in1 = k.copy()
        if len(d[-1]) == 3:
            k = k[:-2] if k[-3]=="X" else k[:-1]
        m = [ f(i) for i in range(len(k)) ]
        print(sum(m))
    ```
    
- 包含某個數字
    
    ```python
    for _ in range(int(input())):
        in1 = list(map(int, input().split()))
        lst = list(map(str, range(in1[0],in1[1]+1)))
        lst = [ i for i in lst if str(in1[2]) in i ]
        print(len(lst))
    
    """
    3
    3 17 3
    0 20 0
    0 150 17
    """
    ```
    
- 求餘數
    
    ```python
    for _ in range(int(input())):
    
        in1 = list(map(int, input().split()))
        print((in1[0]**in1[1]) % in1[2])
    
    """
    2
    10 2009 9
    2 99 5
    
    3
    3 18132 17
    17 1765 3
    65535 65535 36123
    """
    ```
    
- DNA序列
    
    ```python
    for _ in range(int(input())):
        in1 = list(map(int,input().split()))
        in2 = []
        for i in range(in1[0]):
            in2.append(list(input().strip()))
    
        for i in range(in1[1]):
            k = [in2[ii][i] for ii in range(in1[0])]
            dit = {}
            for j in k:
                dit[j] = dit.get(j,0)+1
    
            d = list(dit.items())
            d.sort(key=lambda x:x[1], reverse=True)
            v = set([ i[1] for i in d ])
            w = [ i[0] for i in d ]
            if len(v) == 1:
                for j in list("ACGT"):
                    if j in w:
                        print(j, end="")
                        break
            else:
                print(d[0][0],end="")
                
        print()
    """
    2
    5 8
    TATGATAC
    TAAGCTAC
    AAAGATCC
    TGAGATAC
    TGAGATAC 
    4 10
    ACGTACGTAC
    CCGTACGTAG
    GCGTACGTAT
    TCGTACGTAA
    
    2
    6 10
    ATGTTACCAT
    AAGTTACGAT
    AACAAAGCAA
    AAGTTACCTT
    AAGTTACCAA
    TACTTACCAA
    4 9
    GAGCACGTC
    CATCACGTG
    GCTTACGTT
    CCGTATGTA 
    
    TAAGATAC
    ACGTACGTAA
    
    AAGTTACCAA
    CAGCACGTA
    """
    ```
    
- 循環小數
    
    ```python
    """
    3
    76 25
    5 43
    1 397
    """
    for _ in range(int(input())):
        a,b = list(map(int,input().split()))
        lst = []
        out = []
        while 1:
            out.append(str(a//b))
            s = a%b
            a = s*10
            if s == 0:
                print(out[0], end=".")
                print("".join(out[1:])+"(0)")
                break
            elif s in lst:
                idx = lst.index(s)
                print(out[0],end="")
    
                if idx != 0:
                    print("."+"".join(out[1:idx+1]),end="")
                    print("("+"".join(out[idx+1:])+")")
                else:
                    print(".("+"".join(out[1:])+")")
                break
            elif len(lst)==50:
                print(out[0],end=".")
                print("("+"".join(out[1:])+"...)")
                break
            lst.append(s)
    ```
    
- 著色問題
    
    ```python
    # !!!  https://www.techiedelight.com/zh-tw/greedy-coloring-graph/
    
    class Graph:
        def __init__(self, edges, n):
            self.adjList = [ [] for _ in range(n) ]
            
            for (src, dest) in edges:
                self.adjList[src].append(dest)
                self.adjList[dest].append(src)
    
    def colorGraph(graph, n):
        result = {}
        for u in range(n):
            assigned = set([ result.get(i) for i in graph.adjList[u] if i in result ])
            color = 1
            for c in assigned:
                if color != c:
                    break
                color = color+1
            print(color)
            result[u] = color
            print(result)
        return result
    
    node_number = int(input())
    edge_number = int(input())
    edges = []
    for i in range(edge_number):
        edges.append(tuple(map(int,input().split())))
    graph = Graph(edges, node_number)
    result = colorGraph(graph, node_number)
    
    """
    color_number = len(set(result.values()))
    if color_number >2:
        print("F")
    else:
        print("T")
    """
    
    """
    2
    4
    4
    0 1
    1 2
    2 3
    3 0
    5
    10
    0 1
    0 2
    0 3
    0 4
    1 2
    1 3
    1 4
    2 3
    2 4
    3 4
    """
    ```
    
- 數字迷宮
    
    ```python
    """
    2
    4
    5
    0 3 1 2 9
    7 3 4 9 9
    1 7 5 5 3
    2 3 4 2 5
    1
    6
    0 1 2 3 4 5
    """
    
    for _ in range(int(input())):
        x = int(input())
        y = int(input())
        graph_val = []
        graph_cost = [[ 0 for i in range(y)] for j in range(x)]
        graph_visited = [[ 0 for i in range(y)] for j in range(x)]
        for i in range(x):
            data = list(map(int, input().split()))
            graph_val.append(data)
        queue = [(0,0)]
        while queue:
            qx,qy = queue.pop(0)
            if graph_visited[qx][qy]==0:
                graph_visited[qx][qy]=1
                gx = 9999999 if qx-1<0 else graph_cost[qx-1][qy]
                gy = 9999999 if qy-1<0 else graph_cost[qx][qy-1]
                if not (gx==gy==9999999):
                    graph_cost[qx][qy] = min(gx,gy)+graph_val[qx][qy]
                else:
                    graph_cost[qx][qy] = graph_val[qx][qy]
                if qx+1 < x:
                    queue.append([qx+1,qy])
                if qy+1 < y:
                    queue.append([qx,qy+1])
        print(graph_cost[-1][-1])
    ```
    

## DOM_109

- 找出最大和第二大的數字
    
    ```python
    for _ in range(int(input())):
        lst = list(map(int, input().split()))
        for i in range(2):
            a1 = lst.pop(lst.index(max(lst)))
            print(a1, end=" ")
        print()
    """
    3 
    1 2 3 4 10 9 8 7 
    10 11 12 99 1 2 3 
    1 2 1 2 1 2
    """
    ```
    
- 打印機
    
    ```python
    for _ in range(int(input())):
        in1 = input()
        n = in1[::-1]
        d = sum([ 10**i for i in range(len(n)) if n[i]=="4" ])
        print(int(in1)-d,d)
    ```
    
- 時間計算
    
    ```python
    """
    2
    12/11/2020
    01/01/2019
    30/11/2020
    01/12/2019
    """
    for _ in range(int(input())):
        lst2 = list(map(int,input().split("/")))
        lst1 = list(map(int,input().split("/")))
        y = lst2[2]-lst1[2]
        if lst2[1]<lst1[1]:
            y-=1
        elif lst2[1] == lst1[1] and lst2[0] < lst1[0]:
            y-=1
        
        print(y)
    ```
    
    ```
    """
    3
    8
    48
    126
    """
    for _ in range(int(input())):
        n = int(input())
        if n==1:
            print(1)
            continue
        m = 1
        lst = []
        for i in range(9,1,-1):
            while n%i==0:  # ex:100 455 (55)
                n //=i
                m *= i
                lst.append(str(i))
        if len(lst)==0 or n>1:
            print(-1)
        else:
            print("".join(lst[::-1]))
    ```
    
- 數字相乘
    
    ```python
    """
    3
    8
    48
    126
    """
    for _ in range(int(input())):
        n = int(input())
        if n==1:
            print(1)
            continue
        m = 1
        lst = []
        for i in range(9,1,-1):
            while n%i==0:  # ex:100 455 (55)
                n //=i
                m *= i
                lst.append(str(i))
        if len(lst)==0 or n>1:
            print(-1)
        else:
            print("".join(lst[::-1]))
    ```
    
- 迴文
    
    ```python
    def MMS(i,n):
        if i==0:
            return n
        if lst[i-1] > n+lst[i-1]:
            MMS(i-1,lst[i-1])
        else:
            MMS(i-1, lst[i-1]+n)
        
    
    lst = list(map(int,"-2 -3 4".split()))
    print(MMS(len(lst), 0))
    ```
    
- 最大子數列問題
    
    ```python
    # ! ! ! https://zh.wikipedia.org/zh-tw/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98
    
    def max_subarray(A):
        max_ending_here = max_so_far = A[0]
        for x in A[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    
    for _ in range(int(input())):
        lst = list(map(int,input().split()))
        print(max_subarray(lst))
    
    """
    6
    1 2
    10 -1 -1 2
    216 2
    -2 1 -3 4 -1 2 1 -5 10
    -2 -3 4 -1 -2 1 5 -3
    -2 3 4 1 2 1 5 -3
    """
    ```
    
- 錄音帶
    
    ```python
    # ! itertools
    
    import itertools
    
    while 1:
        try:
            in1 = list(map(int,input().split()))
            n = in1[0]
            c = in1[2:]
            v = 0
            for i in range(1,len(c)+1):
                k = [sum(ii) for ii in list(itertools.combinations(c,i))]
                for j in k:
                    if j <= n:
                        v = max(v,j)
            print(v)
        except:
            break
    ```
    
- 特殊郵件
    
    ```python
    """ ???
    for i in range(1,n+1): # YES
            visited = [0]*n
            k = i-1
            cnt = 0
            mx = 0
            while not visited[k]:
                visited[k] = 1
                k = f[k]
                cnt+=1
            out.append([i,cnt])
    
    def dfs(i):  # !!!! NO
        if not visited[i-1]:
            visited[i-1]=1
            if i in dit:
                dfs(dit[i])
    """
    def dfs(i):  # !!!! NO
        if not visited[i-1]:
            visited[i-1]=1
            if i in dit:
                dfs(dit[i])
    for _ in range(int(input())):
        dit = {}
        n = int(input())
        for i in range(n):
            u,v = list(map(int, input().split()))
            dit[u] = v
        out = []
        for i in range(1,n+1):
            visited = [0]*n
            dfs(i)
            v = [i,len([ ii for ii in visited if ii ])]
            out.append(v)
        out.sort(key=lambda x:[x[1],-x[0]], reverse=True)
    
        print(out[0][0])
    
    """
    3
    3
    1 2
    2 3
    3 1
    4
    1 2
    2 1
    4 3
    3 2
    5
    1 2
    2 1
    5 3
    3 4
    4 5
    """
    ```
    

## DOM_111_1130

- A1：
    
    ```python
    y = int(input())
    print(y-1911)
    ```
    
- A2：
    
    ```python
    while 1:
        n = int(input())
        if n==0:
            break
    
        if n % 400==0:
            print("a leap year")
        elif n%4==0 and n%100!=0:
            print("a leap year")
        else:
            print("a normal year")
    ```
    
- B：
    
    ```python
    n, m = list(map(int, input().split()))
    
    if m > n:
        print(m-n)
    else:
        k = 200-n
        k+= m
        print(k)
    ```
    
- C：
    
    ```python
    s = input()
    s = s[::-1]
    print(int(s))
    ```
    
- D：
    
    ```python
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    k = []
    for i in range(n):
        if l[i] not in l[i+1:]:
            k.append(l[i])
    
    print(len(k))
    for i in k:
        print(i, end=" ")
    ```
    
- E：
    
    ```python
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    dit = {}
    for i in range(n):
        dit[l[i]] = dit.get(l[i], 0)+1
    
    for i in dit:
        print(i, dit[i])
    ```
    
- F：
    
    ```python
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    dit = {}
    for i in range(n):
        dit[l[i]] = dit.get(l[i], 0)+1
    
    for i in dit:
        print(i, dit[i])
    ```
    
- G：
    
    ```python
    for _ in range(int(input())):
        s = input()
        l = []
        for i in s:
            if "A"<=i<="Z":
                l.append(i)
            else:
                l[-1]+=i
        for i in l:
            print(i[0]*int(i[1::]), end="")
        print()
    ```
    
- H：
    
    ```python
    while 1:
        m = list(map(str,input().split()))
    
        if m[0]=="0":
            break
    
        n,s = m[0],m[1]
    
        s = list(s)
        n = int(n)
        n = len(s)//n
    
        k = []
        g=""
        while s:
            g+=s.pop(0)
            if len(g) == n:
                k.append(g)
                g=""
        for i in k:
            print(i[::-1],end="")
        print()
    ```
    
- I：
    
    ```python
    s = input()
    dit = {}
    for i in s:
        i = ord(i)
        dit[i] = dit.get(i, 0)+1
    lst = list(dit.items())
    lst.sort(key=lambda x:(x[1],-x[0]))
    for n,m in lst:
        print(n,m)
    ```
    
- J：
    
    ```python
    # !!!
    
    for _ in range(int(input())):
        n,m = list(map(int, input().split()))
        for i in range(n if n!=1 else 2,m+1):
            for j in range(2, int(i**0.5)+1):
                if i%j == 0:
                    break
            else:
                print(i)
    ```
    
- K：
    
    ```python
    # !!!
    
    def f(n):
        k=0  #存找到的因數
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                k=i
                break
        if k!=0:
            l.append(k)
            f(n//k)
        else:
            l.append(n)
    
    k = 0
    while 1:
        a = int(input())
        if a==0:
            break
        if a==1:
            print(a,":",0)
        else:
            l = []
            f(a)
            l = set(l)
            k = len(l)
            print(a,":",k)
    ```
    
- L：
    
    ```python
    num=0
    for i in range(1,int(input())+1):
        b = str(bin(i))
        for j in b:
            if j == "1":
                num+=1
    print(num)
    ```
    
- M：
    
    ```python
    # !!!
    
    def f(n):
        global lst
        if n == 1:
            return
        if len(lst)==2:
            lst = lst[::-1]+lst
        else:
            lst = lst+lst[::-1]
    
        for i in range(len(lst)):
            if i < len(lst)/2:
                lst[i] = "0" + lst[i]
            else:
                lst[i] = "1" + lst[i]
        f(n-1)
    
    n = int(input())
    lst = ["1","0"]
    
    f(n)
    for i in lst:
        print(i)
    ```
    
- N：LIS  ***
    
    ```python
    _ = int(input())
    lst = list(map(int, input().split()))
    n = len(lst)
    length = [ 1 for i in range(n) ] #dp
    
    for i in range(n):
        for j in range(i):
            if lst[j] < lst[i]:
                length[i] = max(length[i], length[j]+1)
    
    print(max(length))
    ```
    
- O：*Coin Change Problem ****
    
    ```python
    m = list(map(int,input().split()))[1]
    c = list(map(int,input().split()))
    
    dp = [ 0 for i in range(m+1) ]
    dp[0] = 1
    for i in range(len(c)):
        for j in range(c[i], m+1):
            dp[j] += dp[j-c[i]]
    dp[0] = 0
    print(dp[m])
    ```
    
- P：*PreOrder and InOrder to PostOrder* ***
    
    ```python
    class node:
        def __init__(self, data,left=None,right=None):
            self.left = left
            self.right = right
            self.data = data
    
    def buildTree(preorder,inorder):
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = node(inorder[idx])
            root.left = buildTree(preorder, inorder[:idx])
            root.right = buildTree(preorder, inorder[idx+1:])
            return root
    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            res.append(root.data)
    
    preorder,inorder = list(map(list,input().split()))
    root = buildTree(preorder, inorder)
    res = []
    postorder(root)
    print("".join(res))
    ```
    
- Q：*tree*
    
    ```python
    def dfs_D(x):
        for i in range(n):
            if tree[x][i]:
                d[i] = d[x]+1
                dfs_D(i)
    def dfs_H(x):
        h = 0
        for i in range(n):
            if tree[x][i]:
                h = max(h, dfs_H(i)+1)
        return h
    
    n = int(input())
    d = [ 0 for i in range(n) ]
    tree = [[ 0 for i in range(n) ] for j in range(n)]
    for _ in range(n):
        n1,n2,n3 = list(map(int,input().split()))
        if n2 != -1:
            tree[n1][n2] = 1
        if n3 != -1:
            tree[n1][n3] = 1
    
    dfs_D(0)
    info     = { "ID":0,"F":0,"K":0,"D":0,"H":0 }
    info_set = [ info.copy() for i in range(n) ]
    for i in range(n):
        info_set[i]["ID"] = i
    
        for ii in range(n):
            if tree[ii][i] == 1:
                info_set[i]["F"] = ii
                break
        else:
            info_set[i]["F"] = -1
        info_set[i]["K"] = len([ ii for ii in range(n) if tree[i][ii]==1 ])
        info_set[i]["D"] = d[i]
        info_set[i]["H"] = dfs_H(i)
    
        print("node %d: parent = %d, degree = %d, depth = %d, height = %d,"
              %(
                info_set[i]["ID"],
                info_set[i]["F"],
                info_set[i]["K"],
                info_set[i]["D"],
                info_set[i]["H"]
                ))
    ```
    

[DOM_10](https://www.notion.so/DOM_10-66cde00e81c94940ab840ed2ecf32fe2?pvs=21) 

[DOM_103](https://www.notion.so/DOM_103-4a2e5b5e185c4a9b81ce9cdfbbdae623?pvs=21) 

[DOM_104](https://www.notion.so/DOM_104-feec060b3fa2408589620a08793c6991?pvs=21) 

[DOM_105](https://www.notion.so/DOM_105-401c69e9f0c14eff96400c56fecde27b?pvs=21) 

[DOM_106](https://www.notion.so/DOM_106-5ec9a912f79e4fe1ac17623cfd0a8ddb?pvs=21) 

[DOM_107](https://www.notion.so/DOM_107-d91e3069e9f24ff7a1b1961b30172411?pvs=21) 

[DOM_108](https://www.notion.so/DOM_108-7d9a2188971149e185d83ddaa2af56b9?pvs=21) 

[DOM_109](https://www.notion.so/DOM_109-b66919e0bec74f08875bea1c546aa1aa?pvs=21) 

[DOM_111_1130](https://www.notion.so/DOM_111_1130-467c3ed8980842c4ad38d9e70bad2116?pvs=21)
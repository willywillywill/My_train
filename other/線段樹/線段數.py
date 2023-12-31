n = 10
segment_tree = []
lst = list(map(int,"3 2 4 5 6 8 1 2 9 7".split()))

def modify(val,pos,l=0,r=n,idx=0):
    if l==r:
        lst[pos] = val
        return
    m = (l+r)//2
    if pos >= l and pos <= m:
        modify(val, pos, l, m, 2*idx+1)
    else:
        modify(val, pos, m+1, r, 2*idx+2)

def build(l=0,r=n,idx=0):
    segment_tree.append(lst[l:r+1])
    if l==r:
        return
    m = (l+r)//2
    build(l,m,2*idx+1)
    build(m+1,r,2*idx+2)

def query(l,r,L,R,idx):
    if l<=L and R<=r:
        return lst[idx]
    m = (L+R)//2
    if r <= m:
        return query(l,r,L,m, 2*idx+1)
    elif l > m:
        return query(l,r,m+1,R,2*idx+2)
    else:
        return max(
            query(l,r,L,m, 2*idx+1),
            query(l,r,m+1,R,2*idx+2)
                   )



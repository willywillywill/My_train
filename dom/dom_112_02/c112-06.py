def f_s(s):
    s = s.replace(",","")
    s = s.replace(".","")
    if s==s.lower():
        return True
    elif s==s.upper():
        return True
    elif s[0] == s[0].upper() and s[1:]==s[1:].lower():
        return True
    return False



s = list(map(f_s,input().split()))
print(int(all(s)))
def isUnique(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = c
        else:
            return False;
    return True;

print(isUnique("hello"));

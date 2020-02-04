def isPermutation(s1, s2):
    if len(s1) != len(s2):
        return False;
    
    d = {};
    for c in s1:
        if c not in d:
            d[c] = 1;
        else:
            d[c] += 1;

    for c in s2:
        if c not in d:
            return False;
        else:
            d[c] -= 1;
            if d[c] < 0:
                return False;

    return True;

print(isPermutation('hello', 'elleh'));

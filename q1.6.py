def compress(s1):
    d = {}
    compressible = False;

    for c in s1:
        if c not in d:
            d[c] = 1;
        else:
            d[c] += 1;
            if d[c] >= 3:
                compressible = True;

    if not compressible:
        return s1;
    
    new_str = '';
    for key in d:
        new_str += key + str(d[key]);

    return new_str;

print(compress('aabcCC'));

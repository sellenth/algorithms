def urlify(s1):
    s2 = '';
    for c in s1:
        if c == ' ':
            s2 += '%20';
        else:
            s2 += c;
    return s2;

print(urlify('totally wow'));

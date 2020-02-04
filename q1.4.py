def isPalindrome(s1):
    d = {}
    for c in s1:
        if c is not ' ':
            if c not in d:
                d[c] = 1;
            else:
                d[c] += 1;

    found_single = False;

    for key in d:
        if d[key] % 2 != 0:
            if found_single == False:
                found_single = True;
            else:
                return False;

    return True;

print(isPalindrome('racec ar'));

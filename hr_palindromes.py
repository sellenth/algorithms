def canConstructPalindrome(s, m):
    d = {};
    for c in s:
        if c not in d:
            d[c] = 1;
        else:
            d[c] += 1;

    if m % 2:
        num_unique = m // 2;
        found = 0;
        remove = [];
        for key in d:
            if d[key] >= 2:
                remove.append(key);
                found += 1;
        for r in remove:
            del d[r];
        if len(d) > 0:
            if found >= num_unique:
                return 'Yes';
        else:
            return 'No';

    if m % 2 == 0:
        num_unique = m // 2;
        found = 0;
        for key in d:
            if d[key] >= 2:
                found += 1;
        if found >= num_unique:
            return 'Yes';
        else:
            return 'No';

print(canConstructPalindrome('abacdce', 4))
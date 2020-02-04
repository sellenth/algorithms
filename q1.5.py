def oneEdit(s1, s2):
    d = {}
    for c in s1:
        if c not in d:
            d[c] = 1;
        else:
            d[c] += 1;

    num_edits = 0;

    for c in s2:
        if c not in d:
            num_edits += 1;

    diff = len(s1) - len(s2);
    if diff > 0:
        num_edits += diff;

    return num_edits <= 1;

print(oneEdit('wl', 'wlaa'));


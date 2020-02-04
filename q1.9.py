def isRot(s1, s2):
    char = s1[0];
    idx = [];

    #strings can't be rotations if not the same length
    if len(s1) != len(s2):
        return False;

    for i in range(len(s2)):
        if s2[i] == char:
            idx.append(i);

    #strings can't be rotations if missing common character
    if len(idx) == 0:
        return False;


    for i in idx:
        test = s2[i:] + s2[0:i]

        if test not in s1:
            return False

    return True;

print(isRot('waterbottle', 'ttlewaterbo'));

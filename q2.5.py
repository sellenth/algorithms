import ll as lib

#s1 = lib.ll([7, 1, 6]);
#s2 = lib.ll([5, 9, 2]);
s1 = lib.ll([6, 1, 7]);
s2 = lib.ll([2, 9, 5]);

def add(s1, s2):
    cur1 = s1.root;
    cur2 = s2.root;

    val1 = []
    val2 = []

    while cur1:
        #val1.insert(0, cur1.get_val());
        val1.append(cur1.get_val());
        cur1 = cur1.nxt;

    while cur2:
        #val2.insert(0, cur2.get_val());
        val2.append(cur2.get_val());
        cur2 = cur2.nxt;
    
    val1 = ''.join(map(str, val1));
    val2 = ''.join(map(str, val2));

    return int(val1) + int(val2);



s1.print();
print('+');
s2.print();

print(add(s1, s2));


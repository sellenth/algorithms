import ll as lib;

l1 = lib.ll([1, 2]);

def reverse(l):
    curr = l.root;
    nxt  = curr.nxt;
    curr.nxt = None;
    tmp  = None;

    while curr:
        if nxt == None:
            break;
        tmp = nxt.nxt;
        nxt.nxt = curr;
        curr = nxt;
        nxt = tmp;

    l.root = curr;
    return;

reverse(l1);
l1.print();

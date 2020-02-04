import ll as lib

linked1 = lib.ll([1, 2, 3]);
linked2 = lib.ll([0]);
linked2.root = linked1.root.nxt;

def intersect(l1, l2):
    d = {}
    curr = l1.root;

    while curr:
        if curr not in d:
            d[curr] = 1;
        curr = curr.nxt;

    curr = l2.root;

    while curr:
        if curr in d:
            return curr;
        curr = curr.nxt;

print(intersect(linked1, linked2).get_val());


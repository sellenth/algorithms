import ll as lib

linked = lib.ll([1, 2, 3, 4, 2, 5, 2]);

def remove_dup(l):

    curr = l.root;
    found = {};

    found[curr.get_val()] = 1;

    while curr.nxt:
        if curr.nxt.get_val() not in found:
            found[curr.nxt.get_val()] = 1;
            curr = curr.nxt;
        else:
            #remove node
            curr.nxt = curr.nxt.nxt;



linked.print();
remove_dup(linked);
linked.print();


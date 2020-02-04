import ll as lib

linked = lib.ll([3, 5, 8, 5, 10, 2, 1]);

def remove_node(curr, nxt):
    curr.nxt = nxt.nxt;
    return nxt;

def partition(l, x):
    curr = l.root;
    stop = curr;

    while curr.nxt:
        if curr.nxt.get_val() < x:
            stop = curr.nxt;
            while stop.nxt and stop.nxt.get_val() < x:
                stop = stop.nxt;
            tmp = curr.nxt;
            curr.nxt = stop.nxt;
            stop.nxt = l.root
            l.root = tmp;
        else:
            curr = curr.nxt;


linked.print();
partition(linked, 8);
linked.print();


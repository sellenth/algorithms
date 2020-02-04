import ll as lib

linked = lib.ll([1, 2, 3, 4]);

r = linked.root
r.nxt.nxt.nxt.nxt = r;

def find_loop(l):
    slow = l.root;
    step = 2;
    fast = slow;

    while True:
        tmp = fast;
        for i in range(step):
            fast = fast.nxt;
        step += 1;
        slow = slow.nxt;

        if tmp == fast or fast == slow:
            return slow;

print((find_loop(linked)).get_val());

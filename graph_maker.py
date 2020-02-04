class Node:
    incoming = None;
    outgoing = None;
    key = '';

    def __init__(self, key):
        self.incoming = [];
        self.outgoing = [];
        self.key = key;

    def add_incoming(self, n):
        self.incoming.append(n);

    def add_outgoing(self, n):
        self.outgoing.append(n);

projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];
depend = [('b', 'a'), ('c', 'a'), ('f', 'c'), ('f', 'b'), ('a', 'e'), ('d', 'g')];

all_nodes = {};

for p in projects:
    all_nodes[p] = Node(p);

for pair in depend:
    all_nodes[pair[1]].add_incoming(pair[0]);
    all_nodes[pair[0]].add_outgoing(pair[1]);


order = [];

#nodes get removed from the graph when they've been
#   explored and have no incoming edges

#while there are still nodes in the graph
while all_nodes:
    remove = [];
    for key in all_nodes:
        if len(all_nodes[key].incoming) == 0:
            remove.append(key);
            order.append(key);
            for update in all_nodes[key].outgoing:
                all_nodes[update].incoming.remove(key);

    for r in remove:
        del all_nodes[r];

print(order);



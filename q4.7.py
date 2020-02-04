#class Node:
#    incoming = [];
#    outgoing = [];
#    key = '';
#
#    def __init__(self, key):
#        self.key = key;
#
#    def add_outgoing(self, n):
#        self.outgoing.append(n);
#
#    def add_incoming(self, n):
#        self.incoming.append(n);
#
#all_nodes = [];

import networkx as nx


projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];
depend = [('b', 'a'), ('c', 'a'), ('f', 'c'), ('f', 'b'), ('a', 'e'), ('d', 'g')];
impossible_depend = [('b', 'a'), ('c', 'a'), ('f', 'c'), ('f', 'b'), ('a', 'e'), ('d', 'g'), ('e', 'f')];

G = nx.DiGraph();

for i in range(len(depend)):
    depend[i] = (depend[i][1], depend[i][0]);
G.add_edges_from(depend);

build_order = []; 
removed = [];

while(len(G.nodes) > 0):
    found = False;
    for i in G.nodes():
        if len(G.adj[i]) == 0:
            found = True;
            build_order.append(i)
            removed.append(i);
    if found == False:
        print("can't build");
        exit();


    for i in removed:
        G.remove_node(i);
    removed = [];

print(build_order);



import ll as lib

linked = lib.ll([1, 2, 3, 4, 2, 5, 2]);

def del_mid(node):
    if node.nxt:
        node.set_val(node.nxt.get_val());
        if node.nxt.nxt:
            del_mid(node.nxt);
        else:
            node.nxt = None;
   

linked.print();

node = linked.root.nxt.nxt;
print(node.get_val());
del_mid(node);

linked.print();


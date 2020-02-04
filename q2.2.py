import ll as lib

linked = lib.ll([1, 2, 3, 4, 2, 5, 2]);

def last(node, k, res):
    count = 0;
    if node == None:
        return 1;
    count += last(node.nxt, k, res);
    if (count == k):
        res[0] = node.get_val();
    count += 1;
    return count;



linked.print();
result = [0];
last(linked.root, 2, result);
print(result);


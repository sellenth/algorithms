class Node():
    val = None;
    left = None;
    right = None;

    def __init__(self, v):
        self.val = v;

    def add_child(self, v):
        new = Node(v);
        if v < self.val:
            if self.left == None:
                self.left = new;
            else:
                self.left.add_child(v);

        elif v >= self.val:
            if self.right == None:
                self.right = new;
            else:
                self.right.add_child(v);

def in_order(n):

    if n == None:
        return;
    in_order(n.left);
    print(n.val);
    in_order(n.right);

def pst_order(n):
    if n == None:
        return;
    pst_order(n.left);
    pst_order(n.right);
    print(n.val);

def pre_order(n):
    if n == None:
        return;
    print(n.val);
    pre_order(n.left);
    pre_order(n.right);




t = Node(3);
t.add_child(2);
t.add_child(4);
t.add_child(1);


in_order(t);
print();
pre_order(t);
print();
pst_order(t);

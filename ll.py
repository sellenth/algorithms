class Node:
    nxt = None;
    data = -1; 

    def __init__(self, n):
        self.nxt = None;
        self.data = n;

    def add_node(self, n):
        self.nxt = Node(n);

    def get_val(self):
        return self.data;

    def set_val(self, n):
        self.data = n;

class ll:
    root = None;

    def __init__(self, n):
        self.root = n;

    def __init__(self, l):
        if l == None:
            self.root = None;
        else:
            for i in l[::-1]:
                self.add_link(i)

    def add_link(self, n):
        tmp = Node(n);
        tmp.nxt = self.root;
        self.root = tmp;

    def remove_link(self):
        if self.root == None:
            print("remove_link error");
            return None;
        tmp = self.root;
        self.root = self.root.nxt;
        return tmp;


    def print(self):
        cur = self.root;
        while cur:
            print(cur.get_val(), end=' ');
            cur = cur.nxt;
        print();

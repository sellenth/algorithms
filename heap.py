class Node:
    val = 0;
    left = None;
    right = None;

    def assign(self, v):
        self.val = v;

    def new_child(self, v, side):
        if (side == 'left'):
            self.left = Node();
            self.left.assign(v)
        elif (side == 'right'):
            self.right = Node();
            self.right.assign(v)

class Heap:
    root = None
    levels = 0;

    def __init__(self, v):
        self.root = Node();
        self.root.assign(v);
        self.levels+=1;

    def display(self):
        print( '\t' * self.levels + str(self.root.val));
        if self.root.left:
            print(self.root.left.val, end='');
            print('\t', end='');
        else:
            print('\t', end='')

        print('\t', end='');

        if self.root.right:
            print(self.root.right.val, end='');
            print('\t', end='');
        else:
            print('\t', end='')

    def insert(self, v):
        curr = self.root;
        if (v <= curr.val):
            if curr.left == None:
                curr.new_child(v, 'left');
        elif (v > curr.val):
            if curr.right == None:
                curr.new_child(v, 'right');


h = Heap(5);
h.insert(3);
h.insert(7);
h.display();

class node():
    dat = None;
    min = None;
    nxt = None;

    def __init__(self, v):
        self.dat = v;
        self.min = v;
        self.nxt = None;

class min_stack():
    top = None;

    def __init__(self, v):
        self.top = node(v);

    def push(self, v):
        new = node(v);
        new.nxt = self.top;
        if v < self.top.min:
            new.min = v;
        else:
            new.min = self.top.min;
        self.top = new;


s = min_stack(3);
s.push(4);
s.push(5);
print(s.top.min);



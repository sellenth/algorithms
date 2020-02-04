import ll as linked

class Stack:
    top = None;
    cap = 0;

    def __init__(self, v):
        if v == None:
            self.top = linked.ll(None);
        else:
            self.top = linked.ll([v]);
            self.cap = 1;

    def peek(self, v):
        return self.top.root.get_val();

    def is_empty(self):
        if self.top.root == None:
            return True;
        return False;

    def pop(self):
        if self.is_empty():
            print("Can't pop, stack is empty");
            return None;
        self.cap -= 1;
        return self.top.remove_link();

    def push(self, v):
        self.cap += 1;
        self.top.add_link(v);

    def print_all(self):
        while not self.is_empty():
            print((self.pop()).get_val())

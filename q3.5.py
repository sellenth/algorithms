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

    def peek(self):
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

class min_stack:
    s = None;
    tmp = None;

    def __init__(self, v):
        self.s = Stack(v);
        self.tmp = Stack(None);

    def peek(self):
        return self.s.peek();

    def pop(self):
        return self.s.pop();

    def push(self, v):
        if self.s.is_empty():
            self.s.push(v);

        top = self.s.pop().get_val();

        while top < v:
            self.tmp.push(top);
            if self.s.is_empty():
                break;
            else:
                top = self.s.pop().get_val();

        self.s.push(v);
        while not self.tmp.is_empty():
            self.s.push(self.tmp.pop().get_val());

    def print_all(self):
        self.s.print_all();


ms = min_stack(3);
ms.push(4);
ms.push(5);
ms.print_all();

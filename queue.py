import ll as linked

class Queue():
    front = None;
    back = None;

    def __init__(self, v):
        self.front = linked.Node(v);
        self.back = self.front;

    def push(self, v):
        self.back.add_node(v);
        self.back = self.back.nxt;

    def pop(self):
        if self.front == None:
            print("pop error, no node to return");
            return None;
        tmp = self.front;
        self.front = tmp.nxt;
        return tmp;

    def peek(self):
        return self.front.get_val();

    def is_empty(self):
        if self.front == None:
            return True;
        return False;

    def print_all(self):
        while not self.is_empty():
            print((self.pop()).get_val())

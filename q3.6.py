import ll as linked

class Shelter():
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
    #extended the queue. dogs are pos, cats neg

    def pop_neg(self):
        tmp = self.front;
        if tmp.get_val() < 0:
            self.front = tmp.nxt;
            return tmp;

        while tmp.nxt and tmp.nxt.get_val() > 0:
            tmp = tmp.nxt;
        if tmp.nxt == None:
            print("could not pop a negative");
            return None;
        else:
            ret = tmp.nxt
            tmp.nxt = tmp.nxt.nxt;
            return ret;

    def pop_pos(self):
        tmp = self.front;
        if tmp.get_val() > 0:
            self.front = tmp.nxt;
            return tmp;

        while tmp.nxt and tmp.nxt.get_val() < 0:
            tmp = tmp.nxt;
        if tmp.nxt == None:
            print("could not pop a positive");
            return None;
        else:
            ret = tmp.nxt
            tmp.nxt = tmp.nxt.nxt;
            return ret;
            

    def peek(self):
        return self.front.get_val();

    def is_empty(self):
        if self.front == None:
            return True;
        return False;

    def print_all(self):
        while not self.is_empty():
            print((self.pop()).get_val())


s = Shelter(3);
s.push(5)
s.push(8)
s.push(-3)
s.push(-2)
s.push(9)
print(s.pop_neg().get_val());
s.print_all();

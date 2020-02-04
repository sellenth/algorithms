import stack

class my_queue:
    s1 = None;
    s2 = None;

    def __init__(self):
        self.s1 = stack.Stack(None);
        self.s2 = stack.Stack(None);

    def pop(self):
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop().get_val());
        tmp = self.s1.pop();
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop().get_val());

        return tmp;

        

    def push(self, v):
        self.s1.push(v);
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop().get_val());

        while not self.s1.is_empty():
            self.s2.push(self.s1.pop().get_val());

    def print_all(self):
        self.s1.print_all();
        print();
        self.s2.print_all();


q = my_queue();
q.push(1);
q.push(2);
q.push(3);
print(q.pop().get_val());
print(q.pop().get_val());
print(q.pop().get_val());

#s = stack.Stack(1);
#s.push(2);
#s.push(3);
#s.print_all();

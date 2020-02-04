import stack 

class SetOfStacks():
    stacks = [];
    capacity = 4;

    def __init__(self, v):
            self.stacks.append(stack.Stack(v));

    def pop_idx(self, idx):
        if idx < 0 or idx > len(self.stacks):
            print('invalid idx');
            return None;
        else:
            ret = self.stacks[idx].pop();
            if ret == None:
                self.stacks.pop(idx);
                if len(self.stacks) == 0:
                    print('error');
                    return None;
                return self.stacks[idx-1].pop();
            return ret;

    def pop(self):
        ret = self.stacks[-1].pop();
        if ret == None:
            self.stacks.pop();
            if len(self.stacks) == 0:
                print('error');
                return None;
            return self.stacks[-1].pop();
        return ret;

    def push(self, v):
        if self.stacks[-1].cap == self.capacity:
            self.stacks.append(stack.Stack(v));
        else:
            self.stacks[-1].push(v);

s = SetOfStacks(3);
s.push(4);
s.push(3);
s.push(8);
s.push(1);

print();
print(s.pop_idx(0).get_val());

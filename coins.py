amount=4;
denominations=[1,2,3];


def print_mem(m):
    print('\t', end='');
    for i in range(1, len(m[0])):
        print(i, end='\t' * i);
    print();
    for i in m:
        for j in i:
            print(j, end='\t');
        print();

def find_combos(a, d):
    mem = [];

    for v in d:
        mem.append([v] + [0] * a);
    
    for i in range(len(mem)):
        c_val = mem[i][0];
        for target_val in range(1, len(mem[i])):
            x = target_val % c_val;
            num_ways = [];
            
            if i > 0:
                num_ways = list(mem[i-1][target_val]);
                if target_val - c_val > 0:
                    for e in mem[i-1][target_val - c_val]:
                        print(list(e) + [c_val]);
                        num_ways += [list(e) + [c_val]];

            if x == 0:
                num_ways += [[c_val] * (target_val // c_val)];

            mem[i][target_val] = num_ways;

    print_mem(mem);

    print('Number of ways to make ' + str(a) + ': ' + str(len(mem[-1][-1])));
    print(mem[-1][-1]);

find_combos(amount, denominations);
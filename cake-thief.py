#types = [(7, 160), (5, 100), (4, 80), (1, 10)];
types = [(7, 160), (3, 90), (2, 15)]
cap = 20;


def print_mem(m):
    for x in m:
        for v in x:
            print('{:>4}'.format(v), end='')
        print();

def max_duffel_bag(l, cap):
    mem = [];

    l = sorted(l);
    tmp_l = [];

    for (x, y) in l:
        if y == 0:
            print('ignoring valueless cake');
            continue;
        mem.append([x] + [0] * cap);
        tmp_l.append((x,y));
    
    l = tmp_l;

    for i in range(len(l)):
        w = l[i][0]; #weight of current item
        v = l[i][1]; #value of current item

        for j in range(1, len(mem[0])):
            if j >= w: #j current size of knapsack
                if j - w > 0: #if space remains after inserting cake
                    addn = mem[i][j-w]; 
                    #additional value = curr_row's best value at the remaining capacity
                    #or the previous row's best value at the remaining capacity
                    if i > 0:
                        addn = max(addn, mem[i-1][j - w]);
                else:
                    #if there is no remaining weight after inserting cake, can't add additional value
                    addn = 0;
                mem[i][j] = max(v + addn, mem[i-1][j]);
            elif j > 0:
                mem[i][j] = mem[i-1][j];
    
    print_mem(mem);

    i = len(mem) - 1;
    j = len(mem[0]) - 1;

    order = [];

    while i >= 0 and j > 0:
        curr = mem[i][j];
        if i > 0 and curr == mem[i-1][j]:
            i -= 1;
        else:
            order.append(mem[i][0]);
            j -= mem[i][0];
    print(order);

max_duffel_bag(types, cap);
space = [[1,1,0,0,0],
         [0,0,1,0,0],
         [0,0,0,1,1],
         ]

#space = [[1,0,1,1,1],
#         [0,1,1,1,0],
#         [0,0,1,1,0],
#         [0,0,0,0,1],
#         [1,1,0,0,0]
#         ]



n = len(space);
m = len(space[0]);

def inbounds(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False;
    return True;

def valid(x,y):
    return inbounds(x, y) and space[x][y];# == '1';

def find_adj(coords):
    x, y = coords;
    ret = [];
    if valid(x-1, y):
        ret.append((x-1,y));
    if valid(x+1, y):
        ret.append((x+1,y));
    if valid(x, y-1):
        ret.append((x,y-1));
    if valid(x, y+1):
        ret.append((x,y+1));
    return ret;

def find_islands():
    i_count = 0;
    seen = [];
    q = [];

    for i in range(n):
        for j in range(m):
            if valid(i, j) and (i,j) not in q and (i,j) not in seen:
                q.insert(0,(i,j));
                i_count += 1;
            while len(q) != 0:
                curr = q.pop(0);
                seen.insert(0,(curr));
                adj = find_adj(curr);
                for coord in adj:
                    if coord not in seen:
                        q.insert(0, coord);

    return i_count;

print(find_islands());
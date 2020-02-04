arr = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]

def zero(arr):
    n = len(arr);
    m = len(arr[0]);
    coords = [];

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                coords.append([i, j]);

    for i in range(n):
        for c in coords:
            arr[i][c[1]] = 0;

    for j in range(m):
        for c in coords:
            arr[c[0]][j] = 0;


zero(arr);
for l in arr:
    print(l);

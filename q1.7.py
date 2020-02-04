import math

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
arr4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]];

def print_arr(a):
    for l in a:
        print(l);

def rotate(arr):
    n = len(arr);
    for i in range(math.ceil(n / 2)):
        for j in range(n - 1 - (i * 2)):
            prv = arr[i][j + i];
            nxt = arr[j + i][n - 1 - i];
            arr[j + i][n - 1 - i] = prv;

            prv = nxt;
            nxt = arr[n - 1 - i][-1 - j - i];
            arr[n - 1 - i][-1 - j - i] = prv;

            prv = nxt;
            nxt = arr[-1 - j - i][i];
            arr[-1 - j - i][i] = prv;

            prv = nxt;
            nxt = arr[i][j + i];
            arr[i][j + i] = prv;

def rotate_draft(arr):
    n = len(arr);
    for i in range(math.ceil(n / 2)):
        for j in range(n - 1 - (i * 2)):
            print(arr[i][j + i]);
            print(arr[j + i][n - 1 - i]);
            print(arr[n - 1 - i][-1 - j - i]);
            print(arr[-1 - j - i][i]);
            print(arr[i][j + i]);
            print()
        print('--------------');


def rotate1(arr):
    new = [[], [], []];
    n = len(arr);

    for i in range(n):
        for j in range(n):
            new[j].insert(0, arr[i][j]);
    return new;

print_arr(arr);
print()
rotate(arr);
print_arr(arr);

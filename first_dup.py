arr = [2, 1, 3]

for i in range(len(arr)):
    if arr[i] == 0:
        continue;
    elif arr[i] - 1 == i:
        arr[i] = 0;
    else:
        curr = arr[i] - 1;
        if arr[curr] == 0:
            print(arr[i]);
            exit();
        tmp = arr[curr] - 1;
        if arr[tmp] == 0:
            print(arr[curr]);
            exit(); 
        else:
            arr[curr] = 0;
            arr[tmp] = 0;

n = 4;
k = 9;

import math
class Solution:
    
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        arr = list(range(1,n+1))
        while arr:
            p = math.factorial(len(arr) - 1)
            idx =  math.ceil(float(k) / p) - 1
            k = k % p
            ans.append(arr[idx])
            arr.pop(idx)
        return ''.join(str(item) for item in ans) 
        
        

sol = Solution();
print(sol.getPermutation(n, k));

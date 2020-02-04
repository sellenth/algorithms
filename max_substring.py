
#i = [-2,1,-3,4,-1,2,1,-5,4]

#-2
#1
#-3
#-3 4
#-3 4 -1


i = [8,-19,5,-4,20]

def maxSubArray(nums) -> int:
    ans = 0;
    curr = []
    curr_sum = 0;

    for i in range(len(nums)):
        curr.append(nums[i]);
        curr_sum += nums[i]

        if curr_sum < 0:
            curr_sum = 0;
            curr = [];
            continue;
        
        if curr_sum - curr[0] > curr_sum:
            curr_sum -= curr[0]
            curr.pop(0);
        
        if curr_sum > ans:
            ans = curr_sum;
    return ans;


print(maxSubArray(i));

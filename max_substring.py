
#i = [-2,1,-3,4,-1,2,1,-5,4]

-2
1
-3
-3 4
-3 4 -1


i = [8,-19,5,-4,20]

def maxSubArray(nums) -> int:
    curr = [nums[0]];
    curr_sum = nums[0];
    best_sum = curr_sum;
    best = [nums[0]];

    for i in range(len(nums)):
        if curr_sum + nums[i] > curr_sum:
            curr.append(nums[i]);
            curr_sum += nums[i];
            if curr_sum - curr[0] > curr_sum:
                curr.pop(0);
                curr_sum -= curr[0];
            if curr_sum > best_sum:





maxSubArray(i);

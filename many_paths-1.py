#https://leetcode.com/problems/unique-paths/
class Solution:
    goal_x = None;
    goal_y = None;
    num_paths = 0;
    mem = {};

    def dfs(self, x, y):
        if x == self.goal_x and y == self.goal_y:
            self.mem[(x,y)] = 1;
        if x > self.goal_x or y > self.goal_y:
            return 0;
        if (x,y) in self.mem:
           return self.mem[(x,y)];
        
        self.mem[(x,y)] = self.dfs(x+1, y) + self.dfs(x, y+1);
        return self.mem[(x,y)];
        

    def uniquePaths(self, m: int, n: int) -> int:
        self.goal_x = n-1;
        self.goal_y = m-1;
        self.dfs(0, 0);
        return self.mem[(0,0)];

s = Solution();
print(s.uniquePaths(3, 3));
class Solution:
    og = None;
        
    def find_adj(self, coords):
        i = coords[0];
        j = coords[1];
        m = len(self.og);
        n = len(self.og[0]);
        ret = [];
        
        if i - 1 > 0 and self.og[i-1][j] not in ['X', 1]:
            self.og[i-1][j] = 'X';
            ret.append((i-1, j));
        if i + 1 < m and self.og[i+1][j] not in ['X', 1]:
            self.og[i+1][j] = 'X';
            ret.append((i+1, j));
        if j - 1 > 0 and self.og[i][j-1] not in ['X', 1]:
            self.og[i][j-1] = 'X';
            ret.append((i, j-1));
        if j + 1 < m and self.og[i][j+1] not in ['X', 1]:
            self.og[i][j+1] = 'X';
            ret.append((i, j+1));
        
        return ret;
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        self.og = obstacleGrid;
        
        self.og[0][0] = 'X';
        queue = [];
        num_paths = 0;
        
        for pair in self.find_adj((0,0)):
            queue.append(pair);
            
        if len(queue) > 1:
            num_paths += len(queue);
            
        while queue:
            curr = queue.pop(0);
            adj = self.find_adj(curr);
            for pair in adj:
                queue.append(pair);
            if len(adj) > 1:
                num_paths += len(adj);
            
        print(num_paths);

s = Solution();
m = [[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0]];
s.uniquePathsWithObstacles(m);
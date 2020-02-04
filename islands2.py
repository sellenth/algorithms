class Solution:
    g = [];

    def visit_recurse(self, coords):
        x = coords[0];
        y = coords[1];

        if x-1 >= 0 and self.g[x-1][y] == '1':
            self.g[x-1][y] = 'X';
            self.visit_recurse((x-1, y));
        if y-1 >= 0 and self.g[x][y-1] == '1':
            self.g[x][y-1] = 'X';
            self.visit_recurse((x, y-1));
        if y+1 < len(self.g[0]) and self.g[x][y+1] == '1':
            self.g[x][y+1] = 'X';
            self.visit_recurse((x, y+1));
        if x+1 < len(self.g) and self.g[x+1][y] == '1':
            self.g[x+1][y] = 'X';
            self.visit_recurse((x+1, y));

    def numIslands(self, grid):
        self.g = grid;
        num_islands = 0;

        for i in range(len(self.g)):
            for j in range(len(self.g[0])):
                if self.g[i][j] != '1':
                    continue
                num_islands += 1;
                self.g[i][j] = 'X';
                self.visit_recurse((i,j));
        
        return num_islands;

s = Solution();
#print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]));
print(s.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]));
                

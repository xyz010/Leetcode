class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #first let's find the skylines        
        #vertical skyline
        grid_inverted = map(list, zip(*grid))
        vsky = list(map(max,grid_inverted))
        #horizontal skyline
        hsky = list(map(max,grid))
        print vsky, "vertical Skyline"
        print hsky, "horizontal Skyline"
        
        grid_dim = len(grid[0]) #grid symmetrical
        total_sum = 0
        #let's traverse and update the new values to the grid
        for i in range(0,grid_dim):
            for j in range(0,grid_dim):
                new_value = min(hsky[i],vsky[j])
                dif = new_value - (grid[i])[j]
                total_sum += dif
                (grid[i])[j] = new_value
        return total_sum
        

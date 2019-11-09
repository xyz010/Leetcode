class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #for starters lets find the equation of the line created by the first two points
        if (coordinates[1])[0] == (coordinates[0])[0]:
            return False
        else:
            l = ((coordinates[1])[1]-(coordinates[0])[1])/((coordinates[1])[0]-(coordinates[0])[0])
        b = (coordinates[0])[1] - l * (coordinates[0])[0]
        
        #iterate over list and see if the rest of the points belong to the same line
        for i in range(2,len(coordinates)):
            if (coordinates[i])[1] != l * (coordinates[i])[0] + b:
                return False
        return True

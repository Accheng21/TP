import random as rand

class Maze:
    def __init__(self, width=15, height=15, cellSize=15):
        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.wallList = []
        
        self.visited=set()
        self.map = [[0 for i in range(self.size)] for i in range(self.size)]
        
    #I used Randomized Prim's Algorithm here
    def maze(self):
        x = rand.randit(self.width)
        y = rand.randit(self.height)
        currCell = (x,y)    
        self.map[currCell[0]][currCell[1]] = 1
        self.visited.add(currCell)
        wallList = self.getWalls(currCell)

        while (len(wallList) > 0):
            rand_index = rand.randint(len(wallList))
            currCell = wallList[rand_index]
            sides = self.getWalls(currCell)
            visits = 0
            unvisited_Cells = []
            for cell in sides:
                if (cell in self.visited):
                    visits += 1
                elif (cell not in  wallList):
                    unvisited_Cells.append(cell)
            if (visits <= 1):
                self.map[currCell[0]][currCell[1]] = 1 #make the passages 1
                self.visited.add(currCell)
                wallList.extend(unvisited_Cells)
            
            del wallList[rand_index]

    #returns list of cells, check borders
    def getWalls(self, currCell):
        solution = []
        #corner cases
        if (currCell == (0,0)): #upper left
            return [(1,0), (0,1)]
        elif currCell == (0, self.height-1): #bottom left
            return [(0,self.height-2), (1, self.height-1)]
        elif currCell == (self.width-1, self.height-1): #bottom right
            return [(self.width-2,self.height-1), (self.width-1, self.height-2)]
        elif currCell == (self.width-1, 0): #upper right
            return [(self.width-2, 0), (self.width-1,1)]
        #edge cases
        elif (currCell[0] == 0): #left wall
            return [(0,currCell[1]-1), (1, currCell[1]), (0, currCell(1)+1)]
        elif (currCell[1] == self.height-1): #bottom wall
            return [(currCell[0]-1,currCell[1]),(currCell[0],currCell[1]-1),
             (currCell[0]+1,currCell[1])]
        elif (currCell[1] == self.width-1): #right wall
            return [(currCell[0]-1,currCell[1]),(currCell[0],currCell[1]-1),
             (currCell[0],currCell[1]-1)]
        elif (currCell[1] == 0): #top  wall
            return [(currCell[0]-1,0), (currCell[0],1), (currCell[0]+1,0)]
        else:
            return [(currCell[0]-1,currCell[1]),(currCell[0],currCell[1]+1),
             (currCell[0]+1,currCell[1]), (currCell[0],currCell[1]-1)] 
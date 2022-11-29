import random as rand

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        #u means unvisited, p means path, w means wall
        # self.visited=set()
        self.maze = [["u" for i in range(self.width)] for i in 
        range(self.height)] # start with all unvisited according to algo

    
    #I used Randomized Prim's Algorithm here (explanation of it from wikipedia,
    #but I wrote it myself based on my interpretation of it
    #https://en.wikipedia.org/wiki/Maze_generation_algorithm
    
    #helper-fn to return num of paths around given wall
    def numPathsAround(self, wall):
        numPaths = 0
        if (self.maze[wall[0]-1][wall[1]] == 'p'): #left
            numPaths += 1
        if (self.maze[wall[0]][wall[1]+1] == 'p'): #bottom
            numPaths += 1
        if (self.maze[wall[0]+1][wall[1]] == 'p'): #right
            numPaths +=1
        if (self.maze[wall[0]][wall[1]-1] == 'p'): #up
            numPaths += 1

        return numPaths

    #returns our generated maze
    def getMaze(self):
        startX = rand.randint(1,self.width-2) #randint is inclusive
        startY = rand.randint(1,self.height-2) #start not on edge

        self.maze[startX][startY] = 'p'
        self.walls.append([startX-1, startY]) #add the walls around it
        self.maze[startX-1][startY] = 'w' #mark it on maze
        self.walls.append([startX, startY+1])
        self.maze[startX][startY+1] = 'w'
        self.walls.append([startX+1, startY])
        self.maze[startX+1][startY] = 'w'
        self.walls.append([startX, startY-1])
        self.maze[startX][startY-1] = 'w'

        while(len(self.walls) > 0): #explore new walls for new potential paths
            pickedWall = self.walls[rand.randint(0,len(self.walls)-1)]
            #Left wall
            if(pickedWall[1] != 0 ): # guard against index error 
                if (self.maze[pickedWall[0]][pickedWall[1]-1] == 'u' and 
                self.maze[pickedWall[0]][pickedWall[1]+1] == 'p'):

                    paths = self.numPathsAround(pickedWall)
                    if paths <= 1: #according to algorithm
                        self.maze[pickedWall[0]][pickedWall[1]] = 'p' #make path
                        
                        #mark new walls around new marked path
                        #upper path
                        upath = self.maze[pickedWall[0]-1][pickedWall[1]]
                        if pickedWall[0] != 0: #guard against index out of range
                            if (upath !='p'): 
                                upath = 'w'
                            if ([pickedWall[0]-1, pickedWall[1]] not in
                             self.walls):
                                self.walls.append([pickedWall[0]-1,
                                 pickedWall[1]])

                        #bottom path
                        bpath = self.maze[pickedWall[0]+1][pickedWall[1]]
                        if (pickedWall[0] != self.height-1):
                            if (bpath != 'p'):
                                bpath = 'w'
                            if ([pickedWall[0]+1, pickedWall[1]] not in 
                            self.walls):
                                self.walls.append([pickedWall[0]+1, 
                                pickedWall[1]])

                        #leftest cell
                        lpath = self.maze[pickedWall[0]][pickedWall[1]-1]
                        if (pickedWall[1] != 0):	
                            if (lpath != 'p'):
                                lpath = 'w'
                            if ([pickedWall[0], pickedWall[1]-1] not in 
                            self.walls):
                                self.walls.append([pickedWall[0], 
                                pickedWall[1]-1])
                    
                    #remove path from the former list of walls
                    for wall in self.walls:
                        if (wall == pickedWall):
                            self.walls.remove(wall)
                    continue
            #bottom wall
            if(pickedWall[0] != self.height-1 ): # guard against index error 
                if (self.maze[pickedWall[0]+1][pickedWall[1]] == 'u' and 
                self.maze[pickedWall[0]-1][pickedWall[1]] == 'p'):

                    paths = self.numPathsAround(pickedWall)
                    if paths <= 1: #according to algorithm
                        self.maze[pickedWall[0]][pickedWall[1]] = 'p' #make path
                        
                        #mark new walls around new marked path
                        #bottom path
                        botpath = self.maze[pickedWall[0]+1][pickedWall[1]]
                        if pickedWall[0] != self.height-1: 
                            if (botpath !='p'): 
                                botpath = 'w'
                            if ([pickedWall[0]+1, pickedWall[1]] not in
                             self.walls):
                                self.walls.append([pickedWall[0]+1,
                                 pickedWall[1]])

                        #left path
                        leftpath = self.maze[pickedWall[0]][pickedWall[1]-1]
                        if (pickedWall[1] != 0):
                            if (leftpath != 'p'):
                                leftpath= 'w'
                            if ([pickedWall[0], pickedWall[1]-1] not in 
                            self.walls):
                                self.walls.append([pickedWall[0], 
                                pickedWall[1]-1])

                        #right path
                        rightpath = self.maze[pickedWall[0]][pickedWall[1]+1]
                        if (pickedWall[1] != self.width-1):	
                            if (rightpath != 'p'):
                                rightpath = 'w'
                            if ([pickedWall[0], pickedWall[1]+1] not in 
                            self.walls):
                                self.walls.append([pickedWall[0], 
                                pickedWall[1]+1])
                    
                    #remove path from the former list of walls
                    for wall in self.walls:
                        if (wall == pickedWall):
                            self.walls.remove(wall)
                    continue
            #right wall
            if(pickedWall[1] != self.width-1 ): # guard against index error 
                if (self.maze[pickedWall[0]][pickedWall[1]+1] == 'u' and 
                self.maze[pickedWall[0]][pickedWall[1]-1] == 'p'):

                    paths = self.numPathsAround(pickedWall)
                    if paths <= 1: #according to algorithm
                        self.maze[pickedWall[0]][pickedWall[1]] = 'p' #make path
                        
                        #mark new walls around new marked path
                        #right path
                        rP = self.maze[pickedWall[0]][pickedWall[1]+1]
                        if pickedWall[1] != self.width-1: 
                            if (rP !='p'): 
                                rP = 'w'
                            if ([pickedWall[0], pickedWall[1]+1] not in
                             self.walls):
                                self.walls.append([pickedWall[0],
                                 pickedWall[1]+1])

                        #bottom path
                        bP = self.maze[pickedWall[0]+1][pickedWall[1]]
                        if (pickedWall[1] != self.height-1):
                            if (bP != 'p'):
                                bP= 'w'
                            if ([pickedWall[0]+1, pickedWall[1]] not in 
                            self.walls):
                                self.walls.append([pickedWall[0]+1, 
                                pickedWall[1]])

                        #left path
                        lP = self.maze[pickedWall[0]-1][pickedWall[1]]
                        if (pickedWall[0] != 0):	
                            if (lP != 'p'):
                                lP = 'w'
                            if ([pickedWall[0]-1, pickedWall[1]] not in 
                            self.walls):
                                self.walls.append([pickedWall[0]-1, 
                                pickedWall[1]])
                    
                    #remove path from the former list of walls
                    for wall in self.walls:
                        if (wall == pickedWall):
                            self.walls.remove(wall)
                    continue
            #upper wall
            if(pickedWall[0] != 0 ): # guard against index error 
                if (self.maze[pickedWall[0]-1][pickedWall[1]] == 'u' and 
                self.maze[pickedWall[0]+1][pickedWall[1]] == 'p'):

                    paths = self.numPathsAround(pickedWall)
                    if paths <= 1: #according to algorithm
                        self.maze[pickedWall[0]][pickedWall[1]] = 'p' #make path
                        
                        #mark new walls around new marked path
                        #upper path
                        upPath = self.maze[pickedWall[0]-1][pickedWall[1]]
                        if pickedWall[0] != 0: 
                            if (upPath !='p'): 
                                upPath = 'w'
                            if ([pickedWall[0]-1, pickedWall[1]] not in
                             self.walls):
                                self.walls.append([pickedWall[0]-1,
                                 pickedWall[1]])

                        #leftest path
                        lfPath = self.maze[pickedWall[0]][pickedWall[1]-1]
                        if (pickedWall[1] != 0):
                            if (lfPath != 'p'):
                                lfPath= 'w'
                            if ([pickedWall[0], pickedWall[1]-1] not in 
                            self.walls):
                                self.walls.append([pickedWall[0], 
                                pickedWall[1]-1])

                        #righest path
                        rghP = self.maze[pickedWall[0]][pickedWall[1]+1]
                        if (pickedWall[1] != self.width-1):	
                            if (rghP != 'p'):
                                rghP = 'w'
                            if ([pickedWall[0], pickedWall[1]+1] not in 
                            self.walls):
                                self.walls.append([pickedWall[0], 
                                pickedWall[1]+1])
                    
                    #remove path from the former list of walls
                    for wall in self.walls:
                        if (wall == pickedWall):
                            self.walls.remove(wall)
                    continue

                #adapted from https://medium.com/swlh/fun-with-python-1-
                # maze-generator-931639b4fb7e to fit my code
                for i in range(0, self.height):
                    for j in range(0, self.width):
                        if (self.maze[i][j] == 'u'):
                            self.maze[i][j] = 'w'

                # Set entrance and exit
                for i in range(0, self.width):
                    if (self.maze[1][i] == 'p'):
                        self.maze[0][i] = 'p'
                        break

                for i in range(self.width-1, 0, -1):
                    if (self.maze[self.height-2][i] == 'p'):
                        self.maze[self.height-1][i] = 'p'
                        break
        print(self.maze)
        return self.maze

    # def maze(self):
    #     x = rand.randint(0,self.width-2)
    #     y = rand.randint(0,self.height-2)
    #     currCell = (x,y)    
    #     self.map[currCell[0]][currCell[1]] = "white"
    #     self.visited.add(currCell)
    #     walls = self.getWalls(currCell)

    #     while (len(walls) > 0):
    #         rand_index = rand.randint(0,len(walls)-2)
    #         currCell = walls[rand_index]
    #         sides = self.getWalls(currCell)
    #         visits = 0
    #         unvisited_Cells = []
    #         for cell in sides:
    #             if (cell in self.visited):
    #                 visits += 1
    #             elif (cell not in  walls):
    #                 unvisited_Cells.append(cell)
    #         if (visits <= 1):                
    #             print(currCell[0],currCell[1])
    #             print("map", len(self.map), len(self.map[0]))
    #             self.map[currCell[0]][currCell[1]] = "white" #make the passages
    #             self.visited.add(currCell)
    #             walls.extend(unvisited_Cells)
    #         print(len(walls))
    #         print("rand", rand_index)
    #         del walls[rand_index]
    #     return self.map

    # #returns list of cells, check borders
    # def getWalls(self, currCell):
    #     solution = []
    #     #corner cases
    #     if (currCell == (0,0)): #upper left
    #         return [(1,0), (0,1)]
    #     elif currCell == (0, self.height-1): #bottom left
    #         return [(0,self.height-2), (1, self.height-1)]
    #     elif currCell == (self.width-1, self.height-1): #bottom right
    #         return [(self.width-2,self.height-1), (self.width-1, self.height-2)]
    #     elif currCell == (self.width-1, 0): #upper right
    #         return [(self.width-2, 0), (self.width-1,1)]
    #     #edge cases
    #     elif (currCell[0] == 0): #left wall
    #         return [(0,currCell[1]-1), (1,currCell[1]), (0,currCell[1]+1)]
    #     elif (currCell[1] == self.height-1): #bottom wall
    #         return [(currCell[0]-1,currCell[1]),(currCell[0],currCell[1]-1),
    #          (currCell[0]+1,currCell[1])]
    #     elif (currCell[1] == self.width-1): #right wall
    #         return [(currCell[0]-1,currCell[1]),(currCell[0],currCell[1]-1),
    #          (currCell[0],currCell[1]-1)]
    #     elif (currCell[1] == 0): #top  wall
    #         return [(currCell[0]-1,0), (currCell[0],1), (currCell[0]+1,0)]
    #     else: #not edges, all four walls returned
    #         return [(currCell[0]-1,currCell[1]),(currCell[0],currCell[1]+1),
    #          (currCell[0]+1,currCell[1]), (currCell[0],currCell[1]-1)] 
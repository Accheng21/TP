import random as rand

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.entrance = [0,0]
        self.exit = [self.height-1,self.width-1]
        #u means unvisited, white means it's a path, black means wall
        #coloring reasons changed for 112 graphics

        self.maze = [["u" for i in range(self.width)] for j in 
        range(self.height)] # start with all unvisited according to algo
    
    #I used Randomized Prim's Algorithm here (explanation of it from wikipedia,
    #but I wrote it myself based on my interpretation of it
    #https://en.wikipedia.org/wiki/Maze_generation_algorithm
    
    #helper-fn to return num of paths around given wall
    def numPathsAround(self, wall):
        numPaths = 0
        if (self.maze[wall[0]-1][wall[1]] == 'white'): #left
            numPaths += 1
        if (self.maze[wall[0]][wall[1]+1] == 'white'): #bottom
            numPaths += 1
        if (self.maze[wall[0]+1][wall[1]] == 'white'): #right
            numPaths +=1
        if (self.maze[wall[0]][wall[1]-1] == 'white'): #up
            numPaths += 1

        return numPaths

    #returns our generated maze
    def getMaze(self):
        startX = rand.randint(1,self.width-2) #randint is inclusive
        startY = rand.randint(1,self.height-2) #start not on edge

        self.maze[startY][startX] = 'white'
        self.walls.append([startY - 1, startX])
        self.walls.append([startY, startX - 1])
        self.walls.append([startY, startX + 1])
        self.walls.append([startY + 1, startX])
        self.maze[startY-1][startX] = 'black'
        self.maze[startY][startX - 1] = 'black'
        self.maze[startY][startX + 1] = 'black'
        self.maze[startY + 1][startX] = 'black'

        while(self.walls): #explore new walls for new potential paths
            pickedWall = self.walls[rand.randint(0,len(self.walls)-1)]
            #Left Wall
            if(pickedWall[1] != 0 ): # guard against index error 
                if (self.maze[pickedWall[0]][pickedWall[1]-1] == 'u' and 
                self.maze[pickedWall[0]][pickedWall[1]+1] == 'white'):

                    paths = self.numPathsAround(pickedWall)

                    if paths <= 1: #according to algorithm
                        self.maze[pickedWall[0]][pickedWall[1]] = 'white' #make path
                        
                        #mark new walls around new marked path
                        #upper path
                        upath = self.maze[pickedWall[0]-1][pickedWall[1]]
                        if pickedWall[0] != 0: #guard against index out of range
                            if (upath !='white'): 
                                upath = 'black'
                            if ([pickedWall[0]-1, pickedWall[1]] not in
                             self.walls):
                                self.walls.append([pickedWall[0]-1,
                                 pickedWall[1]])

                        #bottom path
                        bpath = self.maze[pickedWall[0]+1][pickedWall[1]]
                        if (pickedWall[0] != self.height-1):
                            if (bpath != 'white'):
                                bpath = 'black'
                            if ([pickedWall[0]+1, pickedWall[1]] not in 
                            self.walls):
                                self.walls.append([pickedWall[0]+1, 
                                pickedWall[1]])

                        #leftest path
                        lpath = self.maze[pickedWall[0]][pickedWall[1]-1]
                        if (pickedWall[1] != 0):	
                            if (lpath != 'white'):
                                lpath = 'black'
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
                self.maze[pickedWall[0]-1][pickedWall[1]] == 'white'):

                    paths = self.numPathsAround(pickedWall)
                    if paths <= 1: #according to algorithm
                        self.maze[pickedWall[0]][pickedWall[1]] = 'white' #make path
                        
                        #mark new walls around new marked path
                        #bottom path
                        botpath = self.maze[pickedWall[0]+1][pickedWall[1]]
                        if (pickedWall[0] != self.height-1): 
                            if (botpath !='white'): 
                                botpath = 'black'
                            if ([pickedWall[0]+1, pickedWall[1]] not in
                             self.walls):
                                self.walls.append([pickedWall[0]+1,
                                 pickedWall[1]])

                        #left path
                        leftpath = self.maze[pickedWall[0]][pickedWall[1]-1]
                        if (pickedWall[1] != 0):
                            if (leftpath != 'white'):
                                leftpath= 'black'
                            if ([pickedWall[0], pickedWall[1]-1] not in 
                            self.walls):
                                self.walls.append([pickedWall[0], 
                                pickedWall[1]-1])

                        #right path
                        rightpath = self.maze[pickedWall[0]][pickedWall[1]+1]
                        if (pickedWall[1] != self.width-1):	
                            if (rightpath != 'white'):
                                rightpath = 'black'
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
                self.maze[pickedWall[0]][pickedWall[1]-1] == 'white'):

                    paths = self.numPathsAround(pickedWall)
                    if paths <= 1: #according to algorithm
                        self.maze[pickedWall[0]][pickedWall[1]] = 'white' #make path
                        
                        #mark new walls around new marked path
                        #right path
                        rP = self.maze[pickedWall[0]][pickedWall[1]+1]
                        if pickedWall[1] != self.width-1: 
                            if (rP !='white'): 
                                rP = 'black'
                            if ([pickedWall[0], pickedWall[1]+1] not in
                             self.walls):
                                self.walls.append([pickedWall[0],
                                 pickedWall[1]+1])

                        #bottom path
                        bP = self.maze[pickedWall[0]+1][pickedWall[1]]
                        if (pickedWall[1] != self.height-1):
                            if (bP != 'white'):
                                bP= 'black'
                            if ([pickedWall[0]+1, pickedWall[1]] not in 
                            self.walls):
                                self.walls.append([pickedWall[0]+1, 
                                pickedWall[1]])

                        #left path
                        lP = self.maze[pickedWall[0]-1][pickedWall[1]]
                        if (pickedWall[0] != 0):	
                            if (lP != 'white'):
                                lP = 'black'
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
                self.maze[pickedWall[0]+1][pickedWall[1]] == 'white'):

                    paths = self.numPathsAround(pickedWall)
                    if paths <= 1: #according to algorithm
                        self.maze[pickedWall[0]][pickedWall[1]] = 'white' #make path
                        
                        #mark new walls around new marked path
                        #upper path
                        upPath = self.maze[pickedWall[0]-1][pickedWall[1]]
                        if pickedWall[0] != 0: 
                            if (upPath !='white'): 
                                upPath = 'black'
                            if ([pickedWall[0]-1, pickedWall[1]] not in
                             self.walls):
                                self.walls.append([pickedWall[0]-1,
                                 pickedWall[1]])

                        #leftest path
                        lfPath = self.maze[pickedWall[0]][pickedWall[1]-1]
                        if (pickedWall[1] != 0):
                            if (lfPath != 'white'):
                                lfPath= 'black'
                            if ([pickedWall[0], pickedWall[1]-1] not in 
                            self.walls):
                                self.walls.append([pickedWall[0], 
                                pickedWall[1]-1])

                        #righest path
                        rghP = self.maze[pickedWall[0]][pickedWall[1]+1]
                        if (pickedWall[1] != self.width-1):	
                            if (rghP != 'white'):
                                rghP = 'black'
                            if ([pickedWall[0], pickedWall[1]+1] not in 
                            self.walls):
                                self.walls.append([pickedWall[0], 
                                pickedWall[1]+1])
                    
                    #remove path from the former list of walls
                    for wall in self.walls:
                        if (wall == pickedWall):
                            self.walls.remove(wall)
                    continue


            for wall in self.walls:
                if (wall == pickedWall):
                    self.walls.remove(wall)
            continue
            

        #adapted from https://medium.com/swlh/fun-with-python-1-
        # maze-generator-931639b4fb7e to fit my code
        for i in range(0, self.height):
            for j in range(0, self.width):
                if (self.maze[i][j] == 'u'):
                    self.maze[i][j] = 'black'

        # Set entrance and exit
        for i in range(0, self.width):
            if (self.maze[1][i] == 'white'):
                self.maze[0][i] = 'blue'
                self.entrance = [0,i]
                break

        for i in range(self.width-1, 0, -1):
            if (self.maze[self.height-2][i] == 'white'):
                self.maze[self.height-1][i] = 'green'
                self.exit = [self.height-1, i]
                break

        return self.maze

    #get entrance location
    def getEntranceLoc(self):
        return self.entrance[0], self.entrance[1]

    #get exit location
    def getExitLoc(self):
        return self.exit[0], self.exit[1]

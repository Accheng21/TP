from cmu_112_graphics import *
from Maze import *
import math

def appStarted(app):
    app.width = 500
    app.height = 500
    app.isGameOver = False

    app.gameWidth = 20
    app.gameHeight = 20
    app.cellSize = 40
    app.maze = Maze(app.gameWidth, app.gameHeight)
    app.theMaze = app.maze.getMaze() 

    app.userY, app.userX = app.maze.getEntranceLoc()
    app.userYSmooth, app.userXSmooth = app.userY, app.userX
    app.exitY, app.exitX = app.maze.getExitLoc()
    app.playerDir = ''
    app.botY, app.botX = app.exitY-1, app.exitX
    app.botYSmooth, app.botXSmooth = app.botY, app.botX
    app.botDir = ''
    app.timerDelay = 100

def keyPressed(app, event):
    if app.isGameOver == False:
        if event.key == 'Up':
            app.playerDir = 'Up'
        elif event.key == 'Down':
            app.playerDir = 'Down'
        elif event.key == 'Right':
            app.playerDir = 'Right'
        elif event.key == 'Left':
            app.playerDir = 'Left'

    #restart
    if event.key == 'r':
        appStarted(app)      

#converts app to grid 
def appToGrid(app, userYSmooth, userXSmooth):
    userYC, userXC = 0, 0
    
    return [userYC ,userXC]

def timerFired(app):
    checkGameOver(app)

    if app.isGameOver == False: 

        #if smooth animation eventually aligns with passage, move grid's xy pos
        # if(appToGrid(app, app.userYSmooth, app.userXSmooth)
        # != [app.userY, app.userX]):
            #moveplayer (changes gridxy)
        
        movePlayer(app, app.playerDir)
        moveBot(app, app.botDir)

        # else:
        #     moveSmoothPlayer(app,app.playerDir)
        #     movePlayer(app, app.playerDir)
# def timerFired(app):
#     checkGameOver(app)

        # moveSmoothPlayer(app, app.playerDir)

#     if app.isGameOver == False: 

#         #if smooth animation eventually aligns with passage, move grid's xy pos
#         if(appToGrid(app, app.userYSmooth, app.userXSmooth)
#         != [app.userY, app.userX]):
#             moveSmoothPlayer(app,app.playerDir)

#         else:
#             movePlayer(app, app.playerDir)
#             moveBot(app, app.botDir)


def moveSmoothPlayer(app, playerDir):
    if playerDir == 'Up':
        app.userYSmooth -= 0.1
    if playerDir == 'Down':
        app.userYSmooth += 0.1
    if playerDir == 'Right':
        app.userXSmooth += 0.1
    if playerDir == 'Left':
        app.userXSmooth -= 0.1

    if not legalMove(app):
        if playerDir == 'Up':
            app.userYSmooth += 0.1
        if playerDir == 'Down':
            app.userYSmooth -= 0.1 
        if playerDir == 'Right':
            app.userXSmooth -= 0.1
        if playerDir == 'Left':
            app.userXSmooth += 0.1

def movePlayer(app, playerDir):
    if playerDir == 'Up':
        app.userY -= 1
    if playerDir == 'Down':
        app.userY += 1
    if playerDir == 'Right':
        app.userX += 1
    if playerDir == 'Left':
        app.userX -= 1

    if not legalMove(app):
        if playerDir == 'Up':
            app.userY += 1
        if playerDir == 'Down':
            app.userY -= 1 
        if playerDir == 'Right':
            app.userX -= 1
        if playerDir == 'Left':
            app.userX += 1 

def moveBot(app, botDir):
    move = determineBotDir(app)
    yMoveDiff = move[0] - app.botY 

    xMoveDiff = move[1] - app.botX

    app.botX += xMoveDiff
    app.botY += yMoveDiff

def determineBotDir(app):
    legals = getLegalMoves(app) #find legal moves
    bestDist = 999
    bestMove = []

    #aLegalMove is an array, legals is 2d array
    for aLegalMove in legals: #find best move within legal moves
        a = distanceFormula(app, aLegalMove[0], aLegalMove[1], 
        app.userY, app.userX)
        if a < bestDist:
            bestDist = a
            bestMove = aLegalMove
    return bestMove


def distanceFormula(app, botY, botX, userY, userX):
    dist = math.sqrt((userY-botY)**2 + (userX-botX)**2)
    return dist
    
#get 2d array selection of legal moves to use in determine bot direction   
def getLegalMoves(app):
    legals = [] 
    #left
    if (app.botX-1 < app.gameWidth and app.botX-1 >= 0) and (
    app.theMaze[app.botY][app.botX-1] == 'white'):
        legals.append([app.botY, app.botX-1])
    #down
    if (app.botY+1 < app.gameHeight and app.botY+1 >= 0) and (
    app.theMaze[app.botY+1][app.botX] == 'white'):
        legals.append([app.botY+1, app.botX])
    #right
    if (app.botX+1 < app.gameWidth and app.botX+1 >= 0) and (
    app.theMaze[app.botY][app.botX+1] == 'white'):
        legals.append([app.botY, app.botX+1])
    #up
    if (app.botY-1 < app.gameHeight and app.botY-1 >= 0) and (
    app.theMaze[app.botY-1][app.botX] == 'white'):
        legals.append([app.botY-1, app.botX])

    return legals

def legalMove(app):
    if app.theMaze[app.userY][app.userX] == 'black':
        return False
    if (app.userX > app.gameWidth or app.userX < 0 or 
    app.userY > app.gameHeight
    or app.userY< 0):
        return False
    return True
    
def drawPlayerBot(app, canvas, r, c, color):
    x0 = c * (app.cellSize) 
    x1 = (c+1) * (app.cellSize)
    y0 = r * (app.cellSize)
    y1 = (r+1) * (app.cellSize)

    canvas.create_rectangle(x0,y0,x1,y1,
        fill = color, outline = 'black', width = 0.5)


def drawCell(app, canvas, r, c, color):
    x0 = c * app.cellSize 
    x1 = (c+1) * app.cellSize 
    y0 = r * app.cellSize 
    y1 = (r+1) * app.cellSize

    canvas.create_rectangle(x0,y0,x1,y1,
        fill = color, outline = 'black', width = 0.5)

def drawMaze(app, canvas):
    for r in range(app.gameHeight):
        for c in range(app.gameWidth):
            drawCell(app, canvas, r, c, app.theMaze[r][c])
    if app.isGameOver:
        drawGameOver(app, canvas)

def drawSmoothUser(app, canvas):
    drawPlayerBot(app, canvas, app.userY, app.userX, 'red')


def drawSmoothBot(app, canvas):
    drawPlayerBot(app, canvas, app.botY, app.botX, 'blue')

def checkGameOver(app):
    if (app.userX == app.exitX and app.userY == app.exitY):
        app.isGameOver = True
    if (app.userX == app.botX and app.userY == app.botY):
        app.isGameOver = True

def drawGameOver(app, canvas):
    canvas.create_rectangle(0,0,app.width, app.height, fill = 'black')
    canvas.create_text(app.width//2, app.height*0.5, text='GG!',
                       fill='white', font='Helvetica 26 bold')

def redrawAll(app, canvas):
    drawMaze(app, canvas)
    drawSmoothUser(app, canvas)
    drawSmoothBot(app, canvas)
    

runApp(width = 780, height = 804)
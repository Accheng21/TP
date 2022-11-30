from cmu_112_graphics import *
from Maze import *
import math

def appStarted(app):
    # app.margin = 10
    app.width = 500
    app.height = 500
    app.isGameOver = False

    app.gameWidth = 20
    app.gameHeight = 20
    app.cellSize = 40
    app.maze = Maze(app.gameWidth, app.gameHeight)
    app.theMaze = app.maze.getMaze() 
    app.userY, app.userX = app.maze.getEntranceLoc()
    app.exitY, app.exitX = app.maze.getExitLoc()
    app.playerDir = ''
    app.botY, app.botX = app.exitY, app.exitX
    app.botDir = ''
    app.timerDelay = 300
    
def keyPressed(app, event):
    if app.isGameOver == False:
        if event.key == 'Up':
            app.playerDir = 'Up'
            # movePlayer(app, -1, 0)
        elif event.key == 'Down':
            app.playerDir = 'Down'
            # movePlayer(app, +1, 0)
        elif event.key == 'Right':
            app.playerDir = 'Right'
            # movePlayer(app, 0, +1)
        elif event.key == 'Left':
            app.playerDir = 'Left'
            # movePlayer(app, 0, -1)  

    #restart
    if event.key == 'r':
        appStarted(app)      

def movePlayer(app, playerDir):
    if playerDir == 'Up':
        app.userY -= 1
    if playerDir == 'Down':
        app.userY +=1 
    if playerDir == 'Right':
        app.userX += 1
    if playerDir == 'Left':
        app.userX -=1 

    if not legalMove(app):
        if playerDir == 'Up':
            app.userY += 1
        if playerDir == 'Down':
            app.userY -=1 
        if playerDir == 'Right':
            app.userX -= 1
        if playerDir == 'Left':
            app.userX +=1 

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
    or app.userY < 0):
        return False
    return True


def timerFired(app):
    checkGameOver(app)
    movePlayer(app, app.playerDir)
    moveBot(app, app.botDir)
    

def drawCell(app, canvas, r, c, color):
    x0 = c * app.cellSize #+ app.margin
    x1 = (c+1) * app.cellSize #+ app.margin
    y0 = r * app.cellSize #+ app.margin
    y1 = (r+1) * app.cellSize #+ app.margin

    canvas.create_rectangle(x0,y0,x1,y1,
        fill = color, outline = 'black', width = 0.5)

def drawMaze(app, canvas):
    for r in range(app.gameHeight):
        for c in range(app.gameWidth):
            drawCell(app, canvas, r, c, app.theMaze[r][c])
    # drawTime(app, canvas)
    if app.isGameOver:
        drawGameOver(app, canvas)

def drawUser(app, canvas):
    drawCell(app, canvas, app.userY, app.userX, 'red')

def drawBot(app, canvas):
    drawCell(app, canvas, app.botY, app.botX, 'brown')

def checkGameOver(app):
    print(app.exitX, app.exitY)
    if (app.userX == app.exitX and app.userY == app.exitY):
        app.isGameOver = True

def drawGameOver(app, canvas):
    canvas.create_rectangle(0,0,app.width, app.height, fill = 'black')
    canvas.create_text(app.width//2, app.height*0.5, text='GAME OVER!',
                       fill='white', font='Helvetica 26 bold')


def redrawAll(app, canvas):
    drawMaze(app, canvas)
    drawUser(app, canvas)
    drawBot(app, canvas)
    

runApp(width = 780, height = 804)
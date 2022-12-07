from cmu_112_graphics import *
from Maze import *


def appStarted(app):
    app.width = 500
    app.height = 500
    app.isGameOver = False
    app.win = False
    app.gameWidth = 20
    app.gameHeight = 20
    app.cellSize = 40
    app.maze = Maze(app.gameWidth, app.gameHeight)
    app.theMaze = app.maze.getMaze() 
    app.userY, app.userX = app.maze.getEntranceLoc()
    app.exitY, app.exitX = app.maze.getExitLoc()
    app.botY, app.botX = app.exitY, app.exitX
    app.playerDir = ''

    app.firstMove = True
    app.timerDelay = 100
    #returns DFS solution for bot to follow 
    app.botMovesDFS = DFS(app, [(app.exitY, app.exitX)])

def keyPressed(app, event):
    if app.isGameOver == False:
        if event.key == 'Up':
            app.playerDir = 'Up'
            if not app.firstMove:
                moveBot(app)
        elif event.key == 'Down':
            app.playerDir = 'Down'
            if not app.firstMove:
                moveBot(app)
        elif event.key == 'Right':
            app.playerDir = 'Right'
            if not app.firstMove:
                moveBot(app)
        elif event.key == 'Left':
            app.playerDir = 'Left'
            if not app.firstMove:
                moveBot(app)
        if event.key == 'f':
            app.firstMove = False
    #restart
    if event.key == 'r':
        appStarted(app)      

def timerFired(app):
    checkWinning(app)
    checkGameOver(app)
    if app.isGameOver == False: 
        movePlayer(app, app.playerDir)

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

def legalMove(app):
    if (app.userX > app.gameWidth or app.userX < 0 or 
    app.userY > app.gameHeight or app.userY < 0):
        return False

    if (app.userY > len(app.theMaze)-1 or app.userX > len(app.theMaze[0])-1):
        return False

    if app.theMaze[app.userY][app.userX] == 'black':
        return False
    return True

def moveBot(app):
    if len(app.botMovesDFS) > 0:
        (app.botY, app.botX) = app.botMovesDFS.pop()
    else:
        app.isGameOver = True

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
    if app.win:
        drawWinning(app, canvas)

def drawUser(app, canvas):
    drawCell(app, canvas, app.userY, app.userX, 'lightblue')

def drawBot(app, canvas):
    drawCell(app, canvas, app.botY, app.botX, 'red')

def checkGameOver(app):
    if (app.userX == app.botX and app.userY == app.botY):
        app.isGameOver = True

def checkWinning(app):
    if (app.userX == app.exitX and app.userY == app.exitY):
        app.win = True


def drawGameOver(app, canvas):
    canvas.create_rectangle(0,0,app.width, app.height, fill = 'black')
    canvas.create_text(400, app.height*0.5, text='HUMANS ELIMINATED!',
                       fill='white', font='Zapfino 26 bold')

def drawWinning(app, canvas):
    canvas.create_rectangle(0,0,app.width, app.height, fill = 'black')
    canvas.create_text(400, app.height*0.5, text='HUMANS WIN!',
                       fill='white', font='Zapfino 26 bold')
def drawGameRules(app, canvas):
    canvas.create_rectangle(790,0,1200, 804, fill = 'black')
    canvas.create_text(1000, 70, text=(
        'H̸̡̧̲͙͙̭͎̺̘͖̾̔̑̈́ȕ̴̧̙̝̳̮̦̘͗̊̒͆́̈m̴̨̛̛̼̟̙̆̀̂̏͆̀͘͠à̴̌̎̿͜͝n̸̢̢̤̮̤̖̥̈͒́̎̿̃͘ ̷̟͔̰̱̀̎̇̀         '), fill='lightblue', font='NanumPenScript 30 ')


    canvas.create_text(1000, 100, text=(
        '      ̷̟͔̰̱̀̎̇̀V̵̛̖̗͎͍̠͙͖̈́͘͜ë̵̪̣̥́̎r̵̡̛̛̳̞̭̞̼̯̗̐̿̿͐̊̂͝s̶̡̡̛̥̭̹̻͔͈̒̿̌̀̍̂͜͝ű̶͙s̶͇̰̀͛͑̒̈́̑   '), fill='white', font='NanumPenScript 30 ')


    canvas.create_text(1000, 130, text=(
        '             ̷̤͝Ǎ̶̛̦̦̠̪̩̇͋̍̋͂Ĩ̵̧͍̠̗̙̖̜͉̊̑́͒̈́̿͝'), fill='red', font='NanumPenScript 30 ')

    canvas.create_text(1000, 265, text=(
        'YOUR MISSION :: '
    ), fill = 'white', font = 'NanumBrushScript 20 bold')

    canvas.create_text(1000, 300, text=(
        'Escape & reach the exit before the bot!'),
                       fill='lightblue', font='Zapfino 15 bold ')
    canvas.create_text(1000, 400, text=(
        'You are blue. The AI is red. Entrance & Exits are green.'
    ), fill = 'white', font = 'NanumBrushScript 15')

    canvas.create_text(1000, 500, text=(
        'Once you are ready, press \'f\' and RUNNNNNNN!!!'
    ), fill = 'white', font = 'NanumBrushScript 15')

    canvas.create_text(1000, 600, text=(
        'Use arrow keys to reach the exit!'
    ), fill = 'white', font = 'NanumBrushScript 25')

    canvas.create_text(1000, 700, text=(
        'Press \'r\' to generate a new maze and restart!'
    ), fill = 'white', font = 'NanumBrushScript 20')

def redrawAll(app, canvas):
    drawMaze(app, canvas)
    drawUser(app, canvas)
    drawBot(app, canvas)
    drawGameRules(app, canvas)
    

#for dfs algo
def isLegalMove(app, row, col):
    if (row < 0 or row >= app.gameHeight) or (col < 0 or col >= app.gameWidth):
        return False
    if app.theMaze[row][col] == 'black':
        return False
    return True

#DFS Solving for solution to end
def DFS(app, sol):
    (currRow, currCol) = sol[-1]
    if (currRow, currCol) == (app.maze.getEntranceLoc()):
        return sol    
    else:
        (currRow, currCol) = sol[-1]

        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for d in dir:
            (nrow, ncol) = (currRow + d[0], currCol + d[1])
            if isLegalMove(app,nrow,ncol) and ((nrow,ncol) not in sol):
                sol.append((nrow,ncol))
                result = DFS(app, sol)
                if result != None:
                    return sol
                sol.pop()
        return None
    
runApp(width = 1200, height = 804)
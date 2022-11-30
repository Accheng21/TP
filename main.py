from cmu_112_graphics import *
from Maze import *

def appStarted(app):
    app.margin = 10
    app.width = 500
    app.height = 500
    app.isGameOver = False

    app.gameWidth = 150
    app.gameHeight = 150
    app.cellSize = 5
    app.maze = Maze(app.gameWidth, app.gameHeight)
    app.theMaze = app.maze.getMaze() 

def keyPressed(app, event):
    pass

def timerFired(app):
    pass

def drawCell(app, canvas, r, c, color):
    x0 = app.margin + c * app.cellSize
    x1 = app.margin + (c+1) * app.cellSize
    y0 = app.margin + r * app.cellSize
    y1 = app.margin + (r+1) * app.cellSize

    canvas.create_rectangle(x0,y0,x1,y1,
        fill = color, outline = 'black', width = 0.5)

def drawMaze(app, canvas):
    for r in range(app.gameHeight):
        for c in range(app.gameWidth):
            drawCell(app, canvas, r, c, app.theMaze[r][c])
    # drawTime(app, canvas)
    if app.isGameOver:
        drawGameOver(app, canvas)

def drawGameOver(app, canvas):
    canvas.create_rectangle()


def redrawAll(app, canvas):
    # canvas.create_rectangle(0,0,app.width,app.height, fill = "white")
    drawMaze(app, canvas)


runApp(width = 780, height = 780)
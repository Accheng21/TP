from cmu_112_graphics import *
from Maze import * 

def appStarted(app):
    app.margin = 10
    app.rows = 40
    app.cols = 40
    app.cellSize = 10
    app.isGameOver = False

    app.cellWidth = 50
    app.cellHeight = 50
    app.cellSize = 5
    app.maze = Maze(app.cellWidth, app.cellHeight)

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
        fill = color, outline = 'black', width = 2)

def drawMaze(app, canvas):
    getMaze = app.maze.getMaze()
    for r in range(app.rows):
        for c in range(app.cols):
            drawCell(app, canvas, r, c, getMaze[r][c])
    # drawTime(app, canvas)
    if app.isGameOver:
        drawGameOver(app, canvas)

def drawGameOver(app, canvas):
    canvas.create_rectangle()


def redrawAll(app, canvas):
    drawMaze(app, canvas)


runApp(width = 500, height = 500)
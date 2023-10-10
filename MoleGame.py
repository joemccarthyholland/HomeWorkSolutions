
import random

# Define the variables
MoleX, MoleY, X, Y, Xhit, Yhit = 0, 0, 0, 0, 0, 0
GameGrid = [['_' for _ in range(10)] for _ in range(10)]
MoleHit = False

def main():
    InitialiseGrid()
    PlaceMole()
    DisplayGrid()
    playGame()
    input()

def PlaceMole():
    global MoleX, MoleY
    MoleX = random.randint(0, 9)
    MoleY = random.randint(0, 9)

def InitialiseGrid():
    global GameGrid
    for X in range(10):
        for Y in range(10):
            GameGrid[X][Y] = '_'

def playGame():
    global MoleHit
    while not MoleHit:
        InputHit()
        hitORMiss()
        DisplayGrid()

def hitORMiss():
    global MoleHit, GameGrid
    if Xhit == MoleX and Yhit == MoleY:
        MoleHit = True
        GameGrid[Xhit][Yhit] = 'M'
    else:
        MoleHit = False
        GameGrid[Xhit][Yhit] = 'X'

def InputHit():
    global Xhit, Yhit
    Xhit = int(input('input X : '))
    Yhit = int(input('input Y : '))

def DisplayGrid():
    global GameGrid
    print('  ', end='') # Pads out top row of numbers
    for X in range(10): # this loop adds the top row of numbers
        print(X, '|', end='')
    print() # starts a new line
    for Y in range(10):
        print(Y, '|', end='') # adds the left column of numbers 1 row at a time
        for X in range(10):
            print(GameGrid[X][Y], '|', end='') # fills in one line of the grid
        print() # starts a new line

# Call the main function
main()
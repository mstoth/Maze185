import random
import turtle

SIZE = 400
PATHWIDTH = 20
PW2 = PATHWIDTH/2

NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

class Maze():
    def __init__(self):
        self.s = turtle.Screen()
        self.s.screensize(SIZE,SIZE)
        self.t = turtle.Turtle()
        self.s.bgcolor('blue')
        self.s.register_shape("custom",((PW2, PW2),(PW2, -PW2),\
                                        (PW2,-PW2),(-PW2,-PW2),\
                                        (-PW2,-PW2),(-PW2,PW2),\
                                        (-PW2,PW2), (PW2,PW2)))
        self.t.shape("custom")
        self.t.color('white')
        self.t.penup()

    def reset(self):
        self.matrix = [[1 for i in range(int(SIZE/PATHWIDTH))] \
                          for i in range(int(SIZE/PATHWIDTH))]
        self.t.goto(-SIZE/2+PW2,SIZE/2-PW2)
        self.matrix[0][0]=0
        return True

    def setMatrixValueAt(self,pos,v):
        xv = pos[0]
        yv = pos[1]
        xi = int((xv+SIZE/2-PW2)/PATHWIDTH)
        yi = int(-(yv-(SIZE/2-PW2))/PATHWIDTH)
        self.matrix[xi][yi]=v
        
    
    def getMatrixValueAt(self,x,y):
        xi = int((x+SIZE/2-PW2)/PATHWIDTH)
        yi = int(-(y-(SIZE/2-PW2))/PATHWIDTH)
        return self.matrix[xi][yi]
    
    def direction(self,pos1,pos2):
        if pos1==pos2:
            return 0
        if pos1[0]==pos2[0]:
            # DO NORTH AND SOUTH
            if pos1[1]<pos2[1]:
                return NORTH
            else:
                return SOUTH
        else:
            # DO EAST AND WEST
            if pos1[0]<pos2[0]:
                return EAST
            else:
                return WEST

    def dig(self,d):
        if d==EAST:
            # if the space to the right is a 1, then we can dig
            if self.matrix[1][0]==1:
                # we can dig
                self.matrix[1][0]=0
                self.t.position=(-170,190)
        return self.t.pos()

    
    

from OpenGL.GL import *
from OpenGL.GLU import *
import math

class DrawC:
    def gambar(x,y,rgb):
        glPointSize(1.0)
        glColor3ub(*rgb)
        glBegin(GL_POINTS)
        glVertex2f(math.ceil(x),math.ceil(y))
        glEnd()

    def dda(Coor1,Coor2,rgb):
        x1 = Coor1[0]
        y1 = Coor1[1]
        x2 = Coor2[0]
        y2 = Coor2[1]
        dx = x2-x1
        dy = y2-y1
        if abs(dx) > abs(dy):
            if(x2 > x1):
                y = y1
                for x in range(int(x1), int(x2) + 1):
                    y = y + dy/abs(dx)
                    DrawC.gambar(x,y,rgb)
            else:
                y = y1
                for x in range(x2, x1 - 1):
                    y = y + dy/abs(dx)
                    DrawC.gambar(x,y,rgb)     
        else:
            if(y2 > y1):
                x = x1
                for y in range(y1, y2 + 1):
                    x = x + dx/abs(dy)
                    DrawC.gambar(x,y,rgb)
            else:
                x = x1
                for y in range(y2, y1 - 1):
                    x = x + dx/abs(dy)
                    DrawC.gambar(x,y,rgb)

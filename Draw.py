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

    def dda(Coor1, Coor2, rgb):
        x1, y1 = Coor1
        x2, y2 = Coor2
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))

        if dx == 0: 
            x_increment = 0
        else:
            x_increment = dx / steps

        if dy == 0: 
            y_increment = 0
        else:
            y_increment = dy / steps

        x = x1
        y = y1
        x_rounded = round(x)
        y_rounded = round(y)
        DrawC.gambar(x_rounded, y_rounded, rgb)

        for _ in range(int(steps)):
            x += x_increment
            y += y_increment
            x_rounded = round(x)
            y_rounded = round(y)

            DrawC.gambar(x_rounded, y_rounded, rgb)

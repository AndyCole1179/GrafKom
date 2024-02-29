from OpenGL.GL import *
from OpenGL.GLU import *
import math
import settingwindow

display = settingwindow.window

class DrawC:
    def gambar(XY,rgb):
        x,y = XY
        glPointSize(2.0)
        glColor3ub(*rgb)
        glBegin(GL_POINTS)
        glVertex2f(math.ceil(x),math.ceil(y))
        glEnd()

    def dda(Coor1, Coor2, rgb,default=False):
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
        DrawC.gambar((x_rounded, y_rounded), rgb)


        for _ in range(int(steps)):
            x += x_increment
            y += y_increment
            x_rounded = round(x)
            y_rounded = round(y)
            DrawC.gambar((x_rounded, y_rounded), rgb)


    def ddaw(Coor1, Coor2, rgb):
        x1,y1 = Coor1
        x2,y2 = Coor2
        if x2-x1 != 0 :
            slope =(y2-y1)/(x2-x1)
        else:
            slope = None
        
        if slope is not None and slope != 0:
        # Calculate intersection points with window borders
            potong_kiri = (0, int(y1 - (x1 * slope)))
            potong_kanan = (display[0], int(y1 + ((display[0] - x1) * slope)))
            potong_atas = (int(x1 - (y1 / slope)), 0)
            potong_bawah = (int(x1 + ((display[1] - y1) / slope)), display[1])
        
        # Cari garis potong di windows
        intersections = [point for point in [potong_kiri, potong_kanan, potong_atas, potong_bawah] if
                        0 <= point[0] <= display[0] and 0 <= point[1] <= display[1]]

        if intersections:
            potong = min(intersections, key=lambda p: (p[0] - x1) ** 2 + (p[1] - y1) ** 2)
        

    def ddadot(Coor1, Coor2, rgb):
        space = 5
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
        
        x,y = x1,y1
        draw_dot =True
        count = 0
        # DrawC.gambar(x_rounded, y_rounded, rgb)

        for i in range(int(steps)):
            if draw_dot:
                DrawC.gambar(((int(x)), int((y))),rgb)
            count += 1
            if count ==space:
                count = 0
                draw_dot = not draw_dot
            x += x_increment
            y += y_increment


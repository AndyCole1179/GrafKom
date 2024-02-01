import pygame 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math


display = (800, 600)
h_display = (int(display[0])/2,int(display[1])/2)
titik_tengah = (int(h_display[0]),int(h_display[1]))
def gambar(x,y,r,g,b):
    glPointSize(1.0)
    glColor3f(r,g,b)
    glBegin(GL_POINTS)
    glVertex2f(math.ceil(x),math.ceil(y))
    glEnd()


def dda(x1,y1,x2,y2,r,g,b):
    dx = x2-x1
    dy = y2-y1
    if abs(dx) > abs(dy):
        if(x2 > x1):
            y = y1
            for x in range(x1, x2 + 1):
                y = y + dy/abs(dx)
                gambar(x,y,r,g,b)
        else:
            y = y1
            for x in range(x2, x1 - 1):
                y = y + dy/abs(dx)
                gambar(x,y,r,g,b)     
    else:
        if(y2 > y1):
            x = x1
            for y in range(y1, y2 + 1):
                x = x + dx/abs(dy)
                gambar(x,y,r,g,b)
        else:
            x = x1
            for y in range(y2, y1 - 1):
                x = x + dx/abs(dy)
                gambar(x,y,r,g,b)
    

# def pembesaran_bayangan(xf,yf):
#     jarak_bayangan = 1/(1/f)
#     pass

def simulasi_cahaya(x,y):
    r1,g1,b1 = 0 , 0 , 0 
    r = 0*255
    g = 1*255
    b = 0*255
    color =(r,g,b)
    print(color)
    while True:
        data = glReadPixels(x,y,1,1,GL_RGB,GL_UNSIGNED_BYTE)
        current_color = np.frombuffer(data,dtype='uint8')
        current_color = tuple(current_color)
        print(current_color)
        gambar(x,y,r1,g1,b1)
        # current_color = tuple(current_color[0])
        if current_color == color:
            break
        x += 1

def object():
    x1 = int(h_display[0])/3
    y1 = int(h_display[1])
    x2 = int(h_display[0])/3
    y2 = int(h_display[1]-40)
    r, g, b = 0.5, 0.6 , 1
    dda(x1,y1,x2,y2,r,g,b)


def cermin(xc,yc,radiusx,radiusy):
    for i  in range (0, int(math.pi/0.0001)):
        theta = i *0.001
        x = xc + abs(radiusx*math.cos(theta-float(math.pi)))
        y = yc + (radiusy*math.sin(theta-float(math.pi)))
        r,g,b =  0, 1 ,0
        gambar(math.ceil(x),math.ceil(y),r,g,b)

def main():
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    glOrtho(0, 800, 600, 0, -1, 1)
    glClearColor(0.1, 0.4, 0.5, 1)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT)
        dda(0,int(h_display[1]),int(display[0]),int(h_display[1]), 1,0,0)
        object()
        cermin(400,300,50,300)
        simulasi_cahaya(int(h_display[0])/3,int(h_display[1]-40))
        pygame.display.flip()
        pygame.time.wait(10)

main()
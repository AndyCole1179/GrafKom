import pygame 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math


class main:

    def main():
        pygame.init()
        pygame.display.set_mode((800,600), DOUBLEBUF|OPENGL)

        glOrtho(0, 800, 600, 0, -1, 1)
        glClearColor(0.1, 0.4, 0.5, 1)
        dda_color=(255,0,255)
        warna_cermin = (255,0,0)
        koor_cermin = (300,300)
        Kaca = cermin()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            glClear(GL_COLOR_BUFFER_BIT)
            main.dda((0,300),(800,300),dda_color)
            main.dda((400,0),(400,600),dda_color)
            Kaca.gambar(100,(300,300),(255,0,0))
            benda.gambar((200,300,200,300-20))
            # simulasi_cahaya(int(h_display[0])/3,int(h_display[1]-40))
            
            pygame.display.flip()
            pygame.time.wait(10)      

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
                    main.gambar(x,y,rgb)
            else:
                y = y1
                for x in range(x2, x1 - 1):
                    y = y + dy/abs(dx)
                    main.gambar(x,y,rgb)     
        else:
            if(y2 > y1):
                x = x1
                for y in range(y1, y2 + 1):
                    x = x + dx/abs(dy)
                    main.gambar(x,y,rgb)
            else:
                x = x1
                for y in range(y2, y1 - 1):
                    x = x + dx/abs(dy)
                    main.gambar(x,y,rgb)
            pass


class cermin:
    def __init__(self) :
        self.radius = None
        self.TitikF = None
        self.coor = None
        
    def gambar (self,radius, CentCirl, warna):
        self.radius = radius
        
        for i in range (0, int(math.pi/0.01)):
            theta = 2.4+i *0.005
            x = CentCirl[0] + (radius*math.cos(theta-float(math.pi)))
            y = CentCirl[1] + (radius*math.sin(theta-float(math.pi)))
            main.gambar(math.ceil(x),math.ceil(y),warna)
        self.titikfocus()

    def titikfocus(self):
        print(self.radius)

        pass
class benda:
    def gambar (posisi):
        koor_bawah = (posisi[0],posisi[1])
        koor_atas = (posisi[2],posisi[3])
        rgb = (0, 255, 0)
        main.dda(koor_bawah,koor_atas,rgb)
        #pantulan_cermin(x2,y2,rgb)


class pantulan_cermin:
    def __init__(self) :
        self.jarak = None

    def simulasi_cahaya(self,x,y,warna,warnastop):
        self.jarak = 0
        while(0,0) <= (x,y) < (800,600) :
            data = glReadPixels(x,y,1,1,GL_RGB,GL_UNSIGNED_BYTE)
            current_color = np.frombuffer(data,dtype='uint8')
            current_color = tuple(current_color)
            main.gambar(x,y,warna)
            if current_color == warnastop:
                break
            x+=1
            self.jarak+=1

    def kalkulasi_banyangan(self,koor):
        jarak_benda = self.jarak

        
    def gambar_bayangan():
        pass



  
Main = main
Main.main()

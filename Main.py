import pygame 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Draw import DrawC
from Benda import benda
from Kaca import Cermin
from Bayangan import bayangan
from garis_cahaya import garis


class main():
    
    def main():
        dragging = False
        mouse_click = False

        pygame.init()
        pygame.display.set_mode((800,600), DOUBLEBUF|OPENGL)
        glOrtho(0,800,600,0,-1,1)
        background = (30,40,50)
        glClearColor(background[0]/255,background[1]/255,background[2]/255,1)

        cermin = Cermin()
        Benda = benda(cermin)
        bayang = bayangan(Benda)
        Garis = garis(bayang)
        garis_tengah = ((0,300),(800,300),(255,0,0))
        J,T,L = 150,50,50
        object = (J,T,L,T)
        object1 = None
        box_click = None
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN :
                    mouse_x , mouse_y = pygame.mouse.get_pos()
                    mouse_x = 400-mouse_x
                    mouse_y = 300-mouse_y

                    if mouse_x < 0:
                        PXKanan = object1[0]
                        PXKiri = PXKanan - object1[2]
                        if mouse_y < 0 :
                            print('x<0,y<0')
                            PYAtas = 0+object1[1]
                            PYBawah = 0
                        else :
                            PYBawah = object1[1]
                            PYAtas = 0
                            print('x<0 ,y>0')

                        if (PXKiri < mouse_x < PXKanan) and    (PYAtas < mouse_y < PYBawah):
                            box_click = True
                        else:
                            box_click = False

                    else:
                        PXKanan = object1[0]
                        PXKiri = PXKanan + object1[2]
                        PYBawah = 300
                        if mouse_y < 0 :
                            PYAtas = 0+object1[1]
                            PYBawah = 0

                        else :
                            PYBawah = object1[1]
                            PYAtas = 0
                        
                        if (PXKanan < mouse_x < PXKiri) and    (PYAtas < mouse_y < PYBawah):
                            box_click = True
                        else:
                            box_click = False
                    dragging = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    dragging = False

            glClear(GL_COLOR_BUFFER_BIT)
            DrawC.dda(*garis_tengah)
            cermin.gambargaris(200)
            if object1 is None:
                Benda.gambar(*object)
                object1 = object
            else :
                 Benda.gambar(*object1)
            bayang.kalkulasi_bayangan()
            Garis.gbcgaris()
            if dragging and box_click:
                mouse_x , mouse_y = pygame.mouse.get_pos()
                mouse_x = 400-mouse_x
                mouse_y = 300-mouse_y
                object1 = (mouse_x,mouse_y,object1[2],object1[3])
            pygame.display.flip()
            pygame.time.wait(10)
            
Main = main
Main.main()

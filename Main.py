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
        pygame.init()
        pygame.display.set_mode((800,600), DOUBLEBUF|OPENGL)
        glOrtho(0,800,600,0,-1,1)
        glClearColor(0,25,255,1)

        cermin = Cermin()
        Benda = benda(cermin)
        bayang = bayangan(Benda)
        Garis = garis(bayang)
        garis_tengah = ((0,300),(800,300),(255,0,0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            glClear(GL_COLOR_BUFFER_BIT)
            DrawC.dda(*garis_tengah)
            cermin.gambar(200,(400,300))
            #cermin.gambarfocus()
            Benda.gambar(350,100)
            bayang.kalkulasi_bayangan()
            Garis.gbc()

            

            pygame.display.flip()
            pygame.time.wait(10)

Main = main
Main.main()
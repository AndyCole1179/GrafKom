from Draw import DrawC
import math
class Cermin:
    def __init__(self):
        self.Radius= None
        self.Center= None
        self.perimeter = None
        self.Warna = (182, 102, 210)
        self.focus = None

    def gambar (self,radius,perimeter):
        self.Radius = radius
        self.perimeter = perimeter
        self.Center = (perimeter[0]-radius,perimeter[1])
        self.focus = (perimeter[0]-(radius/2),perimeter[1])
        for i in range (0, int(math.pi/0.01)):
            theta = 2.4+i *0.005
            x = self.Center[0] + (radius*math.cos(theta-float(math.pi)))
            y = self.Center[1] + (radius*math.sin(theta-float(math.pi)))
            DrawC.gambar(math.ceil(x),math.ceil(y),self.Warna)
            
    def gambargaris (self,radius):
        self.Radius = radius
        self.perimeter = (400,300)
        self.Center = (self.perimeter[0]-radius,self.perimeter[1])
        self.focus = (self.perimeter[0]-(radius/2),self.perimeter[1])
        DrawC.dda((400,0),(400,600),(255,0,0))


    def gambarfocus(self):
        DrawC.dda(self.focus,(self.focus[0],self.focus[1]-30),(255,0,0))

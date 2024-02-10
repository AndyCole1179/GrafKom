from Draw import DrawC
import math

class garis:
    def __init__(self,bayangan) :
        self.bayangan = bayangan
        self.cermin = bayangan.cermin
        self.benda = bayangan.benda
        self.KoorCerminAtas=None
        self.KoorCerminBawah = None
        self.warna = (255,255,0)

    def kalkulasi_garistemu(self,y,r):
        x = math.ceil(math.sqrt((r**2)-(y**2)))

        return x
    def gbc(self): #garis benda cermin
        y = self.benda.tinggi
        r = self.cermin.Radius
        x = self.kalkulasi_garistemu(y,r)
        print(x)
        self.KoorCerminAtas = (self.cermin.Center[0]+x,self.benda.kooratas[1])
        DrawC.dda(self.benda.kooratas,self.KoorCerminAtas,self.warna)
        self.gic()
    
    def gic(self):
        y = self.bayangan.tinggi
        r = self.cermin.Radius
        x = self.kalkulasi_garistemu(y,r)
        print(x)
        self.KoorCerminBawah = (self.cermin.Center[0]+x,self.bayangan.cooratas[1])
        DrawC.dda(self.bayangan.cooratas,self.KoorCerminBawah,self.warna)
        self.gif()

    def gif(self):
        DrawC.dda(self.KoorCerminAtas,self.bayangan.cooratas,self.warna)
        DrawC.dda(self.benda.kooratas,self.KoorCerminBawah,self.warna)
    

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
        x = (math.ceil(math.sqrt((r**2)-(y**2))))

        return x
    
    def gbc(self): #cermin = lingkaran
        y = self.benda.tinggi
        r = self.cermin.Radius
        x = self.kalkulasi_garistemu(y,r)
        self.KoorCerminAtas = (self.cermin.Center[0]+x,self.benda.kooratas[1])
        DrawC.dda(self.benda.kooratas,self.KoorCerminAtas,self.warna)
        self.gic()
    
    def gbcgaris(self):#cermin = garis
        y = self.benda.tinggi
        r = self.cermin.Radius
        self.KoorCerminAtas = (self.cermin.Center[0]+r,self.benda.kooratas[1])
        DrawC.dda(self.benda.kooratas,self.KoorCerminAtas,self.warna)
        self.gicgaris()

    def gic(self):# Cermin = lingkaran
        y = self.bayangan.tinggi
        r = self.cermin.Radius
        x = self.kalkulasi_garistemu(y,r)
        self.KoorCerminBawah = (self.cermin.Center[0]+x,self.bayangan.cooratas[1])
        self.gif()

    def gicgaris(self): # Cermin = garis
        y = self.bayangan.tinggi
        r = self.cermin.Radius
        self.KoorCerminBawah = (self.cermin.Center[0]+r,self.bayangan.cooratas[1])
        DrawC.dda(self.bayangan.cooratas,self.KoorCerminBawah,self.warna)
        self.gif()

    def gif(self):

        if self.benda.koor[0] > self.cermin.focus[0]  and self.benda.koor[0]< self.cermin.perimeter[0]:#Ruang 1
            DrawC.dda(self.KoorCerminAtas,self.bayangan.cooratas,self.warna)
            DrawC.dda(self.KoorCerminBawah,self.benda.kooratas,self.warna)

        elif self.benda.koor[0] > self.cermin.focus[0]  and self.benda.koor[0] > self.cermin.perimeter[0]:#Ruang 4
            DrawC.dda(self.KoorCerminAtas,self.bayangan.cooratas,self.warna)
            DrawC.dda(self.KoorCerminBawah,self.benda.kooratas,self.warna)

        else : # Ruang 2 dan 3
            DrawC.dda(self.KoorCerminAtas,self.bayangan.cooratas,self.warna)
            DrawC.dda(self.benda.kooratas,self.KoorCerminBawah,self.warna)
        # DsrawC.dda(self.bayangan.cooratas,self.KoorCerminAtas,self.warna)
        # print(self.bayangan.cooratas)
        # print(self.KoorCerminAtas)
        # DrawC.dda(self.KoorCerminBawah,self.benda.kooratas,self.warna)
        # print(self.KoorCerminBawah)
        # print(self.benda.kooratas)
    

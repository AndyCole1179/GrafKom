from Draw import DrawC
import math
class bayangan:
    def __init__(self,benda) :
        self.tinggi =None
        self.jarak = None
        self.benda = benda
        self.cermin = self.benda.cermin
        self.warna = (0,0,150)
        self.cooratas = None
        self.coorbawah = None
    
    def kalkulasi_bayangan(self):
        if self.benda.jarak == 0 or self.cermin.Radius == 0 or self.cermin.Radius/2 == self.benda.jarak :
            pass
        else:
            self.jarak = int(1/((1/(self.cermin.Radius/2))-(1/self.benda.jarak)))
            self.tinggi = int (self.jarak*self.benda.tinggi/self.benda.jarak)
            self.gambar_bayang()

    def gambar_bayang(self):
        self.coorbawah = (self.cermin.perimeter[0]-self.jarak,self.cermin.perimeter[1])
        self.cooratas =  (self.coorbawah[0],self.coorbawah[1]+self.tinggi)
        DrawC.dda(self.coorbawah,self.cooratas,self.warna)

    def kalkulasi_garistemu(y,r):
        x = math.ceil(math.sqrt((r**2)-(y**2)))
        return x

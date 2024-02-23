from Draw import DrawC
import math
class bayangan:
    def __init__(self,benda) :
        self.tinggi =None
        self.jarak = None
        self.benda = benda
        self.cermin = self.benda.cermin
        self.warna = (241,171,185)
        self.cooratas = None
        self.coorbawah = None
    
    def kalkulasi_bayangan(self):
        if self.benda.jarak == 0 or self.cermin.Radius == 0 or self.cermin.Radius/2 == self.benda.jarak :
            pass
        else:
            self.jarak = int(1/((1/(self.cermin.Radius/2))-(1/self.benda.jarak)))
            self.tinggi = int (self.jarak*self.benda.tinggi/self.benda.jarak)
            self.lebar = (int(self.benda.lebar*self.jarak/self.benda.jarak))
            self.gambar_bayang()
        
    def gambar_bayang(self):
        self.coorbawah = (self.cermin.perimeter[0]-self.jarak,self.cermin.perimeter[1])
        self.cooratas =  (self.coorbawah[0],self.coorbawah[1]+self.tinggi)
        if self.jarak > 0:
            kanan_atas = (self.cooratas[0]-int(self.lebar),self.cooratas[1])
            kanan_bawah = (self.coorbawah[0]-int(self.lebar),self.coorbawah[1])
        if self.cooratas[1] < 300:
            kanan_atas = (self.cooratas[0]+int(self.lebar),self.cooratas[1])
            kanan_bawah = (self.coorbawah[0]+int(self.lebar),self.coorbawah[1])
        if self.jarak <0:
            print("bebek")
            kanan_atas = (int(self.lebar)+self.cooratas[0],self.cooratas[1])
            kanan_bawah = (int(self.lebar)+self.coorbawah[0],self.coorbawah[1])
        
        DrawC.dda(self.coorbawah,self.cooratas,self.warna)
        DrawC.dda(self.cooratas,kanan_atas,self.warna)
        DrawC.dda(kanan_bawah,kanan_atas,self.warna)
        DrawC.dda(self.coorbawah,kanan_bawah,self.warna)

    def kalkulasi_garistemu(y,r):
        x = math.ceil(math.sqrt((r**2)-(y**2)))
        return x

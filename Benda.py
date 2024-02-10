from Draw import DrawC

class benda:
    def __init__(self,cermin):
        self.tinggi = None
        self.lebar = None
        self.cermin = cermin
        self.warna = (255,0,0)
        self.jarak = None
        self.kooratas = None

    def gambar(self,jarak,tinggi):
        self.tinggi = tinggi
        self.jarak = jarak
        koor_bawah = (self.cermin.perimeter[0]-jarak,self.cermin.perimeter[1])
        koor_atas =  (koor_bawah[0],koor_bawah[1]-tinggi)
        self.kooratas = koor_atas
        DrawC.dda(koor_bawah,koor_atas,self.warna)
    

from Draw import DrawC

class benda:
    def __init__(self,cermin):
        self.tinggi = None
        self.lebar = None
        self.cermin = cermin
        self.warna = (255,0,0)
        self.jarak = None
        self.kooratas = None
        self.koor = None

    def gambar(self,jarak,tinggi,lebar):
        self.lebar = lebar
        self.tinggi = tinggi
        self.jarak = jarak
        if jarak < 0 :
            koor_bawah = (self.cermin.perimeter[0]-jarak,self.cermin.perimeter[1])
            self.koor = koor_bawah
            koor_atas =  (koor_bawah[0],koor_bawah[1]-tinggi)
            self.kooratas = koor_atas
            TKiriAtas = (int(koor_atas[0]+(lebar/2)),koor_atas[1])
            TKiriBawah = (int(koor_bawah[0]+(lebar/2)),koor_bawah[1])

        else :
            koor_bawah = (self.cermin.perimeter[0]-jarak,self.cermin.perimeter[1])
            self.koor = koor_bawah
            koor_atas =  (koor_bawah[0],koor_bawah[1]-tinggi)
            self.kooratas = koor_atas
            TKiriAtas = (koor_atas[0]-(lebar/2),koor_atas[1])
            TKiriBawah = (koor_bawah[0]-(lebar/2),koor_bawah[1])


        DrawC.dda(TKiriAtas,koor_atas,self.warna)
        DrawC.dda(TKiriBawah,TKiriAtas,self.warna)
        DrawC.dda(koor_atas,koor_bawah,self.warna)
        DrawC.dda(TKiriBawah,koor_bawah,self.warna)
        
        #DrawC.dda(koor_bawah,koor_atas,self.warna)




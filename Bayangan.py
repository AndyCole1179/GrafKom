from Draw import DrawC
import math
import settingwindow

display = settingwindow.window
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
            perbesaran = self.jarak/self.benda.jarak
            self.tinggi = int (self.jarak*self.benda.tinggi/self.benda.jarak)
            self.lebar = (int(self.benda.lebar*self.jarak/self.benda.jarak))
            garis1,garis2 = (),()
            for i in range(len(self.benda.garis1)):
                garis1 += ((round((self.benda.garis1[i][0])*perbesaran)),round(self.benda.garis1[i][1]*perbesaran)),
                garis2 += ((round((self.benda.garis2[i][0])*perbesaran)),round(self.benda.garis2[i][1]*perbesaran)),
            self.gambar_bayang(garis1,garis2)
        
    def gambar_bayang(self,list1,list2):
        self.coorbawah = (self.cermin.perimeter[0]-self.jarak,self.cermin.perimeter[1])
        self.cooratas =  (self.coorbawah[0],self.coorbawah[1]+self.tinggi)

        if self.jarak> 0: #bayangan berada di kiri cermin
            if self.cooratas[1] > display[1]/2: #bayangan berada di bawah titik tengah
                kanan_atas = (self.cooratas[0]-int(self.lebar),self.cooratas[1])
                kanan_bawah = (self.coorbawah[0]-int(self.lebar),self.coorbawah[1])
            else :  #bayangan berada di atas titik tengah
                kanan_atas = (self.cooratas[0]+int(self.lebar),self.cooratas[1])
                kanan_bawah = (self.coorbawah[0]+int(self.lebar),self.coorbawah[1])

        else: #bayangan berada di kanan cermin
            if self.cooratas[1] > display[1]/2: #bayangan berada di bawah titik tengah
                kanan_atas = (self.cooratas[0]+int(self.lebar),self.cooratas[1])
                kanan_bawah = (self.coorbawah[0]+int(self.lebar),self.coorbawah[1])
            else :#bayangan berada di atas titik tengah
                kanan_atas = (self.cooratas[0]-int(self.lebar),self.cooratas[1])
                kanan_bawah = (self.coorbawah[0]-int(self.lebar),self.coorbawah[1])
        
        DrawC.dda(self.coorbawah,self.cooratas,self.warna)
        DrawC.dda(self.cooratas,kanan_atas,self.warna)
        DrawC.dda(kanan_bawah,kanan_atas,self.warna)
        DrawC.dda(self.coorbawah,kanan_bawah,self.warna)
        if  self.jarak > 0:
            if list1[0][1]>0:
                for item in range(len(list1)):
                    DrawC.dda((-list1[item][0]+400.0-self.jarak ,list1[item][1]+300.0),(-list2[item][0]+400.0-self.jarak,list2[item][1]+300.0),self.warna)
            else:
                for item in range(len(list1)):
                    DrawC.dda((list1[item][0]+400.0-self.jarak ,list1[item][1]+300.0),(list2[item][0]+400.0-self.jarak,list2[item][1]+300.0),self.warna)
        else :
            if list1[0][1]>0:
                for item in range(len(list1)):
                    DrawC.dda((list1[item][0]+400.0-self.jarak ,list1[item][1]+300.0),(list2[item][0]+400.0-self.jarak,list2[item][1]+300.0),self.warna)
            else:
                for item in range(len(list1)):
                    DrawC.dda((-list1[item][0]+400.0-self.jarak ,list1[item][1]+300.0),(-list2[item][0]+400.0-self.jarak,list2[item][1]+300.0),self.warna)


    def kalkulasi_garistemu(y,r):
        x = math.ceil(math.sqrt((r**2)-(y**2)))
        return x

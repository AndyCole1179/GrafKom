from Draw import DrawC
import math

class garis:
    def __init__(self,bayangan) :
        self.bayangan = bayangan
        self.cermin = bayangan.cermin
        self.benda = bayangan.benda
        self.KoorCerminAtas=None
        self.KoorCerminBawah = None
        self.warna = (255, 255, 153)

    def kalkulasi_garistemu(self,y,r):
        x = (math.ceil(math.sqrt((r**2)-(y**2))))

        return x
    
    
    def gbcgaris(self):#cermin = garis
        y = self.benda.tinggi
        r = self.cermin.Radius
        benda = self.benda.kooratas[1]
        if self.benda.kooratas[1] > 300:
            benda = benda+1
        else:
            benda = benda-1
        self.KoorCerminAtas = (self.cermin.Center[0]+r,benda)
        if self.benda.kooratas[0] >400:
            DrawC.dda((800,benda),self.KoorCerminAtas,self.warna)
        else:
            DrawC.dda((0,benda),self.KoorCerminAtas,self.warna)
        self.gicgaris()

    def gicgaris(self): # Cermin = garis
        y = self.bayangan.tinggi
        r = self.cermin.Radius
        self.KoorCerminBawah = (self.cermin.Center[0]+r,self.bayangan.cooratas[1])
        if self.bayangan.cooratas[0] > 400:
            DrawC.ddadot((800,self.bayangan.cooratas[1]),self.KoorCerminBawah,self.warna)
        else :
            DrawC.ddadot((0,self.bayangan.cooratas[1]),self.KoorCerminBawah,self.warna)
        #DrawC.dda(self.bayangan.cooratas,self.KoorCerminBawah,self.warna)
        self.gif()

    def kalkulasi(self,coor1,coor2):
        x1,y1 = coor1
        x2,y2 = coor2
        if x1 == x2:
            return (x1, 0), (x1, 600)
    
        if y1 == y2:
            return (0, y1), (800, y2)
        
        slope =(y2-y1)/(x2-x1)
        
        if slope is not None and slope != 0:
            potong_kiri = (0, int(y1 - (x1 * slope)))
            potong_kanan = (800, int(y1 + ((800 - x1) * slope)))
            potong_atas = (int(x1 - (y1 / slope)), 0)
            potong_bawah = (int(x1 + ((600 - y1) / slope)), 600)

        # Find valid intersections within window bounds
            garis_potong = [point for point in [potong_kiri, potong_kanan, potong_atas, potong_bawah] if
                        0 <= point[0] <= 800 and 0 <= point[1] <= 600]
            return(garis_potong)

    def gif(self):
        
        #ruang 1
        if self.benda.koor[0] > self.cermin.focus[0]  and self.benda.koor[0]< self.cermin.perimeter[0]:
            DrawC.ddadot(self.KoorCerminAtas,self.bayangan.cooratas,self.warna)
            DrawC.dda(self.KoorCerminBawah,self.benda.kooratas,self.warna)
            DrawC.dda(self.KoorCerminBawah,(0,self.KoorCerminBawah[1]),self.warna)
            bebek = self.kalkulasi(self.KoorCerminAtas,self.bayangan.cooratas)
            if self.bayangan.cooratas[1] <300:
                if bebek[0][0] == 0:
                    DrawC.ddadot(bebek[1],self.bayangan.cooratas,self.warna)
                else:
                    DrawC.ddadot(bebek[0],self.bayangan.cooratas,self.warna)
            else :
                DrawC.ddadot(bebek[1],self.KoorCerminAtas,self.warna)


        #ruang 4
        elif self.benda.koor[0] > self.cermin.focus[0]  and self.benda.koor[0] > self.cermin.perimeter[0]:
            DrawC.dda(self.KoorCerminBawah,(self.benda.kooratas[0]-1,self.KoorCerminBawah[1]),self.warna)
            ayam = self.kalkulasi(self.benda.kooratas,self.KoorCerminBawah)
            if self.benda.kooratas[1] >300:
                DrawC.dda(ayam[1],self.KoorCerminBawah,self.warna)
            else :
                if ayam[0][0] == 0:
                    DrawC.dda(ayam[1],self.KoorCerminBawah,self.warna)
                else:
                    DrawC.dda(ayam[0],self.KoorCerminBawah,self.warna)
            bebek = self.kalkulasi(self.bayangan.cooratas,self.KoorCerminAtas)
            if self.bayangan.cooratas[1] > 300:
                DrawC.ddadot(bebek[0],self.KoorCerminAtas,self.warna)
            else :
                if bebek[0][0] == 0:
                    DrawC.ddadot(bebek[0],self.KoorCerminAtas,self.warna)
                else:
                    DrawC.ddadot(bebek[1],self.KoorCerminAtas,self.warna)
            
        # Ruang 2 dan 3
        else :
            ayam = self.kalkulasi(self.KoorCerminBawah,self.benda.kooratas)
            if self.benda.kooratas[1] < 300:
                DrawC.dda(ayam[0],self.KoorCerminBawah,self.warna)

            else :
                if ayam[0][0] == 0:
                    DrawC.dda(ayam[0],self.KoorCerminBawah,self.warna)
                else:
                    DrawC.dda(ayam[1],self.KoorCerminBawah,self.warna)
            bebek = self.kalkulasi(self.KoorCerminAtas,self.bayangan.cooratas)
            if self.bayangan.cooratas[1] >300:
                if bebek[0][0] == 0:
                    DrawC.ddadot(bebek[0],self.KoorCerminAtas,self.warna)
                else:
                    DrawC.ddadot(bebek[1],self.KoorCerminAtas,self.warna)
            else :
                DrawC.ddadot(bebek[0],self.KoorCerminAtas,self.warna)
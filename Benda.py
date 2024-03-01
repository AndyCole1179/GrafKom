from Draw import DrawC

class benda:
    def __init__(self,cermin):
        self.tinggi = None
        self.lebar = None
        self.cermin = cermin
        self.warna = (255, 51, 153)
        self.jarak = None
        self.kooratas = None
        self.koor = None
        self.garis1 = None
        self.garis2 = None

    def gambar(self,jarak,tinggi,lebar,T):
        self.lebar = lebar*tinggi/T
        self.tinggi = tinggi
        self.jarak = jarak

        if jarak < 0 :
            koor_bawah = (self.cermin.perimeter[0]-jarak,self.cermin.perimeter[1])
            self.koor = koor_bawah
            koor_atas =  (koor_bawah[0],koor_bawah[1]-tinggi)
            self.kooratas = koor_atas
            if tinggi > 0 :
                TKiriAtas = (koor_atas[0]+(self.lebar),koor_atas[1])
                TKiriBawah = (koor_bawah[0]+(self.lebar),koor_bawah[1])
            else:
                TKiriAtas = (koor_atas[0]-(self.lebar),koor_atas[1])
                TKiriBawah = (koor_bawah[0]-(self.lebar),koor_bawah[1])

        else :
            koor_bawah = (self.cermin.perimeter[0]-jarak,self.cermin.perimeter[1])
            self.koor = koor_bawah
            koor_atas =  (koor_bawah[0],koor_bawah[1]-tinggi)
            self.kooratas = koor_atas
            if tinggi > 0 :
                TKiriAtas = (koor_atas[0]-(self.lebar),koor_atas[1])
                TKiriBawah = (koor_bawah[0]-(self.lebar),koor_bawah[1])
            else:
                TKiriAtas = (koor_atas[0]+(self.lebar),koor_atas[1])
                TKiriBawah = (koor_bawah[0]+(self.lebar),koor_bawah[1])

        DrawC.dda(TKiriAtas,koor_atas,self.warna)
        DrawC.dda(TKiriBawah,TKiriAtas,self.warna)
        DrawC.dda(koor_atas,koor_bawah,self.warna)
        DrawC.dda(TKiriBawah,koor_bawah,self.warna)
        
        #DrawC.dda(koor_bawah,koor_atas,self.warna)
    def gambartest(self,jarak,tinggi,lebar,T,list1,list2):
        self.lebar = lebar*tinggi/T
        self.tinggi = tinggi
        self.jarak = jarak
        if  jarak > 0:
            if list1[0][1]>0:
                for item in range(len(list1)):
                    DrawC.dda((-list1[item][0]+400.0-jarak ,-list1[item][1]+300.0),(-list2[item][0]+400.0-jarak,-list2[item][1]+300.0),self.warna)
            else:
                for item in range(len(list1)):
                    DrawC.dda((list1[item][0]+400.0-jarak ,-list1[item][1]+300.0),(list2[item][0]+400.0-jarak,-list2[item][1]+300.0),self.warna)
        else :
            if list1[0][1]>0:
                for item in range(len(list1)):
                    DrawC.dda((list1[item][0]+400.0-jarak ,-list1[item][1]+300.0),(list2[item][0]+400.0-jarak,-list2[item][1]+300.0),self.warna)
            else:
                for item in range(len(list1)):
                    DrawC.dda((-list1[item][0]+400.0-jarak ,-list1[item][1]+300.0),(-list2[item][0]+400.0-jarak,-list2[item][1]+300.0),self.warna)
        
    
    def kalkulasi(self,J,T,L,TT):
        perbesaranT = T/TT
        temp1, temp2 = self.garis_benda()
        pivotx,pivoty  = temp1[0][0],temp1[0][1]
        self.garis1 = ()
        self.garis2 = ()
        for i in range(len(temp1)):
            self.garis1 += ((round((temp1[i][0]-pivotx)*perbesaranT)),round(temp1[i][1]*perbesaranT)),
            self.garis2 += ((round((temp2[i][0]-pivotx)*perbesaranT)),round(temp2[i][1]*perbesaranT)),
        self.gambartest(J,T,L,TT,self.garis1,self.garis2)

    def garis_benda(self):
        garis_benda1 = (
            (71.66666667 ,49.66666667),
            (89.33333333,24),
            (90.66666667,11.33333333),
            (88.33333333,8.666666667),
            (88.33333333, 4.333333333),
            (97.66666667, 0),
            (89.33333333, 24),
            (103.6666667, 12.33333333),
            (115,7.333333333),
            (136, 4.333333333),
            (371, 5),
            (383.6666667, 48.33333333),
            (314.3333333, 43.33333333),
            (190, 43.33333333),
            (175.6666667, 47.33333333),
            (175.6666667, 47.33333333),
            (170.6666667, 46.66666667),
            (166.07, 49.70333333),
            (175.6666667, 47.33333333),
            (200, 67.66666667),
            (216.7833333, 43.33333333),
            (217.6666667, 67.66666667),
            (295.3333333, 59.66666667),
            (220, 59.66666667),
            (325.3333333, 48.33333333),
            (325.3333333, 59.66666667),
            (295.3333333, 59.66666667),
            (217.6666667, 67.66666667),
            (217.6666667, 67.66666667),
            (217.6666667, 67.66666667),
            (216.6366667, 78.08666667),
            (210.28, 78.14666667),
            (201.7866667, 78.23),
            (191.3333333, 78.33333333),
            (225.3333333, 78),
            (225.3333333, 78),
            (228.3433333, 85.72333333),
            (247.6666667, 84),
            (257, 77.66666667),
            (263.3333333, 87),
            (273.6666667, 87),
            (273.6666667, 76.33333333),
            (295.6666667, 76.33333333)
        )
        garis_benda2= (
            (89.33333333,24),
            (90.66666667, 11.33333333),
            (88.33333333, 8.666666667),
            (88.33333333, 4.333333333),
            (97.66666667, 0),
            (198, 4.333333333),
            (103.6666667, 12.33333333),
            (115, 7.333333333),
            (136, 4.333333333),
            (371,5),
            (383.6666667, 48.33333333),
            (325.3333333, 48.33333333),
            (325.3333333, 48.33333333),
            (314.3333333, 43.33333333),
            (190, 43.33333333),
            (170.6666667, 46.66666667),
            (73.73, 46.66666667),
            (71.66666667, 49.66666667),
            (166.07, 49.70333333),
            (175.6666667, 47.33333333),
            (220, 59.66666667),
            (220, 59.66666667),
            (220, 59.66666667),
            (190.3433333, 59.59666667),
            (325.3333333, 59.66666667),
            (295.3333333, 59.66666667),
            (295.6666667, 76.33333333),
            (220, 59.66666667),
            (200, 67.66666667),
            (225.3833333, 78),
            (212.9466667, 67.66666667),
            (210.0733333, 67.66666667),
            (205.69, 67.66666667),
            (200, 67.66666667),
            (191.3333333, 78.33333333),
            (257, 77.66666667),
            (191.3333333, 78.33333333),
            (228.3333333, 85.66666667),
            (247.6666667, 84),
            (257, 77.66666667),
            (263.3333333, 87),
            (273.6666667, 87),
            (273.6666667, 76.33333333)
        )
        return garis_benda1,garis_benda2
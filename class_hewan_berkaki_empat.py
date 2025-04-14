class hewan_berkaki_empat():
        def __init__(self, nama, jenis):
                self.nama = nama
                self.jenis = jenis

        def berlari(self):
                print(self.nama, "berlari")

        def berdiri(self):
                print(self.nama, "berdiri")

class kucing(hewan_berkaki_empat):
        def __init__(self, nama, jenis, umur):
                super().__init__(nama, jenis)
                self.umur = umur

        def umur_kucing(self):
                print(self.nama, "berumur", self.umur)

class anjing(hewan_berkaki_empat):
        def __init__(self, nama, jenis, umur):
                super().__init__(nama, jenis)
                self.umur = umur
        
        def ndeuraso(self):
                print(self.nama, "ndeuraso")

        def umur_anjing(self):
                print(self.nama, "berumur", self.umur)

samiu = kucing("samiu", "ince", 4)
samiu.berdiri()
samiu.berlari()
samiu.umur_kucing()

mahmud = anjing("mahmud", "leo", 4)
mahmud.berdiri()
mahmud.berlari()
mahmud.ndeuraso()
mahmud.umur_anjing()

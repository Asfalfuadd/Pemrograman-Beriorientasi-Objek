class cat :
        def __init__(self,nama,umur):
                self.nama = nama
                self.umur = umur 
        
        def duduk(self):
                print(f"{self.nama} duduk")

        def berdiri(self):
                print(f"{self.nama} berdiri")

        def berlari(self):
                print(f"{self.nama} berlari")

        def bab(self):
                print(f"{self.nama} buang air besar")

        def bak(self):
                print(f"{self.nama} buang air kecil")

kucingku = cat("Diego",4)

print(f"kucingku bernama {kucingku.nama}")
print(f"kucingku berumur {kucingku.umur} tahun")

kucingku.duduk()
kucingku.berdiri()
kucingku.berlari()
kucingku.bab()
kucingku.bak()

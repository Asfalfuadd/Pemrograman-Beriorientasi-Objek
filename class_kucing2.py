class cat :
        def __init__ (self, ras , umur):
                self.ras = ras
                self.umur = umur

        def melompat(self):
                print(f"{self.ras} melompat")

        def tidur(self):
                print(f"{self.ras} tidur")

kucing_saya = cat ("Persia",3)
kucing_dia = cat ("jawa",4)

print(f"Kucing saya {kucing_saya.ras}")
print(f"Kucing dia {kucing_dia.ras}")

kucing_saya.melompat()
kucing_dia.tidur()

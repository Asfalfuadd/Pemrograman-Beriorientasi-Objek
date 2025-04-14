class mahasiswa():
        def __init__(self, nama, nim, nilai):
                self.nama = nama
                self._nim = nim
                self._nilai = nilai

        def set_nilai(self, nilai):
                self._nilai = nilai

        def get_nilai(self):
                return self._nilai
        
        def set_nim(self, nim):
                self._nim = nim

        def get_nim(self):
                return self._nim
        
        def set_nama(self,nama):
                self.nama = nama

        def get_nama(self):
                return self.nama


pall = mahasiswa("Pall", "76543210", 70)

pall.set_nama("Pall")
print(pall.get_nama())
pall.set_nim(76543210)
print(pall.get_nim())

print(pall.get_nilai())
pall.set_nilai(98)
print(pall.get_nilai())

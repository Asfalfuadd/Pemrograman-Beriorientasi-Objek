class MAHASISWA :
        def __init__(self, nama, nim, tempat_tgl_lahir, alamat, no_hp):
                self.nama = nama
                self.nim = nim
                self.ttl = tempat_tgl_lahir
                self.alamat = alamat
                self.no_hp = no_hp

        def tampilkan_data(self):
                print("Nama                     : ", (self.nama))
                print("NIM                      : ", (self.nim))
                print("Tempat Tanggal Lahir     : ", (self.ttl))
                print("Alamat                   : ", (self.alamat))
                print("No Handphone             : ", (self.no_hp))
                print("--------------------------------")

list_mahasiswa = []
jumlah = int(input("Masukkan jumlah mahasiswa : "))

for i in range(jumlah):
        print("\nMasukkan data mahasiswa ke -", (i+1))
        nama = input("Masukkan nama mahasiswa : ")
        nim = input("Masukkan NIM mahasiswa : ")
        ttl = input("Masukkan tempat/tanggal lahir mahasiswa : ")
        alamat = input("Masukkan alamat mahasiswa : ")
        no_hp = input("Masukkan no telepon mahasiswa : ")
        print()

        mahasiswa = MAHASISWA(nama, nim, ttl, alamat, no_hp)
        list_mahasiswa.append(mahasiswa)

for mahasiswa in list_mahasiswa:
        mahasiswa.tampilkan_data()
        print()



data_mahasiswa = []
jumlah_mahasiswa = int(input("Masukkan Jumlah Mahasiswa : "))


for i in range (jumlah_mahasiswa):
        nama = (input("Masukkkan Nama : "))
        nim = (input("Masukkan Nim : "))
        alamat = (input("Masukkan alamat : "))
        print()

        data_mahasiswa.append((nama, nim, alamat))

for mahasiswa in data_mahasiswa:
        print("Nama",mahasiswa[0])
        print("Nim",mahasiswa[1])
        print("Alamat",mahasiswa[2])


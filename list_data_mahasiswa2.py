data_mahasiswa = []
nilai_matematika = []
nilai_bind = []
nilai_barab = []

jumlah = int(input("Masukkan Jumlah Mahasiswa : "))

for i in range (jumlah):
        nama = input("Masukkan Nama Mahasiswa : ")
        nim = input("Masukkan NIM Mahasiswa : ")
        mtk = int(input("Masukkan Nilai Matematika : "))
        bind = int(input("Masukkan NIlai Bahasa Indonesia : "))
        barab = int(input("Masukkan Nilai Bahasa Arab : "))

        data_mahasiswa.append((nama,nim))
        nilai_matematika.append(mtk)
        nilai_bind.append(bind)
        nilai_barab.append(barab)

rata_rata_mtk = sum(nilai_matematika) / jumlah
rata_rata_bind = sum(nilai_bind) / jumlah
rata_rata_barab = sum(nilai_barab) / jumlah
        
print("\nData Mahasiswa")
for i in data_mahasiswa:
        print("Nama",i[0])
        print("Nim",i[1])
        print("Nilai Matematika",nilai_matematika)
        print("Nilai Bahasa Indonesia",nilai_bind)
        print("Nilai Bahasa Arab",nilai_barab)

print("\nNilai Rata-Rata Setiap Matkul")
print("Rata rata Nilai Matematika : ",rata_rata_mtk)
print("Rata rata Nilai Bahasa Indonesia : ",rata_rata_bind)
print("Rata rata Nilai Bahasa Arab : ",rata_rata_barab)





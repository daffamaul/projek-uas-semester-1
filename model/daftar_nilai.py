import os
class Data_mahasiswa:
    nama = []
    nim = []
    uts = []
    uas = []
    tugas = []
    akhir = []

    # Tambah data
    def tambah(self):
        os.system("cls")
        print("Tambah data\n")
        nama    = input("Nama           : ")
        self.nama.append(nama)
        nim     = int(input("NIM            : "))
        self.nim.append(nim)
        # tugas   = int(input("Nilai Tugas    : "))
        # self.tugas.append(tugas)
        # uts     = int(input("NIlai UTS      : "))
        # self.uts.append(uts)
        # uas     = int(input("Nilai UAS      : "))
        # self.uas.append(uas)
        # akhir   = (tugas * .3) + (uts * .35) + (uas * .35)
        # self.akhir.append(akhir)
        uts     = 0
        self.uts.append(uts)
        uas     = 0
        self.uas.append(uas)
        tugas   = 0
        self.tugas.append(tugas)
        akhir = (tugas * .3) + (uts * .35) + (uas * .35)
        self.akhir.append(akhir)

        print("\nData {0} berhasil di tambahkan".format(nama))
                
    # Menghapus inputan nama
    def hapus(self, nama):
        os.system("cls")
        print("Hapus data inputan")
        nama = (input("\nMasukan Namal : "))
        if nama in self.nama:
            print("Data {0} berhasil di hapus".format(nama))
            index = self.nama.index(nama)
            del self.nama[index]
            del self.nim[index]
            del self.uts[index]
            del self.uas[index]
            del self.tugas[index]
            del self.akhir[index]
        else:
            os.system("cls")
            print("NAMA {0} TIDAK ADA!".format(nama))
    
        # Mengubah data nama inputan
    def ubah(self, nama):
        os.system("cls")
        input_nama = input("Nama yang ingin di ubah : ")
        if input_nama in nama:
            print(f"Nama {input_nama} tersedia, silahkan ubah.")
            index = nama.index(input_nama)
            self.nim[index]     = int(input("NIM            : "))
            self.tugas[index]   = int(input("Nilai TUgas    : "))
            self.uts[index]     = int(input("Nilai UTS      : "))
            self.uas[index]     = int(input("Nilai UAS      : "))
            self.akhir[index] = (self.tugas[index] * .3) + (self.uts[index] * .35) + (self.uas[index] * .35)

            print("\nData {0} berhasil di ubah".format(input_nama))
        else:
            os.system("cls")
            print("NAMA {0} TIDAK ADA!".format(nama))
    
    def cari(self):
        os.system("cls")
        print("Mencari data")
        print("="*15)
        nama = (input("\nMasukan Nama yg ingin di cari : "))
        if nama in self.nama:
            print("Nama tersedia, berikut datanya")
            index = self.nama.index(nama)
            print(f"Nama Mahasiswa: {self.nama[index]}")
            print(f"NIM Mahasiswa : {self.nim[index]}")
            print(f"Nilai UTS     : {self.uts[index]}")
            print(f"Nilai UAS     : {self.uas[index]}")
            print(f"Nilai TUGAS   : {self.tugas[index]}")
        else:
            os.system("cls")
            print("NAMA {0} TIDAK ADA!".format(nama))
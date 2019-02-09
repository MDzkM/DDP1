class OverFlowValueException(Exception):
    pass

# Class untuk objek manusia
class Manusia():
    # Init objek manusia
    def __init__(self, nama, tanggal, bulan, tahun, alamat):
        self.nama = nama
        self.tanggal_lahir = tanggal
        self.bulan_lahir = bulan
        self.tahun_lahir = tahun
        self.alamat = alamat

    # Fungsi untuk mencetak manusia
    def __str__(self):
        result = ""
        result += "Nama: {}\n".format(self.nama)
        result += "Umur: {} tahun\n".format(self.umur(30, 11, 2018))
        result += "Tempat tinggal: {}\n".format(self.alamat)
        return result

    # Fungsi untuk menghitung umur
    def umur(self, tanggal_now, bulan_now, tahun_now):
        umur_sementara = 0
        if (tahun_now > self.tahun_lahir):
            if (bulan_now >= self.bulan_lahir):
                if (tanggal_now >= self.tanggal_lahir):
                    umur_sementara += tahun_now - self.tahun_lahir
                else:
                    umur_sementara += tahun_now - self.tahun_lahir - 1
            else:
                umur_sementara += tahun_now - self.tahun_lahir - 1
        return umur_sementara

# Class untuk objek mahasiswa inherit manusia
# TO-DO lakukan inheritance
class Mahasiswa(Manusia):
    # Init mahasiswa memanggil init Manusia
    def __init__(self, nama, npm, tanggal, bulan, tahun, alamat):
        # TO-DO init
        super().__init__(nama, tanggal, bulan, tahun, alamat)
        self.npm = npm
        # TO-DO dictionary untuk mata kuliah
        self.mata_kuliah = dict()
        self.makananku = "Yoshinoya"

    # Fungsi untuk mencetak mahasiswa
    def __str__(self):
        result = ""
        result += "NPM: {}\n".format(self.npm)
        result += "{} makananku!\n".format(self.makananku)
        result += "IP untuk mata kuliah yang lulus: {:.2f}!\n".format(self.hitung_IP_lulus())
        result += "IP untuk semua mata kuliah: {:.2f}!\n".format(self.hitung_IP_semua())
        return super().__str__() + result

    # Fungsi untuk mengambil matkul
    def ambil_matkul(self, nama, sks):
        # TO-DO code here
        matkul = MataKuliah(nama, sks)
        self.mata_kuliah[nama] = matkul
        # Hint: bikin objek matkul di assign ke dictionary

    # Fungsi untuk menginput nilai dari suatu matkul
    def input_nilai_matkul(self, nama, nilai):
        # TO-DO code here
        self.mata_kuliah[nama].input_nilai(nilai)
        # Hint: Akses matkul terlebih dahulu, update nilai,
        # lalu assign balik lagi ke dictionary

    # Fungsi untuk menghitung IP lulus atau tidak
    def hitung_IP_lulus(self):
        total = 0;
        total_SKS_lulus = 0;
        for matkul in self.mata_kuliah.values():
            # TO-DO bagaimana kode untuk mengecek dia lulus??
            # Apa yang harus diubah??
            if matkul.nilai_IP() >= 2.0:
                total += matkul.nilai_IP() * matkul.sks
                total_SKS_lulus += matkul.sks


        if total_SKS_lulus == 0:
            return 0

        return total/total_SKS_lulus

    # Fungsi untuk menghitung total IP
    def hitung_IP_semua(self):
        total = 0
        total_SKS = 0
        for matkul in self.mata_kuliah.values():
            # TO-DO bagaimana kode untuk menghitung IP total??
            total += matkul.nilai_IP() * matkul.sks
            total_SKS += matkul.sks

        if total_SKS == 0:
            return 0

        return total/total_SKS

# Class untuk objek mata kuliah
class MataKuliah():
    # Objek dictionary untuk referensi nilai
    referensi_IP = {"A": 4.0,
                    "A-": 3.7,
                    "B+": 3.3,
                    "B": 3.0,
                    "B-": 2.7,
                    "C+": 2.3,
                    "C": 2.0,
                    "D": 1.0,
                    "E": 0.0}

    # Init dari objek mata kuliah
    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks
        self.nilai_angka = 0

    # Fungsi untuk mengambil bobot dari IP
    def nilai_IP(self):
        return MataKuliah.referensi_IP[self.nilai_huruf()]

    # Fungsi untuk mengambil nilai huruf dari suatu IP
    def nilai_huruf(self):
        if (self.nilai_angka in range(85, 111)):
            return "A"
        elif (self.nilai_angka in range(80, 85)):
            return "A-"
        elif (self.nilai_angka in range(75, 80)):
            return "B+"
        elif (self.nilai_angka in range(70, 75)):
            return "B"
        elif (self.nilai_angka in range(65, 70)):
            return "B-"
        elif (self.nilai_angka in range(60, 65)):
            return "C+"
        elif (self.nilai_angka in range(55, 60)):
            return "C"
        elif (self.nilai_angka in range(40, 55)):
            return "D"
        elif (self.nilai_angka in range(0, 40)):
            return "E"
        else:
            return "NaN"

    # Fungsi untuk menginput nilai dari mata kuliah ini
    def input_nilai(self, nilai):
        self.nilai_angka = nilai

# main function untuk menjalankan program
def main():
    daftar_mahasiswa = dict()
    still_work_hour = True
    while (still_work_hour):
        try:
            command = input("Masukkan event yang terjadi: ").split() # list

            # tipe maba
            if (command[0].upper() == "MABA"):
                # Contoh: Maba Kace 1706017060 27 09 1999 Pocin
                # TO-DO: akses input satu-satu
                nama = command[1]
                npm = command[2]
                tanggal = command[3]
                bulan = command[4]
                tahun = command[5]
                alamat = command[6]
                # TO-DO: Jika input salah raise error
                if len(command) != 7:
                    raise IndexError

                for word in range(4):
                    if word.isnumeric() == False:
                        raise ValueError

                if npm < 0 or npm > 1899999999:
                    raise OverFlowValueException

                if tanggal < 1 or tanggal > 31:
                    raise OverFlowValueException

                if bulan < 1 or bulan > 12:
                    raise OverFlowValueException

                if tahun < 1990 or tahun > 2018:
                    raise OverFlowValueException
                # Key: string nama, value: objek mahasiswa
                # TO-DO: buat objek mahasiswa dan masukkan ke dictionary daftar_mahasiswa
                mahasiswa = Mahasiswa(nama, npm, tanggal, bulan, tahun, alamat)
                daftar_mahasiswa[nama] = mahasiswa

                print("Mahasiswa dengan nama {} dan NPM {} terdaftar!".format(command[1], command[2]))

            # tipe ambil matkul
            elif (command[0].upper() == "AMBILMATKUL"):
                # Contoh: AmbilMatkul Kace DDP1 4

                # Udah ada mabanya
                if (command[1] in daftar_mahasiswa.keys()):
                    sks = int(command[3])

                    # TO-DO: SKS gak sesuai
                    if sks < 1 or sks > 144:
                        raise OverFlowValueException

                    # mahasiswa ambil matkul
                    mahasiswa = daftar_mahasiswa[command[1]]
                    mahasiswa.ambil_matkul(command[2], int(command[3]))
                    print("{} mengambil mata kuliah {}!".format(command[1], command[2]))

                # Belum terdaftar
                else:
                    print("Mahasiswa dengan nama {} belum terdaftar!".format(command[1]))

            # tipe input nilai
            elif (command[0].upper() == "INPUTNILAI"):
                # Contoh: InputNilai Kace DDP1 85

                if (command[1] in daftar_mahasiswa.keys()):
                    nilai = int(command[3])

                    # TO-DO: Nilai gak sesuai
                    if nilai < 0 or nilai > 110:
                        raise OverFlowValueException

                    # Ada matkulnya input nilai
                    # TO-DO: akses mahasiswa
                    mahasiswa = daftar_mahasiswa[command[1]]
                    if (command[2] in mahasiswa.mata_kuliah.keys()):
                        mahasiswa.input_nilai_matkul(command[2], nilai)
                        print("Nilai dari mata kuliah {} yang diambil oleh {} adalah {}!".format(command[2], command[1], int(command[3])))

                    # gak ada matkulnya
                    else:
                        print("{} belum mengambil mata kuliah {}".format(command[1], command[2]))

                # Mahasiswa belom terdaftar
                else:
                    print("Mahasiswa dengan nama {} belum terdaftar!".format(command[1]))

            # Tipe hitung IP
            elif (command[0].upper() == "HITUNGIP"):
                # Contoh: HitungIP Kace
                if (command[1] in daftar_mahasiswa.keys()):
                    # TO-DO: akses mahasiswa
                    mahasiswa = daftar_mahasiswa[command[1]]
                    print("IP untuk mata kuliah yang lulus saja yang diambil oleh {} adalah {:.2f}!".format(command[1], mahasiswa.hitung_IP_lulus()))
                    print("IP untuk semua mata kuliah yang diambil oleh {} adalah {:.2f}!".format(command[1], mahasiswa.hitung_IP_semua()))
                # Belom ada mahasiswanya
                else:
                    print("Mahasiswa dengan nama {} belum terdaftar!".format(command[1]))

            elif (command[0].upper() == "PRINT"):
                # Contoh: Print Kace
                if (command[1] in daftar_mahasiswa.keys()):
                    mahasiswa = daftar_mahasiswa[command[1]]
                    print(mahasiswa)
                else:
                    print("Mahasiswa dengan nama {} belum terdaftar!".format(command[1]))

            elif (command[0].upper() == "PULANG"):
                # Pulang
                print("Sekarang sudah pukul 17.00 Waktu Indonesia Depok. Rey sudah letih dan ingin pulang sambil menikmati indahnya sunset di Depok.")
                still_work_hour = False

            else:
                print("Perintah tidak tersedia.")
        except IndexError:
            print("Banyak parameter yang anda masukkan kurang, Rey!")
        except ValueError:
            print("Ada parameter yang seharusnya berisi bilangan tetapi anda isi dengan non-bilangan.")
        except OverFlowValueException:
            print("Ada nilai bilangan pada parameter yang melewati batas wajar.")
        except KeyboardInterrupt:
            print("\nRey memiliki urusan mendadak sehingga harus meninggalkan pekerjaannya.")
            still_work_hour = False

if __name__ == '__main__':
    main()

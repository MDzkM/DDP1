# TO-DO import test and main file here
from main import *
import unittest

# Class untuk test
class Tutorial12UnitTest(unittest.TestCase):

    # Test umur Manusia
    def test_manusia_umur_func(self):
        manusia = Manusia("Name", 15, 1, 2000, "Address")

        self.assertEqual(manusia.umur(15, 1, 2018), 18)
        self.assertNotEqual(manusia.umur(14, 1, 2018), 18)
        self.assertEqual(manusia.umur(14, 1, 2018), 17)
        self.assertNotEqual(manusia.umur(12, 12, 2017), 17)
        self.assertEqual(manusia.umur(16, 1, 2019), 19)
        self.assertNotEqual(manusia.umur(16, 1, 2018), 19)

    # Test untuk matkul diambil oleh seorang Mahasiswa
    def test_mahasiswa_ambil_matkul_func(self):
        # TO-DO: create some object mahasiswa here

        mahasiswa = Mahasiswa("Name", 1806141334, 15, 1, 2000, "Address")
        self.assertTrue(len(mahasiswa.mata_kuliah) == 0) # Why 0??

        # TO-DO ambil_matkul function on mahasiswa -> check the new length
        # Hint: should be one
        mahasiswa.ambil_matkul("DDP1", 1)
        self.assertTrue(len(mahasiswa.mata_kuliah) == 1)

        # TO-DO ambil_matkul function on mahasiswa -> check the new length
        # Hint: should be two, remember the name of matkul should be different!
        mahasiswa.ambil_matkul("DDP2", 1)
        self.assertTrue(len(mahasiswa.mata_kuliah) == 2)


    # Test untuk hitung IP lulus dari seorang Mahasiswa
    def test_mahasiswa_hitung_ip_lulus(self):
        mahasiswa = Mahasiswa("Name", 1806040201, 15, 1, 2000, "Address")

        mahasiswa.ambil_matkul("Mata Kuliah", 4)
        mahasiswa.input_nilai_matkul("Mata Kuliah", 49)
        # TO-DO check ip_lulus, fungsi apa yang kita gunakan??
        # Hint: IP lulus 0.0
        self.assertAlmostEqual(mahasiswa.hitung_IP_lulus(), 0.0)

        mahasiswa.ambil_matkul("Mata Kuliah 2", 6)
        mahasiswa.input_nilai_matkul("Mata Kuliah 2", 80)
        # TO-DO check ip_lulus terbaru
        # Hint: IP lulus 3.7000000000000006
        self.assertAlmostEqual(mahasiswa.hitung_IP_lulus(), 3.7000000000000006)

        mahasiswa.ambil_matkul("Mata Kuliah 3", 3)
        mahasiswa.input_nilai_matkul("Mata Kuliah 3", 62)
        # TO-DO check ip_lulus terbaru
        # Hint: IP lulus 3.2333333333333334
        self.assertAlmostEqual(mahasiswa.hitung_IP_lulus(), 3.2333333333333334)

    # Test untuk hitung IP semua (lulus + tidak lulus) dari seorang Mahasiswa
    def test_mahasiswa_hitung_ip_semua(self):
        mahasiswa = Mahasiswa("Name", 1806040201, 15, 1, 2000, "Address")
        mahasiswa.ambil_matkul("Mata Kuliah", 4)
        mahasiswa.input_nilai_matkul("Mata Kuliah", 49)
        # TO-DO Check IP total
        # Hint: IP total 1.0
        self.assertAlmostEqual(mahasiswa.hitung_IP_semua(), 1.0)

        mahasiswa.ambil_matkul("Mata Kuliah 2", 6)
        mahasiswa.input_nilai_matkul("Mata Kuliah 2", 80)
        # TO-DO Check IP total
        # Hint: IP total 2.62
        self.assertAlmostEqual(mahasiswa.hitung_IP_semua(), 2.62)


        mahasiswa.ambil_matkul("Mata Kuliah 3", 3)
        mahasiswa.input_nilai_matkul("Mata Kuliah 3", 62)
        # TO-DO Check IP total
        # Hint: IP total 2.5461538461538464
        self.assertAlmostEqual(mahasiswa.hitung_IP_semua(), 2.5461538461538464)

    # Test untuk hitung IP suatu Mata Kuliah
    def test_matkul_nilai_ip(self):
        matkul = MataKuliah("MPKTB", 6)
        matkul.input_nilai(88)
        # TO-DO: Check nilai_IP matkul,
        # fungsi apa yang harus digunakan untuk mengtest nilai sekarang??
        # Hint: IP seharusnya 4.0
        self.assertEqual(matkul.nilai_IP(), 4.0)

        matkul2 = MataKuliah("MPKTA", 6)
        matkul2.input_nilai(41)
        # TO-DO: Check nilai_IP matkul2
        # Hint: IP seharusnya 1.0
        self.assertEqual(matkul2.nilai_IP(), 1.0)

        matkul3 = MataKuliah("DDP1", 4)
        matkul3.input_nilai(69)
        # TO-DO: Check nilai_IP matkul3
        # Hint: IP seharusnya 2.7
        self.assertEqual(matkul3.nilai_IP(), 2.7)

    # Test untuk hitung nilai huruf suatu Mata Kuliah
    def test_matkul_nilai_huruf(self):
        matkul = MataKuliah("MPKTB", 6)
        matkul.input_nilai(88)
        # TO-DO: Check nilai huruf matkul
        # fungsi apa yang harus digunakan untuk mengtest nilai sekarang??
        # Hint: nilai huruf seharusnya A
        self.assertEqual(matkul.nilai_huruf(), 'A')

        matkul2 = MataKuliah("MPKTA", 6)
        matkul2.input_nilai(41)
        # TO-DO: Check nilai huruf matkul
        # Hint: nilai huruf seharusnya D
        self.assertEqual(matkul2.nilai_huruf(), 'D')

        matkul3 = MataKuliah("DDP1", 4)
        matkul3.input_nilai(69)
        # TO-DO: Check nilai huruf matkul
        # Hint: nilai huruf seharusnya B-
        self.assertEqual(matkul3.nilai_huruf(), 'B-')

    # Test untuk hitung IP suatu Mata Kuliah
    def test_matkul_input_nilai(self):
        matkul = MataKuliah("SDA", 4)
        matkul.input_nilai(55)
        self.assertEqual(matkul.nilai_angka, 55)

if __name__ == '__main__':
    unittest.main()

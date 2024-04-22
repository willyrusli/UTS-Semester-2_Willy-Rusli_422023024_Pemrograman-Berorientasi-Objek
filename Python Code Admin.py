class Admin:
    def _init_(self, id, nama, alamat, telepon, email):
        self.id = id
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon
        self.email = email

class Buku:
    def _init_(self, judul, pengarang, tahun_terbit, jumlah):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.jumlah = jumlah

class PerpustakaanUKRIDA:
    def _init_(self):
        self.daftar_mahasiswa = []
        self.inventaris_buku = []

    def daftarkan_mahasiswa_baru(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)
        print(f"Mahasiswa baru {mahasiswa.nama} telah didaftarkan.")

    def tambahkan_buku_baru(self, buku):
        self.inventaris_buku.append(buku)
        print(f"Buku baru {buku.judul} telah ditambahkan ke inventaris.")

    def hapus_buku(self, judul):
        for buku in self.inventaris_buku:
            if buku.judul == judul:
                self.inventaris_buku.remove(buku)
                print(f"Buku {judul} telah dihapus dari inventaris.")
                return
        print(f"Buku dengan judul {judul} tidak ditemukan.")

    def perbarui_informasi_buku(self, judul, informasi_baru):
        for buku in self.inventaris_buku:
            if buku.judul == judul:
                buku.judul = informasi_baru['judul']
                buku.pengarang = informasi_baru['pengarang']
                buku.tahun_terbit = informasi_baru['tahun_terbit']
                buku.jumlah = informasi_baru['jumlah']
                print(f"Informasi buku {judul} telah diperbarui.")
                return
        print(f"Buku dengan judul {judul} tidak ditemukan.")

    def cari_mahasiswa(self, nama):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa.nama == nama:
                return mahasiswa
        return None

    def kelola_pinjaman_buku(self, mahasiswa, buku, tanggal_peminjaman, tanggal_pengembalian):
        # Implementasi manajemen pinjaman buku
        pass

class Mahasiswa:
    def _init_(self, nim, nama, alamat, telepon, email):
        self.nim = nim
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon
        self.email = email

class Perpustakaan:
    def _init_(self):
        self.daftar_mahasiswa = []
        self.daftar_peminjaman = []

    def daftar_mahasiswa_baru(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)
        print(f"Mahasiswa baru {mahasiswa.nama} telah didaftarkan.")

    def cari_buku(self, judul):
        # Implementasi pencarian buku
        pass

    def pinjam_buku(self, mahasiswa, judul):
        # Implementasi peminjaman buku
        pass

    def kembalikan_buku(self, mahasiswa, judul):
        # Implementasi pengembalian buku
        pass

    def perbarui_pinjaman_buku(self, mahasiswa, judul, tanggal_perpanjangan):
        # Implementasi perpanjangan pinjaman buku
        pass

    def lihat_riwayat_peminjaman(self, mahasiswa):
        # Implementasi untuk melihat riwayat peminjaman
        pass
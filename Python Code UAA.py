class UAA:
    def _init_(self, id, nama, alamat, telepon, email):
        self.id = id
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon
        self.email = email

class PerpustakaanUKRIDA:
    def _init_(self):
        self.daftar_mahasiswa = []
        self.inventaris_buku = []

    def perbarui_informasi_buku(self, judul, informasi_baru):
        for buku in self.inventaris_buku:
            if buku['judul'] == judul:
                buku.update(informasi_baru)
                print(f"Informasi buku {judul} telah diperbarui.")
                return
        print(f"Buku dengan judul {judul} tidak ditemukan.")

    def cari_mahasiswa(self, nama):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa['nama'] == nama:
                return mahasiswa
        return None

    def kelola_pinjaman_buku(self, mahasiswa, buku, tanggal_peminjaman, tanggal_pengembalian):
        # Implementasi manajemen pinjaman buku
        pass

    def pembayaran(self, mahasiswa, jumlah_denda):
        # Implementasi pembayaran denda
        pass

class Dosen:
    def _init_(self, nid, nama, alamat, telepon, email):
        self.nid = nid
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon
        self.email = email

class PerpustakaanUKRIDA:
    def _init_(self):
        self.inventaris_buku = []

    def tambahkan_buku_baru(self, buku):
        self.inventaris_buku.append(buku)
        print(f"Buku baru {buku['judul']} telah ditambahkan ke inventaris.")

    def hapus_buku(self, judul):
        for buku in self.inventaris_buku:
            if buku['judul'] == judul:
                self.inventaris_buku.remove(buku)
                print(f"Buku {judul} telah dihapus dari inventaris.")
                return
        print(f"Buku dengan judul {judul} tidak ditemukan.")

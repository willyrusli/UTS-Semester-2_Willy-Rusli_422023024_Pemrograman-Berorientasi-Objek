class Buku:
    def _init_(self, id_buku, judul, pengarang, isbn, subjek):
        self.id_buku = id_buku
        self.judul = judul
        self.pengarang = pengarang
        self.isbn = isbn
        self.subjek = subjek

class PerpustakaanUKRIDA:
    def _init_(self):
        self.inventaris_buku = []

    def buku_tersedia(self, judul):
        for buku in self.inventaris_buku:
            if buku.judul == judul:
                return True
        return False

    def buku_tidak_tersedia(self, judul):
        return not self.buku_tersedia(judul)

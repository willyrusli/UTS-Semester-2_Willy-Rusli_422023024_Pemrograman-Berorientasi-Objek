class PerpustakaanUKRIDA:
    def _init_(self):
        self.inventaris_buku = []

    def tambahkan_buku_baru(self, id_buku, judul, pengarang, isbn, subjek):
        buku_baru = {
            'id_buku': id_buku,
            'judul': judul,
            'pengarang': pengarang,
            'isbn': isbn,
            'subjek': subjek
        }
        self.inventaris_buku.append(buku_baru)
        print(f"Buku baru '{judul}' telah ditambahkan ke sistem perpustakaan.")

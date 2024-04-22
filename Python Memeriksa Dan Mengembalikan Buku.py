class PerpustakaanUKRIDA:
    def _init_(self):
        self.inventaris_buku = []

    def periksa_dan_kembalikan_buku(self, id_buku):
        for buku in self.inventaris_buku:
            if buku['id_buku'] == id_buku:
                if buku['tersedia']:
                    print(f"Buku '{buku['judul']}' telah diperiksa dan siap untuk dikembalikan.")
                else:
                    print(f"Buku '{buku['judul']}' telah dikembalikan ke perpustakaan.")
                    buku['tersedia'] = True
                return
        print("Buku tidak ditemukan dalam inventaris perpustakaan.")

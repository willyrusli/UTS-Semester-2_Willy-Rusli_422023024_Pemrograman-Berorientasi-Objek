class PerpustakaanUKRIDA:
    def _init_(self):
        self.inventaris_buku = []

    def cari_buku(self, kriteria):
        hasil_pencarian = []
        for buku in self.inventaris_buku:
            if kriteria.lower() in buku['judul'].lower() or kriteria.lower() in buku['pengarang'].lower():
                hasil_pencarian.append(buku)
        if hasil_pencarian:
            print("Hasil pencarian:")
            for buku in hasil_pencarian:
                print(f"Judul: {buku['judul']}, Pengarang: {buku['pengarang']}")
        else:
            print("Buku tidak ditemukan.")

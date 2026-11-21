class Buku:
    # Class attribut: penghitung, jumlah buku yang di buat
    jumlah_buku = 0
    total_stok = 0

    # constructor
    def __init__(self, judul, penulis, stok):
        self.judul = judul
        self.penulis = penulis
        self.__stok = 0                 # encapsulation: atribut private
        self.stok = stok                # lewat setter agar divalidasi
        Buku.jumlah_buku += 1
        Buku.total_stok += self.__stok

    # Property
    @property
    def stok(self):
        return self.__stok

    # setter
    @stok.setter
    def stok(self, nilai):
        if nilai < 0:
            raise ValueError("Stok tidak boleh kurang dari 0")
        self.__stok = nilai

    # Method
    def dipinjam(self):
        if self.__stok == 0:
            return False
        self.__stok -= 1    
        Buku.total_stok += 1
        return True

    def dikembalikan(self):
        self.__stok += 1
        Buku.total_stok += 1

    #Class method
    @classmethod
    def jumlah(cls):
        return f"jumlah buku : {cls.jumlah_buku}"

    @classmethod
    def total(cls):
        return f"total stok semua buku : {cls.total_stok}"

    #static method
    @staticmethod
    def hitung_denda(hari_telat):
        return hari_telat * 1000

    def __str__(self):
        return f"judul = {self.judul}\npenulis = {self.penulis}\nstok = {self.stok}"

class Anggota:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.__pinjaman = []            #private

    # method
    def pinjam(self, buku):
        if buku.dipinjam():
            self.__pinjaman.append(buku)
            print(f"{self.nama} meminjam buku '{buku.judul}'")
        else:
            print(f"stok buku '{buku.judul}' habis")

    def kembalikan(self, buku, hari_telat=0):
        if buku in self.__pinjaman:
            self.__pinjaman.remove(buku)
            buku.dikembalikan()
            print(f"{self.nama} mengembalikan buku '{buku.judul}'")
            if hari_telat > 0:
                print(f"denda : Rp.{Buku.hitung_denda(hari_telat)}")
        else:
            print(f"{self.nama} tidak meminjam buku '{buku.judul}'")

    def __str__(self):
        return f"nama = {self.nama}\nnim = {self.nim}\nbuku dipinjam = {len(self.__pinjaman)}"


# ===== program utama ======
buku1 = Buku("Python Dasar", "Budi", 2)
buku2 = Buku("Algoritma", "Siti", 1)
buku3 = Buku("Basis Data", "Andi", 3)

mhs1 = Anggota("Salwa", "14012500124")
mhs2 = Anggota("Zahira", "14012500101")

print(buku1)
print()
print(mhs1)
print()

mhs1.pinjam(buku1)
mhs1.pinjam(buku2)
mhs2.pinjam(buku2)          # stok habis
mhs1.kembalikan(buku2, 3)   # telat 3 hari

print()
print(Buku.jumlah())
print(Buku.total())

# uji setter
try:
    buku3.stok = -1
except ValueError as e:
    print("Error:", e)

    # SALWA SALSABILA FATHYHA (14012500124)
    # 3B-Kom
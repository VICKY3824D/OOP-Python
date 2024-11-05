from abc import ABC, abstractmethod

# membuat kelas Makanan
class Makanan(ABC):
    
    # mendeskripsikan fungsi persiapan secara abstrak
    @abstractmethod
    def persiapan():
        pass;
    
    # mendeskripsikan fungsi waktu_memasak secara abstrak
    @abstractmethod
    def waktu_memasak():
        pass;
    
    # mendeskripsikan fungsi suhu_memasak secara abstrak
    @abstractmethod
    def suhu_memasak():
        pass;

# membuat kelas Pasta yang diturunkan  dari kelas Makanan
class Pasta(Makanan):
    
    # mengisikan fungsi  persiapan untuk kelas Pasta
    def persiapan(self):
        return ("pasta, air, garam");
    
    # mengisikan fungsi  waktu_memasak untuk kelas Pasta
    def waktu_memasak(self):
        return ("10 Menit");
    
    # mengisikan fungsi suhu_memasak untuk kelas Pasta
    def suhu_memasak(self):
        return ("90 derajat celcius");

# membuat kelas Sup yang diturunkan  dari kelas Makanan
class Sup(Makanan):
    
    # mengisikan fungsi  persiapan untuk kelas Sup
    def persiapan(self):
        return ("air sayur, garam, bumbu");
    
    # mengisikan fungsi  waktu_memasak untuk kelas Sup
    def waktu_memasak(self):
        return ("20 Menit");

    # mengisikan fungsi  suhu_memasak untuk kelas Sup
    def suhu_memasak(self):
        return ("80 derajat celcius");


nama_makanan = input("Nama makanan: ");

if nama_makanan.lower() ==  "pasta":
    pasta = Pasta(); #membuat objek jika nama_makananya  adalah pasta
    print("mempersiapkan pasta ...");
    print(f"Bahan\t\t: {pasta.persiapan()}"); # menampilkan bahan dari pasta
    print(f"Waktu memasak\t: {pasta.waktu_memasak()}");  # menampilkan waktu memasak dari pasta
    print(f"Suhu\t\t: {pasta.suhu_memasak()}"); #  menampilkan suhu dari pasta
    
elif nama_makanan.lower() == "sup":
    sup = Sup();  #membuat objek jika nama_makananya  adalah sup
    print("mempersiapkan sup ...");  # menampilkan persiapan sup
    print(f"Bahan\t\t: {sup.persiapan()}");  # menampilkan bahan dari sup
    print(f"Waktu memasak\t: {sup.waktu_memasak()}");   # menampilkan waktu memasak dari sup
    print(f"Suhu\t\t: {sup.suhu_memasak()}");  # menampilkan suhu dari sup
    
else:
    print("makanan tidak ditemukan");
        


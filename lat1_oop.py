from abc import ABC, abstractmethod

class Makanan(ABC):
    @abstractmethod
    def persiapan():
        pass;
    
    @abstractmethod
    def waktu_memasak():
        pass;
    
    @abstractmethod
    def suhu_memasak():
        pass;

class Pasta(Makanan):
    def persiapan(self):
        return ("pasta, air, garam");
    
    def waktu_memasak(self):
        return ("10 Menit");
        
    def suhu_memasak(self):
        return ("90 derajat celcius");

class Sup(Makanan):
    def persiapan(self):
        return ("air sayur, garam, bumbu");
    
    def waktu_memasak(self):
        return ("20 Menit");
        
    def suhu_memasak(self):
        return ("80 derajat celcius");
        
nama_makanan = input("Nama makanan: ");

if nama_makanan.lower() ==  "pasta":
    pasta = Pasta();
    print("mempersiapkan pasta ...");
    print(f"Bahan\t\t: {pasta.persiapan()}");
    print(f"Waktu memasak\t: {pasta.waktu_memasak()}");
    print(f"Suhu\t\t: {pasta.suhu_memasak()}");
    
elif nama_makanan.lower() == "sup":
    sup = Sup();
    print("mempersiapkan sup ...");
    print(f"Bahan\t\t: {sup.persiapan()}");
    print(f"Waktu memasak\t: {sup.waktu_memasak()}");
    print(f"Suhu\t\t: {sup.suhu_memasak()}");
    
else:
    print("makanan tidak ditemukan");
        


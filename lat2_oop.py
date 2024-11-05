class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama;
        self.__saldo = saldo;
        
    def deposit(self, jumlah):
        self.__saldo += jumlah;
    
    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup");
        else:
            self.__saldo -= jumlah;
    
    def lihat_saldo(self):
        return self.__saldo;
    
    

print("Pilihan: ");
print("1. Buat Akun ");
print("2. Lihat Saldo ");
print("3. Deposit ");
print("4. Tarik ");

pilihan =  int(input("Masukkan Pilihan: "));
if pilihan == 1:
    nama = input("nama: ");
    saldo = int(input("saldo awal: "));
    akun = AkunBank(nama, saldo);
    print("Akun berhasi dibuat");
    
elif  pilihan == 2:
   print()
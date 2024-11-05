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
            print("Penarikan berhasil.");
    
    def lihat_saldo(self):
        return self.__saldo;

# Dictionary untuk menyimpan akun nasabah berdasarkan nama mereka
akun_nasabah = {};

while True:
    print("\nPilihan: ");
    print("1. Buat Akun ");
    print("2. Lihat Saldo ");
    print("3. Deposit ");
    print("4. Tarik ");
    print("5. Keluar ");

    pilihan = int(input("Masukkan Pilihan: "));
    
    if pilihan == 1:
        nama = input("Nama nasabah: ");
        saldo = int(input("Saldo awal: "));
        
        if nama in akun_nasabah:
            print("Nasabah dengan nama ini sudah ada.");
        else:
            akun_nasabah[nama] = AkunBank(nama, saldo)
            print("Akun berhasil dibuat untuk nasabah:", nama);
    
    elif pilihan == 2:
        nama = input("Masukkan nama nasabah: ");
        if nama in akun_nasabah:
            print(f"Saldo  {nama}: {akun_nasabah[nama].lihat_saldo()}");
        else:
            print("Akun nasabah tidak ditemukan.");
    
    elif pilihan == 3:
        nama = input("Masukkan nama nasabah: ");
        if nama in akun_nasabah:
            jumlah = int(input("Jumlah deposit: "));
            akun_nasabah[nama].deposit(jumlah);
            print("Deposit berhasil.");
        else:
            print("Akun nasabah tidak ditemukan.");
    
    elif pilihan == 4:
        nama = input("Masukkan nama nasabah: ");
        if nama in akun_nasabah:
            jumlah = int(input("Jumlah penarikan: "));
            akun_nasabah[nama].tarik(jumlah);
        else:
            print("Akun nasabah tidak ditemukan.");
    
    elif pilihan == 5:
        print("Terima kasih telah menggunakan layanan kami.");
        break;
    
    else:
        print("Pilihan tidak valid.");

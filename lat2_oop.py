class AkunBank:
    
    # konstruktor menambah nama nasabah dan saldo awal
    def __init__(self, nama, saldo):
        self.nama = nama;
        self.__saldo = saldo; # saldo yang bersifat private
    
    # method untuk  menambahkan saldo
    def deposit(self, jumlah):
        self.__saldo += jumlah;
    
    # method untuk penarikan saldo
    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            # print tidak cukup 
            print("Saldo tidak cukup");
        else:
            self.__saldo -= jumlah;
            print("Penarikan berhasil.");
    
    # method untuk  menampilkan saldo
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
            # jika nama nasabah sudah ada maka  tampilkan pesan
            print("Nasabah dengan nama ini sudah ada.");
        else:
            # membuat akun baru jika  nama nasabah belum ada
            akun_nasabah[nama] = AkunBank(nama, saldo)
            print("Akun berhasil dibuat untuk nasabah:", nama);
    
    elif pilihan == 2:
        nama = input("Masukkan nama nasabah: ");
        if nama in akun_nasabah:
            # jika nasabah ditemukan  maka tampilkan saldonya
            print(f"Saldo  {nama}: {akun_nasabah[nama].lihat_saldo()}");
        else:
            print("Akun nasabah tidak ditemukan.");
    
    elif pilihan == 3:
        nama = input("Masukkan nama nasabah: ");
        if nama in akun_nasabah:
            # jika nama nasabah ditemukan, masukkan jumlah deposit
            jumlah = int(input("Jumlah deposit: "));
            
            # memanggil method deposit() yang melekat pada  objek akun nasabah
            akun_nasabah[nama].deposit(jumlah);
            print("Deposit berhasil.");
        else:
            print("Akun nasabah tidak ditemukan.");
    
    elif pilihan == 4:
        nama = input("Masukkan nama nasabah: ");
        if nama in akun_nasabah:
            # jika nama nasabah ditemukan, masukkan jumlah penarikan
            jumlah = int(input("Jumlah penarikan: "));
            
            # memanggil method tarik() yang melekat pada  objek akun nasabah
            akun_nasabah[nama].tarik(jumlah);
        else:
            print("Akun nasabah tidak ditemukan.");
    
    elif pilihan == 5:
        # keluar/break
        print("Terima kasih telah menggunakan layanan kami.");
        break;
    
    else:
        print("Pilihan tidak valid.");

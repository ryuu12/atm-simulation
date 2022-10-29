#
# Program Simulasi Mesin ATM.
# Source code utama: main.py
# 
# Dirancang oleh: Rayhan Rusyd (16722042), Fathi Aurasaliha Thorifah (16722072), Adi Achmad Farhan (16722272), Shabreen Tsabitha Fiddien (16722127), Daffa Nabil (16722107).
# Dibuat untuk memenuhi Tugas Besar Mata Kuliah Pengenalan Komputer.
#

import os

#Objek Nasabah
class Nasabah:
    def __init__(self, nama, no_rek, pin_atm, bank, saldo):
        self.nama = nama
        self.no_rek = no_rek
        self.saldo = saldo
        self.pin_atm = pin_atm
        self.bank = bank

    def showPIN(self):
        return self.pin_atm 
    
    def showRek(self):
        return self.no_rek 

    def showBank(self):
        return self.bank 

    def showSaldo(self):
        return self.saldo 
    
    def showNama(self):
        return self.nama 

    def ubahPin(self,pin_baru): 
        self.pin_atm = pin_baru

    def kurangSaldo(self,nominal_transfer): 
        self.saldo -= nominal_transfer
    
    def tambahSaldo(self,nominal_transfer): 
        self.saldo += nominal_transfer
    
#Array yang akan digunakan
kode_bank = [876, 865, 812] 
uang_tunai = list() 
user = [ 
    Nasabah("Albert", 12345678, 8989, kode_bank[1], 900000), 
    Nasabah("Andi", 87654321, 1212, kode_bank[0], 900000) 
    ]

#Fungsi devTools() untuk menu "Developer Mode".
def devTools(): 
    print("You are now on developer mode.")
    print("Developer Tools:")
    print("[1] List of arrays\n[2] List of user\n[3] Exit developer mode")
    pilihan = int(input(">"))
    if pilihan == 1: 
        os.system("cls")
        print(f"kode_bank: {kode_bank}")
        print(f"uang_tunai: {uang_tunai}")
        input("Press any key to return...")
        devTools()
    elif pilihan == 2:
        for i in range(len(user)):
            print(f"[User {i+1}]")
            print(f"Nama: {user[i].showNama()}")
            print(f"No Rekening: {user[i].showRek()}")
            print(f"Saldo: {user[i].showSaldo()}")
            print(f"PIN: {user[i].showPIN()}")
            print(f"Kode bank: {user[i].showBank()}")
        input("Press any key to return...")
        devTools()
    if pilihan == 3: 
        inputKartu()
    else:
        devTools() 

#Fungsi gantiPIN() untuk proses pembuatan PIN baru nasabah.
def gantiPIN(nasabah):
    pin_baru = int(input("Masukkan pin baru anda:"))
    konfirmasi_pin = int(input("Konfirmasi pin baru: "))
    if konfirmasi_pin == pin_baru:
        nasabah.ubahPin(pin_baru)
        print("Anda berhasil mengubah PIN anda.")
        input()
        menuUtama(nasabah) 
    else:
        print("Anda salah mengisi konfirmasi PIN.")
        input()
        gantiPIN(nasabah) 

#Fungsi tarikTunai() untuk proses penarikan uang tunai dari ATM.
def tarikTunai(nasabah):
    os.system("cls")
    print("Pecahan uang: 50000") 
    nominal = int(input("Masukkan nominal: ")) 
    if nominal > nasabah.showSaldo(): 
        print("Mohon maaf, saldo anda tidak mencukupi")
        tarikTunai(nasabah) 
    else:
        if nominal % 50000 == 0 : 
            for i in range(nominal//50000): 
                uang_tunai.append(50000) 
                nasabah.kurangSaldo(50000) 
            print("Penarikan selesai.")
            print(f"Sisa saldo anda adalah: {nasabah.showSaldo()}")
            input("Silahkan ambil kartu anda... ")
            inputKartu() 
        else:
            input("Nominal yang anda masukkan tidak dapat diproses...")
            tarikTunai(nasabah) 

#Fungsi transfer() untuk proses transfer uang antar akun nasabah.
def transfer(nasabah, tujuan):
    for i in range(len(user)):
        if user[i].showRek() == tujuan: 
            print(f"Anda akan transfer uang kepada {user[i].showNama()}")
    nominal = nasabah.showSaldo() + 1
    while (nominal > nasabah.showSaldo()):
        nominal = int(input("Masukkan nominal transfer: "))
        if nominal > nasabah.showSaldo():
            print("Maaf, saldo anda tidak mencukupi")
    nasabah.kurangSaldo(nominal)
    for i in range(len(user)):
        if user[i].showRek() == tujuan:
            user[i].tambahSaldo(nominal)
    print(f"Anda berhasil transfer uang sebesar {nominal}")
    print(f"Sisa saldo anda adalah {nasabah.showSaldo()}")
    kembali = input("Kembali ke menu utama? (Y/N) ")
    kembali.lower()
    if kembali == "y":
        menuUtama(nasabah)

#Fungsi cekTransfer() untuk melakukan pengecekan apakah rekening yang dituju valid.
#Fungsi ini dilakukan sebelum transfer()
def cekTransfer(nasabah, bank):
    ada_rekening = False
    while (ada_rekening == False):
        rekening = int(input("Masukkan nomor rekening tujuan: "))
        for i in range(len(user)):
            if user[i].showRek() == rekening and user[i].showBank() == bank:
                transfer(nasabah, rekening)
                ada_rekening=True
        if ada_rekening == False:
            print("Nomor rekening tidak terdaftar atau berada di bank yang salah")

#Fungsi menuTransfer() untuk proses pemilihan bank tujuan dengan memasukkan kode bank.
def menuTransfer(nasabah):
    os.system("cls")
    bank_valid = False
    while (bank_valid==False):
        bank_code = int(input("Masukkan kode bank: "))
        for i in range(len(kode_bank)):
            if bank_code == kode_bank[i]:
                cekTransfer(nasabah, bank_code)
                bank_valid=True
                break

#Fungsi cekSaldo() untuk mengecek saldo nasabah dengan memanggil saldo dari objek Nasabah.
def cekSaldo(nasabah):
    print(f"Saldo anda yang tersisa adalah: {nasabah.showSaldo()}")
    pilihan = input("Kembali ke menu utama? (Y/N)")
    pilihan.lower()
    if pilihan == "y":
        menuUtama(nasabah)

#Fungsi menuUtama() untuk menampilkan opsi yang bisa dipilih oleh nasabah.
def menuUtama(nasabah):
    os.system("cls")
    print("Pilih transaksi yang diinginkan. Ketik angka pilihan untuk memilih.")
    print("[1] Transfer\n[2] Tarik Tunai\n[3] Cek Saldo\n[4] Ubah PIN\n[5] Keluar")
    pilihan = int(input("Pilihan: "))
    if pilihan == 1:
        menuTransfer(nasabah)
    elif pilihan == 2:
        tarikTunai(nasabah)
    elif pilihan == 3:
        cekSaldo(nasabah)
    elif pilihan == 4:
        gantiPIN(nasabah)
    elif pilihan == 5:
        inputKartu()

#Fungsi blokirKartu() untuk menampikan notifikasi bahwa kartu ATM ter-blokir.
def blokirKartu():
    print("Kartu anda terblokir")

#Fungsi inputKartu() untuk proses memasukkan kartu ATM dengan cara menuliskan nomor kartu.
def inputKartu():
    os.system("cls")
    kartu = int(input("Masukkan nomor kartu anda: "))
    ada_kartu = False
    if kartu == 900:
        devTools()
        ada_kartu=True
    for i in range(len(user)):
        if kartu == user[i].showRek():
            menuPin(user[i])
            ada_kartu = True
            break
    if ada_kartu==False:
        print("Kartu tidak terbaca.")

#Fungsi menuPin() untuk memasukkan PIN nasabah.
#Fungsi ini dilakukan setelah menuPin()
def menuPin(nasabah):
    i=0
    konfirmasi_pin = False
    while(i<3 and konfirmasi_pin == False):
        isi_pin = int(input("Masukkan PIN: "))
        if isi_pin == nasabah.showPIN():
            menuUtama(nasabah)
            konfirmasi_pin = True
        else:
            i+=1
    if i==3:
        blokirKartu()

#Fungsi yang akan dijalankan pertama kali adalah inputKartu()
inputKartu()
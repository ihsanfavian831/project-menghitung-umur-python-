from datetime import date

print("=== Program Menghitung Umur ===")
tahun_lahir = int(input("Masukkan Tahun lahir: "))
bulan_lahir = int(input("Masukkan Bulan Lahir (1-12): "))
hari_lahir = int(input("Masukkan Hari Lahir (1-31): "))


hari_ini = date.today()
umur = hari_ini.year - tahun_lahir
bulan = hari_ini.month - bulan_lahir
hari = hari_ini.day - hari_lahir

if (hari_ini.month, hari_ini.day) < (bulan_lahir, hari_lahir):
   umur -= 1
   
print(f"\ntanggal hari ini: {hari_ini}")
print(f"umur kamu sekarang adalah {umur} tahun, bulan {bulan}, hari {hari}")
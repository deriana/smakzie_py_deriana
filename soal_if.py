# Input jam masuk dan jam keluar dalam format 24 jam (misal: 08:30)
jam_masuk = input("Masukkan jam masuk (hh:mm): ")
jam_keluar = input("Masukkan jam keluar (hh:mm): ")

# Pisahkan jam dan menit
jam_masuk = int(jam_masuk.split(":")[0])
menit_masuk = int(jam_masuk.split(":")[1])

jam_keluar = int(jam_keluar.split(":")[0])
menit_keluar = int(jam_keluar.split(":")[1])

# Hitung lama parkir dalam jam
lama_parkir = (jam_keluar - jam_masuk) + (menit_keluar - menit_masuk) / 60

# Hitung biaya parkir
biaya_pertama = 2000
biaya_per_jam_berikutnya = 500

if lama_parkir <= 2:
    biaya_total = biaya_pertama
else:
    biaya_total = biaya_pertama + (lama_parkir - 2) * biaya_per_jam_berikutnya

print(f"Biaya parkir: {biaya_total} Rupiah")
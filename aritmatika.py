harga = int(input("Masukkan harga per item: "))
jumlah = int(input("Masukkan jumlah item: "))
diskon = int(input("Masukkan diskon (dalam persen): "))
total_harga = harga * jumlah
total_harga_setelah_diskon = total_harga - (total_harga * diskon / 100)

print("Harga per item:", harga)
print("Jumlah item:", jumlah)
print("Total harga sebelum diskon:", total_harga)
print("Total harga setelah diskon:", total_harga_setelah_diskon)
import difflib

list1 = ["apel", "jeruk", "mangga"]
list2 = ["apel", "jeruk", "kiwi"]

print("Dif dengan ndiff untuk dua daftar:")
diff = difflib.ndiff(list1, list2)
print('\n'.join(diff))
# Fungsi: Membandingkan dua daftar untuk melihat perbedaan antara elemen.
# Kondisi: Ketika Anda ingin mengetahui perbedaan antara dua koleksi elemen.

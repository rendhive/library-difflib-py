import difflib

diff = ['- Bunga merah', '+ Bunga biru']

restored_text = difflib.restore(diff, 1)
print("Teks yang dipulihkan:")
print(' '.join(restored_text))
# Fungsi: Memulihkan teks dari hasil diff.
# Kondisi: Ketika Anda mendapatkan hasil dari perubahan dan ingin memulihkannya.

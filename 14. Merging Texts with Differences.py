import difflib

text1 = "Kucing"
text2 = "Kucin"

combined_lines = difflib.ndiff(text1.splitlines(), text2.splitlines())
print("Teks yang digabung dengan perbedaannya:")
for line in combined_lines:
    print(line)
# Fungsi: Menggabungkan teks sambil menunjukkan perbedaan.
# Kondisi: Ketika Anda melakukan kolaborasi antara dua teks yang mungkin berbeda.

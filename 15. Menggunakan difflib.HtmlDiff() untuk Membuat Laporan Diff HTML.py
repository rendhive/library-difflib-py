import difflib

text1 = "Ini adalah versi pertama."
text2 = "Ini adalah versi kedua dan lebih baik."

d = difflib.HtmlDiff()
html_diff = d.make_file(text1.splitlines(), text2.splitlines(), fromdesc='Versi Pertama', todesc='Versi Kedua')

with open('diff.html', 'w') as f:
    f.write(html_diff)

print("Laporan diff HTML telah dibuat.")
# Fungsi: Membuat file HTML untuk perbandingan teks.
# Kondisi: Ketika Anda ingin membuat laporan perbandingan visual yang dapat dibagikan.

import difflib

text1 = "Line 1\nLine 2\nLine 3"
text2 = "Line 1\nLine 2 modified\nLine 3"

d = difflib.HtmlDiff()
html_diff = d.make_file(text1.splitlines(), text2.splitlines(), fromdesc='Original', todesc='Modified')

with open('diff_output.html', 'w') as f:
    f.write(html_diff)

print("HTML Diff telah dibuat.")
# Fungsi: Membuat tampilan HTML untuk perbandingan teks.
# Kondisi: Ketika Anda ingin menghasilkan laporan visual dari perbandingan teks.

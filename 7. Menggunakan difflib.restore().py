import difflib

diff = ['- apple', '+ orange']

restored = list(difflib.restore(diff, 1))

print("Teks yang dipulihkan:")
print(' '.join(restored))
# Fungsi: Memulihkan teks dari hasil diff.
# Kondisi: Ketika Anda ingin mengetahui bentuk asli dari hasil diff.

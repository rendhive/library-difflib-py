import difflib

string1 = "Saya suka nasi."
string2 = "Saya suka mie."

diff = difflib.ndiff(string1.split(), string2.split())
print("Fixable differences:")
print('\n'.join(diff))
# Fungsi: Menampilkan perbedaan yang dapat diperbaiki.
# Kondisi: Ketika Anda ingin mendapatkan saran tentang perubahan pada teks.

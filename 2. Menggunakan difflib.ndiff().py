import difflib

string1 = "Saya suka apel."
string2 = "Saya suka orange."

diff = difflib.ndiff(string1.split(), string2.split())
print("Dif dengan ndiff:")
print('\n'.join(diff))
# Fungsi: Menghasilkan perbandingan antara dua string kata-per-kata.
# Kondisi: Ketika Anda ingin mengetahui perbedaan kata antara dua string.

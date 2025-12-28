import difflib

string1 = "Kucing"
string2 = "Kucinng"

diff = difflib.ndiff(string1, string2)
print("Dif karakter dengan ndiff:")
print('\n'.join(diff))
# Fungsi: Menghasilkan perbandingan karakter antara dua string.
# Kondisi: Ketika Anda ingin melihat perbedaan antara karakter secara langsung.

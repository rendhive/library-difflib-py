import difflib

string1 = "Ini adalah teks yang pertama."
string2 = "Ini adalah teks yang kedua."

diff = difflib.context_diff(string1.splitlines(), string2.splitlines(), lineterm='')
print("Dif dengan context_diff:")
print('\n'.join(diff))
# Fungsi: Menghasilkan perbandingan dalam format context diff.
# Kondisi: Ketika Anda ingin konteks tambahan di sekitar perubahan.

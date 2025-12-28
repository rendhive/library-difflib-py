import difflib

string1 = "Hello World!\nThis is a test."
string2 = "Hello Python!\nThis is a test."

diff = difflib.unified_diff(string1.splitlines(), string2.splitlines(), lineterm='')
print("Dif dengan unified_diff:")
print('\n'.join(diff))
# Fungsi: Menghasilkan perbandingan dalam format unified diff.
# Kondisi: Ketika Anda memerlukan tampilan diff yang lebih terstruktur dan lebih formal.

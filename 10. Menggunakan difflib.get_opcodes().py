import difflib

string1 = "Bunga merah"
string2 = "Bunga kuning"

matcher = difflib.SequenceMatcher(None, string1, string2)
opcodes = matcher.get_opcodes()

print("Opcodes:")
print(opcodes)
# Fungsi: Menghasilkan opcode perbandingan antara dua string.
# Kondisi: Ketika Anda ingin mendapatkan detail tentang apa yang ditambahkan, dihapus, atau diubah.

import difflib

text1 = """Kalimat pertama.
Kalimat kedua.
Kalimat ketiga."""
text2 = """Kalimat pertama yang telah diubah.
Kalimat kedua.
Kalimat keempat."""

context_diff = difflib.context_diff(text1.splitlines(), text2.splitlines())
print("Writers Context Diff:")
print('\n'.join(context_diff))
# Fungsi: Memberikan konteks di sekitar baris yang diubah.
# Kondisi: Ketika Anda ingin menambahkan konteks di sekitar perubahan untuk memahami lebih lanjut.

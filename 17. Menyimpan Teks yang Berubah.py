import difflib

original_text = "Hello, how are you?"
modified_text = "Hello, how have you been?"

diff = difflib.ndiff(original_text.split(), modified_text.split())

with open('changes.txt', 'w') as file:
    for line in diff:
        if line.startswith('+ '):
            file.write(line[2:] + "\n")

print("Perubahan disimpan di changes.txt.")
# Fungsi: Menyimpan perubahan yang ditambahkan ke file.
# Kondisi: Ketika Anda ingin merekam semua perubahan yang ditambahkan dari teks asli.

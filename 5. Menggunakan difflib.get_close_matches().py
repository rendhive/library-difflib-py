import difflib

word = "appel"
word_list = ["apple", "banana", "orange"]
matches = difflib.get_close_matches(word, word_list)

print("Kata terdekat:")
print(matches)
# Fungsi: Mencari kata terdekat dari list yang diberikan.
# Kondisi: Ketika Anda ingin memberikan saran kata yang benar kepada pengguna.

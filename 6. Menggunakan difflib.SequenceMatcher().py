import difflib

string1 = "Python is great"
string2 = "Python is awesome"

matcher = difflib.SequenceMatcher(None, string1, string2)
ratio = matcher.ratio()

print("Rasio Kesamaan:")
print(ratio)
# Fungsi: Menghitung rasio kesamaan antara dua sekuens.
# Kondisi: Ketika Anda ingin mengetahui tingkat kesamaan antara dua string.

import difflib

text1 = "Atlantis is a fictional island."
text2 = "Atlantis is a legendary island."

matcher = difflib.SequenceMatcher(None, text1, text2)
similarity_ratio = matcher.ratio()

print("Rasio kesamaan teks:")
print(similarity_ratio)
# Fungsi: Menghitung rasio kesamaan antara dua teks.
# Kondisi: Ketika Anda perlu menilai seberapa dekat dua teks.

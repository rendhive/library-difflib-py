import difflib

text1 = "Kucing sangat lucu."
text2 = "Kucing itu lucu sekali."

matcher = difflib.SequenceMatcher(None, text1, text2)
match_histogram = matcher.get_matching_blocks()

print("Histogram kesamaan:")
print(match_histogram)
# Fungsi: Mendapatkan histogram yang menunjukkan kemiripan di berbagai blok.
# Kondisi: Ketika Anda ingin menilai seberapa banyak bagian teks yang cocok.

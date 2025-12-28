import difflib

text_to_fix = "Apel adalah buah yang enak."
suggestions = ["Apel adalah buah yang enak.", "Apel adalah buah yang lezat.", "Apel adalah makanan lezat."]

closest_matches = difflib.get_close_matches(text_to_fix, suggestions)

print("Saran perbaikan:")
print(closest_matches)
# Fungsi: Mencarikan saran perbaikan berdasarkan teks yang diberikan.
# Kondisi: Ketika Anda ingin mengusulkan alternatif teks.

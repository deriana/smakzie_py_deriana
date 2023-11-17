import random

def madlibs_generator():
    # Input words from the user
    noun = input("Masukkan kata benda: ")
    verb = input("Masukkan kata kerja: ")
    adjective = input("Masukkan kata sifat: ")
    adverb = input("Masukkan kata keterangan: ")

    # List of possible stories
    happy_story = f"Sekali waktu, ada seekor {adjective} {noun} yang senang sekali bermain dan {verb} {adverb} setiap hari. Hidupnya penuh dengan kebahagiaan, dan dia hidup bahagia selamanya."
    sad_story = f"Sekali waktu, ada seekor {adjective} {noun} yang selalu merasa sedih dan tidak pernah bisa menemukan kebahagiaan. Meskipun dia mencoba keras untuk {verb} {adverb}, akhirnya hidupnya tidak bahagia."

    # Choose a random story type
    selected_story = random.choice([happy_story, sad_story])

    # Print the selected story with the user's words
    print(selected_story)

# Panggil fungsi madlibs_generator untuk membuat cerita
madlibs_generator()

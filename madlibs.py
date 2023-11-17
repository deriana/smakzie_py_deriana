# Fungsi untuk mengakses file dengan nama yang sesuai
with open("story_sad.txt", "r") as f:
    story = f.read()

# Fungsi untuk mengakses atau mengedit file yang telah diakses
words = []
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story): 
    if char == target_start:
        start_of_word = i
        
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.append(word)
        start_of_word = -1

answers = {}


# Menggunakan jawaban yang sudah ada dan meminta input hanya jika diperlukan
for word in words:
    if word not in answers:
        answer = input("Edit Kalimat Ini " + word + ":")
        answers[word] = answer

    story = story.replace(word, answers[word])

# Menyimpan jawaban ke dalam file eksternal
print(story)

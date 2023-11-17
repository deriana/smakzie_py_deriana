while True:
    print ("==========================================")
    print ("============Madilbs Generator=============")
    print ("==========================================")    
    print ("Opsi Cerita Dari Madlibs Generator")
    print ("1. Cerita Happy Ending 😊")
    print ("2. Cerita Sad Ending 😭")   
    print ("3. Keluar ? 😥")
    print ("==========================================")
    
    choice =int(input("Masukkan pilihan anda :"))
    
    if choice == 1:
        # Fungsi untuk mengakses file dengan nama yang sesuai
        with open("story_happy.txt", "r") as f: #code untuk mengakses nya 
            story = f.read() #membuat variabel untuk file yang sudah di akses tadi

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

        print(story)
        
    elif choice == 2:
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
    
    elif choice == 3:
        print("=========================================")
        print("   TERIMA KASIH TELAH MENGGUNAKAN       ")
        print("       APLIKASI KAMI DI PYTHON          ")
        print("=========================================")
        break
    
    else :
        print ("=====================================")
        print ("=========Authentication Eror=========")
        print ("=====================================")
        
    back = input("Ketik 'apapun' untuk kembali atau 'keluar' untuk keluar:")
    if back.lower() == 'keluar':
        print("=========================================")
        print("   TERIMA KASIH TELAH MENGGUNAKAN       ")
        print("       APLIKASI KAMI DI PYTHON          ")
        print("=========================================")  
        break
    
    
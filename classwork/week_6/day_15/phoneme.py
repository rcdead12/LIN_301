vowels = ["a", "e", "i", "o", "u"]
consonants = ["p", "t", "k", "m", "n", "s", "r", "l"]
sound_checks = {"consonant": 0, "vowel": 0}

while True:
    sound = input("Enter a sound (or quit to quit): ")
    if sound == "quit":
        break
    if sound in vowels:
        sound_checks["vowel"] += 1
        print(sound, "is a vowel.")
    elif sound in consonants:
        sound_checks["consonant"] += 1
        print(sound, "is a consonant.")
    else:
        print(sound, "is something else!")
    print(sound_checks)
word = input("Enter any word: ")

first_letter = word[0]
is_vowel = (first_letter == "a") or (first_letter == "e") or (first_letter == "i") or (first_letter == "o") or (first_letter == "u")

print("First letter ,", first_letter, ", is a vowel --", is_vowel)
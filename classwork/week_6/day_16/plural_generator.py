word = input("Give me an English noun, in the singular: ")

sibilants = ["s", "z", "ʃ", "ʒ", "tʃ", "dʒ"] 
voiceless = ["p", "t", "k", "f", "θ"]

if word[-1] in sibilants:
    plural = word + "ɪz"
elif word[-1] in voiceless:
    plural = word + "s"
else:
    plural = word + "z"
print("Plural: ", plural)
word = "pin"
starts_p = word[0] == "p"
starts_t = word[0] == "t"
starts_k = word[0] == "k"
aspirated = (starts_p == True) or (starts_t == True) or (starts_k == True)

print(word)
print(aspirated)
import re                                               #loads python's regex toolkit

with open("../../../data/gutenburg/alice.txt", encoding="utf-8") as f:  #opens alice.txt
    text = f.read()                                     #reads the whole file into one string, called 'text'

matches_a_q = re.findall(r"[a-q]at", text)   # finds "cat", "cot", or "cut"
print(len(matches_a_q))                      # counts how many were found
print(*matches_a_q, sep="\n")                # prints each match on a separate line
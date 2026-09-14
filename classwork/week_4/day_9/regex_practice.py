import re                                               #loads python's regex toolkit

with open("../../../data/gutenburg/alice.txt", encoding="utf-8") as f:  #opens alice.txt
    text = f.read()                                     #reads the whole file into one string, called 'text'
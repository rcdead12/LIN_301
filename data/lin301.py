import os
import re

HERE = os.path.dirname(__file__)   # the folder lin301.py lives in: data/


def ttr(words):
    return len(set(words)) / len(words)

def ttr_first(words, n=10000):
    return len(set(words[:n])) / len(words[:n])

def avg_word_len(words):
    wd_len_total = 0
    for w in words:
        wd_len_total += len(w)
    return wd_len_total / len(words)

def load_words(filename):
    try:
        with open(os.path.join(HERE, "gutenberg", filename), "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Couldn't find a file — check the filename and location.")
    
    while not lines[0].startswith("*** START"):
        lines = lines[1:]     # chop off the first line
    lines = lines[1:]         # chop off the *** START line itself
    
    while not lines[-1].startswith("*** END"):
        lines = lines[:-1]    # chop off the last line
    lines = lines[:-1]        # chop off the *** END line itself
    
    text = "".join(lines)
    
    ## cleaning and splitting
    words = re.split(r"[\W]+", text.lower())
    return [w for w in words if w != ""]

def report(title, words):
    ttr = len(set(words)) / len(words)
    ttr_10000 = len(set(words[:10000])) / len(words[:10000])

    letters = 0
    for w in words:
        letters += len(w)

    print(title, "TTR:", ttr)
    print(title, "TTR (10,000 words):", ttr_10000)
    print(title, "Average Word Length:", letters / len(words))
    return ttr_10000
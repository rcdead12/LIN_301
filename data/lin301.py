import os
import re
import pandas as pd

HERE = os.path.dirname(__file__)   # the folder lin301.py lives in: data/

stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
             "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
             "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
             "on", "by", "could", "would", "very", "no", "what", "which", "they",
             "were", "there", "me", "an", "must", "this", "said", "from", "or",
             "will", "any", "much", "than", "such", "their", "them", "if", "do",
             "did", "one", "when", "your", "more", "are", "we", "who", "up",
             "out", "down", "into", "s", "t"]

def ttr(words):
    return len(set(words)) / len(words)

def ttr_first(words, n=10000):
    return len(set(words[:n])) / len(words[:n])

def avg_word_len(words):
    total = 0
    for w in words:
        total += len(w)
    return total / len(words)

def ly_rate(words):
    count = 0
    for w in words:
        if w.endswith("ly"):
            count += 1
    return count / len(words) * 1000

def stopword_rate(words, stopwords):
    count = 0
    for w in words:
        if w in stopwords:
            count += 1
    return count / len(words)

def load_text(filename):
    with open(os.path.join(HERE, "gutenberg", filename), "r", encoding="utf-8") as f:
        lines = f.readlines()
    while not lines[0].startswith("*** START"):
        lines = lines[1:]
    lines = lines[1:]
    while not lines[-1].startswith("*** END"):
        lines = lines[:-1]
    lines = lines[:-1]
    return "".join(lines)

def load_words(filename):
    text = load_text(filename)
    words = re.split(r"[\W_]+", text.lower())
    return [w for w in words if w != ""]

def report(title, words):
    print(title, "TTR:", ttr(words))
    print(title, "TTR (10,000 words):", ttr_first(words))
    print(title, "Average Word Length:", avg_word_len(words))
    print(title, "-ly words per 1,000:", ly_rate(words))
    return ttr_first(words)

def book_to_df(filename, label):
    text = load_text(filename)
    chapters = re.split(r"(?im)^CHAPTER\s+(?:[IVXLCDM]+|\d+)\b", text)
    chapters = chapters[1:]
    rows = []
    chapter_num = 0
    for chapter in chapters:
        chapter_num += 1
        words = re.split(r"[\W_]+", chapter.lower())
        words = [w for w in words if w != ""]
        for w in words:
            rows.append({"word": w, "chapter": chapter_num})
    df = pd.DataFrame(rows)
    df["text"] = label
    return df

def add_columns(df, stopwords):
    df["length"] = df["word"].str.len()
    df["is_ly"] = df["word"].str.endswith("ly")
    df["is_stopword"] = df["word"].isin(stopwords)
    return df
import re
from collections import Counter
import matplotlib.pyplot as plt
import urllib.request

stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
             "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
             "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
             "on", "by", "could", "would", "very", "no", "what", "which", "they",
             "were", "there", "me", "an", "must", "this", "said", "from", "or",
             "will", "any", "much", "than", "such", "their", "them", "if", "do",
             "did", "one", "when", "your", "more", "are", "we", "who", "up",
             "out", "down", "into", "s", "t"]

# DOWNLOAD
# url = "https://www.gutenberg.org/ebooks/996.txt.utf-8"  # Don Quixote
# filename = "../../../data/gutenberg/don.txt"

# try:
#     urllib.request.urlretrieve(url, filename)
#     print("Downloaded:", filename)
# except FileNotFoundError:
#     print("Couldn't save the file — does the ../../../data/gutenberg/ folder exist?")

# url = "https://www.gutenberg.org/ebooks/27673.txt.utf-8"  # Oedipus King of Thebes
# filename = "../../../data/gutenberg/oedipus.txt"

# try:
#     urllib.request.urlretrieve(url, filename)
#     print("Downloaded:", filename)
# except FileNotFoundError:
#     print("Couldn't save the file — does the ../../../data/gutenberg/ folder exist?")


# Setup for Don Quixote
try:
    with open("../../../data/gutenberg/don.txt", "r", encoding="utf-8") as f:
        don_lines = f.readlines()
except FileNotFoundError:
    print("Couldn't find that file — check the filename and location.")

while not don_lines[0].startswith("*** START"):
    don_lines = don_lines[1:]     # removes the first line

don_lines = don_lines[1:]

while not don_lines[-1].startswith("*** END"):
    don_lines = don_lines[:-1]    # removes the last line

don_lines = don_lines[:-1]        # removes the *** END line 

don_text = "".join(don_lines)

don_list = re.split(r"[\W]+", don_text.lower())    # reformats words to lowercase
don_list = [w for w in don_list if w != ""]

don_ttr = len(set(don_list)) / len(don_list)    # calculates ttr

don_ttr_10000 = len(set(don_list[:10000])) / len(don_list[:10000])  # calculates ttr for first 10k words

don_wd_len_total = 0
for w in don_list:      # calculates avg word length
    don_wd_len_total += len(w)
don_avg_word_len = don_wd_len_total / len(don_list)

# Setup for Oedipus King of Thebes
try:
    with open("../../../data/gutenberg/oedipus.txt", "r", encoding="utf-8") as f:
        oed_lines = f.readlines()
except FileNotFoundError:
    print("Couldn't find that file — check the filename and location.")

while not oed_lines[0].startswith("*** START"):
    oed_lines = oed_lines[1:]     # removes the first line

oed_lines = oed_lines[1:]

while not oed_lines[-1].startswith("*** END"):
    oed_lines = oed_lines[:-1]    # removes last line

oed_lines = oed_lines[:-1]        # removes the *** END line

oed_text = "".join(oed_lines)

oed_list = re.split(r"[\W]+", oed_text.lower())    # reformats words to lowercase
oed_list = [w for w in oed_list if w != ""]


# CALCULATING DESIRED VARIABLES
oed_ttr = len(set(oed_list)) / len(oed_list)    # calculates ttr
don_ttr = len(set(don_list)) / len(don_list)

print("TTR for Oedipus King of Thebes:", oed_ttr)
print("TTR for Don Quixote:", don_ttr)


oed_ttr_10000 = len(set(oed_list[:10000])) / len(oed_list[:10000])    # calculates ttr for first 10k words
don_ttr_10000 = len(set(don_list[:10000])) / len(don_list[:10000])

print("TTR for Oedipus King of Thebes (10,000 words):", oed_ttr_10000)
print("TTR for Don Quixote (10,000 words):", don_ttr_10000)


oed_word_len_total = 0
for w in oed_list:      # calculates average word length
    oed_word_len_total += len(w)
oed_avg_word_len = oed_word_len_total / len(oed_list)

don_word_len_total = 0
for w in don_list:
    don_word_len_total += len(w)
don_avg_word_len = don_word_len_total / len(don_list)

print("Oedipus King of Thebes average word Length:", oed_avg_word_len)
print("Don Quixote average word Length:", don_avg_word_len)

# finding rate of suffixes per 1000 words
oed_ly_words = [w for w in oed_list if w.endswith("ly")]
oed_ly_per_1k = len(oed_ly_words) / len(oed_list) * 1000
oed_ed_words = [w for w in oed_list if w.endswith("ed")]
oed_ed_per_1k = len(oed_ed_words) / len(oed_list) * 1000
oed_er_words = [w for w in oed_list if w.endswith("er")]
oed_er_per_1k = len(oed_er_words) / len(oed_list) * 1000

don_ly_words = [w for w in don_list if w.endswith("ly")]
don_ly_per_1k = len(don_ly_words) / len(don_list) * 1000
don_ed_words = [w for w in don_list if w.endswith("ed")]
don_ed_per_1k = len(don_ed_words) / len(don_list) * 1000
don_er_words = [w for w in oed_list if w.endswith("er")]
don_er_per_1k = len(don_er_words) / len(don_list) * 1000


print("Rate of words ending in -ly per 1000 words in Oedipus King of Thebes:", oed_ly_per_1k)
print("Rate of words ending in -ed per 1000 words in Oedipus King of Thebes:", oed_ed_per_1k)
print("Rate of words ending in -er per 1000 words in Oedipus King of Thebes:", oed_er_per_1k)

print("Rate of words ending in -ly per 1000 words in Don Quixote:", don_ly_per_1k)
print("Rate of words ending in -ed per 1000 words in Don Quixote:", don_ed_per_1k)
print("Rate of words ending in -er per 1000 words in Don Quixote:", don_er_per_1k)

print("Some words that do not end in these suffixes but rather happen to end in those letters do occur.")


# % of books lines containing dialogue
oed_dialogue_lines = [line for line in oed_lines if "\"" in line] # puts all lines containing a quotation mark into one list
oed_dialogue_percent = len(oed_dialogue_lines) / len(oed_lines) * 100

don_dialogue_lines = [line for line in don_lines if "\"" in line]
don_dialogue_percent = len(don_dialogue_lines) / len(don_lines) * 100

print("Percent of lines in Oedipus King of Thebes containing dialogue:", oed_dialogue_percent)
print("Percent of lines in Don Quixote containing dialogue:", don_dialogue_percent)

# finding top 10 most common words
oed_content = [w for w in oed_list if w not in stopwords] # adding 
oed_top10 = Counter(oed_content).most_common(10)

don_content = [w for w in don_list if w not in stopwords]
don_top10 = Counter(don_content).most_common(10)

print("Top 10 most common content words in Oedipus King of Thebes:", oed_top10)
print("These top 10 words suggest that Oedipus is the main character in this book and it is centered largely around him. The fact that the word 'god' appears so often suggests it is a mythical story.")
print("Top 10 most common content words in Don Quixote:", don_top10)
print("All of these top 10 words are often-used verbs or refer to Don Quixote, with 'don', 'quixote', and 'himself' all being within the top 10. This suggests it is a story very very centered around this character and not much else.")



# Plotting data in bar chart
plt.bar(["Don Quixote", "Oedipus"], [don_ttr_10000, oed_ttr_10000])
plt.title("TTR Comparison: Don Quixote vs. Oedipus King of Thebes")
plt.xlabel("Book")
plt.ylabel("TTR")
plt.show()

# Plotting data in log
oed_freqs = [pair[1] for pair in Counter(oed_list).most_common()] # creating list of most frequent words paired with their frequency
oed_ranks = range(1, len(oed_freqs) + 1) # assigning rank for each of the most common words

plt.plot(oed_ranks, oed_freqs)
plt.title("Rank vs. Frequency for Oedipus King of Thebes (Log Scale)")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.xscale("log")
plt.yscale("log")
plt.show()





# try:
#     with open("../../../data/gutenberg/alice.txt", "r", encoding="utf-8") as f:
#         alice_text = f.read()
# except FileNotFoundError:
#     print("Couldn't find that file — check the filename and location.")

# alice_list = re.split(r"[\W]+", alice_text.lower())    # lowercase this time!
# alice_list = [w for w in alice_list if w != ""]

# alice_content = [w for w in alice_list if w not in stopwords]
# alice_top15 = Counter(alice_content).most_common(15)

# alice_labels = [pair[0] for pair in alice_top15]
# alice_freqs = [pair[1] for pair in alice_top15]

# plt.bar(alice_labels, alice_freqs)
# plt.title("Top 15 Content Words in Alice in Wonderland")
# plt.xlabel("Word")
# plt.ylabel("Frequency")
# plt.xticks(rotation=45)
# plt.tight_layout()    # keeps the rotated labels from getting cut off
# plt.savefig("alice_top15.png")    # saves to the folder you're running from
# plt.show()
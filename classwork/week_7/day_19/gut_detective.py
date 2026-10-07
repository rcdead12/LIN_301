import re
from collections import Counter
import matplotlib.pyplot as plt
import urllib.request

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


# Don Quixote
# try:
#     with open("../../../data/gutenberg/don.txt", "r", encoding="utf-8") as f:
#         don_lines = f.readlines()
# except FileNotFoundError:
#     print("Couldn't find that file — check the filename and location.")

# while not don_lines[0].startswith("*** START"):
#     don_lines = don_lines[1:]     # chop off the first line

# don_lines = don_lines[1:]

# while not don_lines[-1].startswith("*** END"):
#     don_lines = don_lines[:-1]    # chop off the last line

# don_lines = don_lines[:-1]        # chop off the *** END line itself

# don_text = "".join(don_lines)


# Oedipus King of Thebes
try:
    with open("../../../data/gutenberg/oedipus.txt", "r", encoding="utf-8") as f:
        oed_lines = f.readlines()
except FileNotFoundError:
    print("Couldn't find that file — check the filename and location.")

while not oed_lines[0].startswith("*** START"):
    oed_lines = oed_lines[1:]     # chop off the first line

oed_lines = oed_lines[1:]

while not oed_lines[-1].startswith("*** END"):
    oed_lines = oed_lines[:-1]    # chop off the last line

oed_lines = oed_lines[:-1]        # chop off the *** END line itself

oed_text = "".join(oed_lines)

oed_list = re.split(r"[\W]+", oed_text.lower())    # lowercase this time!
oed_list = [w for w in oed_list if w != ""]

oed_tokens = len(oed_list)
oed_types = len(set(oed_list))
oed_ttr = oed_types / oed_tokens

# stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
#              "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
#              "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
#              "on", "by", "could", "would", "very", "no", "what", "which", "they",
#              "were", "there", "me", "an", "must", "this", "said", "from", "or",
#              "will", "any", "much", "than", "such", "their", "them", "if", "do",
#              "did", "one", "when", "your", "more", "are", "we", "who", "up",
#              "out", "down", "into", "s", "t"]

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
austen_opening = ["it", "is", "a", "truth", "universally", "acknowledged", "that", "a",
                   "single", "man", "in", "possession", "of", "a", "good", "fortune",
                   "must", "be", "in", "want", "of", "a", "wife"]

bronte_opening = ["there", "was", "no", "possibility", "of", "taking", "a", "walk",
                   "that", "day", "we", "had", "been", "wandering", "in", "the",
                   "leafless", "shrubbery", "an", "hour", "in", "the", "morning"]

aust_tokens = len(austen_opening)
aust_types = len(set(austen_opening))

bront_tokens = len(bronte_opening)
bront_types = len(set(bronte_opening))

aust_ttr = aust_types / aust_tokens
bront_ttr = bront_types / bront_tokens

print("Austen tokens: ", aust_tokens)
print("Austen types: ", aust_types)

print("Bronte tokens: ", bront_tokens)
print("Bronte types: ", bront_types)

print("Austen TTR: ", aust_ttr)
print("Bronte TTR: ", bront_ttr)
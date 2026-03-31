import hashlib
from itertools import product

# Load MD5 hashes
with open("hashes.txt", "r") as f:
    hashes = set(line.strip() for line in f if line.strip())

# Load wordlist
with open("diceware_cleaned_wordlist_v2.txt", "r") as f:
    words = [w.strip() for w in f if w.strip().isalpha()]

# Apply all-lower and all-upper casing
words_lower = words
words_upper = [w.upper() for w in words]
all_words = words_lower + words_upper

# Special characters allowed
specials = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+', '?']

# Output list for cracked results
cracked = []

# Loop over all combinations
for word1, word2 in product(all_words, repeat=2):
    for sep1 in specials:
        for sep2 in specials:
            candidate = f"{word1}{sep1}liber8{sep2}{word2}"
            hash = hashlib.md5(candidate.encode()).hexdigest()
            if hash in hashes:
                cracked.append(f"{hash}:{candidate}")
                print(f"{hash}:{candidate}")  # Optional: progress output

# Write to file
with open("type3_cracked.txt", "w") as f:
    for entry in cracked:
        f.write(entry + "\n")

print(f"\nDone! {len(cracked)} passwords cracked. Output saved to type3_cracked.txt.")

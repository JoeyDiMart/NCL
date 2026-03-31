import hashlib

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

# Load hash list
with open("hashes.txt", "r") as f:
    hashes = set(line.strip() for line in f)

# Load wordlist
with open("dice_words.txt", "r", encoding="latin-1") as f:
    words = [line.strip().lower() for line in f if line.strip().isalpha()]

found = {}

all_special_chars_list = ['!', '@', '#', '$', '%', '&', '*', '?']

for w1 in words:
    for w2 in words:
        for char1 in all_special_chars_list:
            for char2 in all_special_chars_list:
                pwd = f"{w1}{char1}{w2}{char2}liber8"
                h = md5(pwd)
                if h in hashes:
                    print(f"{h}:{pwd}")
import py7zr
import itertools
import re
import string

archive = "flag.7z"

def valid(p):
    return (len(p) >= 8 and
            re.search(r'[a-z]', p) and
            re.search(r'[A-Z]', p) and
            re.search(r'\d', p) and
            re.search(r'[^a-zA-Z\d]', p))

def try_password(password):
    try:
        with py7zr.SevenZipFile(archive, mode='r', password=password) as z:
            z.readall()
            return True
    except:
        return False

# Leet speak substitutions
def leet_variations(word):
    leet_map = [
        ('a', ['@', '4']),
        ('e', ['3']),
        ('i', ['1', '!']),
        ('o', ['0']),
        ('s', ['$', '5']),
        ('t', ['7']),
        ('l', ['1']),
        ('g', ['9']),
        ('b', ['8']),
    ]
    variations = {word}
    for char, replacements in leet_map:
        new_variations = set()
        for v in variations:
            new_variations.add(v)
            for r in replacements:
                new_variations.add(v.replace(char, r))
                new_variations.add(v.replace(char.upper(), r))
        variations = new_variations
    return variations

bases = [
    "IronMaiden", "Maiden", "UpTheIrons", "Eddie", "Trooper",
    "Killers", "Beast", "Hallowed", "Charlotte", "Phantom",
    "Powerslave", "Seventh", "Moonchild", "Sanctuary", "Purgatory",
    "Wrathchild", "Transylvania", "Harris", "Dickinson", "McBrain",
    "NumberOfTheBeast", "RunToTheHills", "MrPickles", "Pickles",
    "FearOfTheDark", "BraveNewWorld", "DanceOfDeath", "WickerMan",
    "PieceOfMind", "SomewhereinTime", "FinalFrontier",
]

symbols = list("!@#$%&*")
number_chunks = [
    "1", "2", "3", "12", "21", "123", "1234", "666",
    "2022", "22", "2010", "10", "2009", "09", "2008", "08",
    "2007", "07", "2006", "06", "2005", "05", "2004", "04",
    "2003", "03", "1982", "82", "1984", "84", "1980", "80",
]

candidates = set()

for base in bases:
    # Generate leet variations
    leet_vars = leet_variations(base)
    for var in leet_vars:
        for sym in symbols:
            for num in number_chunks:
                candidates.add(f"{var}{num}{sym}")
                candidates.add(f"{var}{sym}{num}")
                candidates.add(f"{num}{var}{sym}")
                candidates.add(f"{var}{num}1{sym}")

# Filter
candidates = [p for p in candidates if valid(p)]
seen = set()
candidates = [p for p in candidates if not (p in seen or seen.add(p))]

total = len(candidates)
print(f"[*] Testing {total} leet+constrained candidates...")

for i, password in enumerate(candidates):
    if i % 500 == 0:
        print(f"\r[{i}/{total}] Testing: {password:<35}", end="", flush=True)
    if try_password(password):
        print(f"\n\n[+] PASSWORD FOUND: {password}")
        exit(0)

print(f"\n[-] Not found in {total} candidates")
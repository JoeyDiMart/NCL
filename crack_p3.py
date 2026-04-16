import py7zr

wordlist = "iron_filtered.txt"
archive = "flag.7z"

with open(wordlist, "r", errors="ignore") as f:
    passwords = f.read().splitlines()

total = len(passwords)
for i, password in enumerate(passwords):
    if i % 500 == 0:
        print(f"\r[{i}/{total}] Testing: {password}", end="", flush=True)
    try:
        with py7zr.SevenZipFile(archive, mode='r', password=password) as z:
            z.readall()
            print(f"\n\n[+] PASSWORD FOUND: {password}")
            break
    except Exception:
        continue
else:
    print("\n[-] Not found")
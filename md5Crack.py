'''
All flags are in the format "SKY-SENH-" followed by 4 digits.
Go through a list of all numbers 0000-9999 and find hash
'''
import hashlib

password_prefix = "SKI-SENH-"
md5_hash = "69ffb0a8ab8861c1ba5574d68e186de1"  # put the md5 hash you want to crack here

for i in range(0000, 10000):
    md5_obj = hashlib.md5()
    password = password_prefix + (str(i).zfill(4))
    md5_obj.update(password.encode('utf-8'))
    hashed_pass = md5_obj.hexdigest()
    print(hashed_pass)
    if md5_hash == hashed_pass:
        print(f"The password: {password}")
        break


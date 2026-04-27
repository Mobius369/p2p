#decryption using the ascii code
msg = input("Enter a message to decrypt: ")
decmsg = ""
for ch in msg:
    asc = ord(ch) - 3
    dech = chr(asc)
    decmsg += dech
print("Decrypted message:",decmsg)

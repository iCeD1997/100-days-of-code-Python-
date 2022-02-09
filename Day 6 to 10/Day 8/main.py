#Caesar Cipher
import os
from art import logo,alphabet

def cipher(en_or_de,shift,message):
    list_message = list(message)
    cipher_message = []
    cipher_final = ("")

    if en_or_de == "encode":
        for x in list_message:
            if x != " ":
                y = alphabet.index(x)
                cipher_message.append(alphabet[y+shift])
            else:
                cipher_message.append(" ")
        for x in cipher_message:
            cipher_final += x
        print(f"Here's the encoded result: {cipher_final}")

    elif en_or_de == "decode":
        for x in list_message:
            if x != " ":
                y = alphabet.index(x)
                cipher_message.append(alphabet[y-shift])
            else:
                cipher_message.append(" ")
        for x in cipher_message:
            cipher_final += x
        print(f"Here's the decoded result: {cipher_final}")

again = 'yes'
while again == 'yes':
    os.system('cls')
    print(logo)
    encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    mess = input("Type your message:\n").lower()
    shift_no = int(input("Type the shift number:\n"))
    cipher(en_or_de=encode_or_decode,shift=shift_no,message=mess)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    


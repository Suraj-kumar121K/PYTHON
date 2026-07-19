alphabet = ['A', 'B', 'C', 'D', 'E', ' F', ' G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position+shift_key
        cipher_text +=  alphabet[new_position]
    print(f"Here's is the text after encryption: {cipher_text}")    

what_to_do = input("type 'encrypt' for encryption,type 'decrypt' for decryption:\n")
text = input("Type your message:\n")
shift=int(input("Enter shift key:\n"))
if what_to_do == "decrypt":
    encryption(plain_text = text, shift_key = shift)
# elif what_to_do=="decrypt":
#     encryption(text,shift)
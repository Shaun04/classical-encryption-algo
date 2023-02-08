import string

alphabets = {}
inv_alphabets = {}

alphabet_list = string.ascii_letters.lower()
for i in range(len(alphabet_list)):
    alphabets[alphabet_list[i]] = i - 26 #strings as keys and numbers as value
    inv_alphabets[i] = alphabet_list[i] #numbers as keys and string as value

def enc_ceaser(key):
    input_data = str(input("Enter the plaintext: "))
    for data in input_data:
        if data in alphabets:
            cipher_text_index = (alphabets[data] + key) % 26 # (P+K) mod 26
            cipher_text = inv_alphabets[cipher_text_index] 
            print(cipher_text, end="") 
        else:
            print("Try only letters, not other characters")

def dec_ceaser(key):
    input_data = str(input("Enter the ciphertext: "))
    for data in input_data:
        if data in alphabets:
            cipher_text_index = (alphabets[data] - key) % 26 # (P-K) mod 26
            cipher_text = inv_alphabets[cipher_text_index] 
            print(cipher_text, end="") 
        else:
            print("Try only letters, not other characters")


choice = input("Enter 1 for Encryption and 2 for decryption: ")

try:
    key = int(input("Enter the key: "))
    if choice == "1":
        enc_ceaser(key)   
    elif choice == "2":
        dec_ceaser(key)
    else:
        print("Enter something valid.")
    
except ValueError:
    print("Error: Key should be only numbers")
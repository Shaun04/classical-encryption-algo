from multiprocessing.sharedctypes import Value


def encryption(key_var):
    text = str(input("Enter the text: "))
    text_list = [x for x in text]
    key = [x for x in key_var]

    #add padding
    while True:
        if len(text_list) % len(key_var) == 0:
            break
        else:
            text_list.append(" ") 

    #adding key to the list
    red = len(text_list) / len(key) - 1

    for i in key:
        if len(key) == len(text_list):
            break
        else:
            add = int(i) + len(key_var)
            key.append(str(add))    
    
    #encryption
    cipher_text = []
    for i in key:
        i = int(i)
        cipher_text.append(text_list[i - 1])
        #print(text_list[i - 1])
    print(''.join(x for x in cipher_text))

def decryption(key_var):
    
    ct = str(input("Enter the ciphertext: "))
    cipher_text = [x for x in ct]
    key = [x for x in key_var]

    #added extended keys
    for i in key:
        if len(key) == len(ct):
            break
        else:
            add = int(i) + len(key_var)
            key.append(str(add))

    dict = {}
    #swapping the indexs and printing the cipher text
    for i in range(len(key)):
        int_i = int(key[i])
        dict[int_i] = cipher_text[i]
        
    decrypted = []
    sorted_dict = sorted(dict.items()) #sorting the dict according to their keys
    
    for i in sorted_dict:
        decrypted.append(i[1])

    print(''.join(x for x in decrypted))


user_input = input("Enter 1 for Encryption and 2 for decryption: ")

try:
    key_var = int(input("Enter the key: "))
    if user_input == "1":
        encryption(str(key_var))    
    elif user_input == "2":
        decryption(str(key_var))
    else:
        print("Enter something valid.")
    
except ValueError:
    print("Key should be only numbers")


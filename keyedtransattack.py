# this is the brute force approach to find the potential keys of the encryption
import time
"""
Statitics:
Length Key | Time Taken(s)
    2           0.004  
    3           0.011
    4           0.072
    5           0.575
    6           6.417
    7          94.801
"""

ct = str(input("Enter the cipher text: "))

def decryption(key_var):
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
    return decrypted


def brute_force(ct):
    print("Calculating.....")
    key_start = "1" * len(ct)
    key_start_int = int(key_start)
    potential_keys = []

    while True:
        if len(str(key_start_int)) > len(ct):
            break
        else:
            key_start_int += 1     
            key_list = [x for x in str(key_start_int)]
            key_list_int = []
            count_num = 0
            for i in key_list:
                count_num += key_list.count(i) #to check the count of the element and if the addition of the count exceeds the len of the string then there are duplicates
                key_list_int.append(int(i))
            """condition below is to check if the keys dont have a 0, have no duplicates and the largest number of the key is 
            equal to the length of the key"""
            if "0" not in key_list and count_num == len(ct) and max(key_list_int) == len(key_list):
                potential_key = ''.join(x for x in key_list)
                potential_keys.append(potential_key)

    print("Now decrypting with the potential keys")
    for i in potential_keys:
        potential_decryption = decryption(i)
        pot_plain_text = ''.join(x for x in potential_decryption)
        print(f'Key used is {i} to get {pot_plain_text}')

start = time.time()
brute_force(ct)
end = time.time()
print(f"Time taken {end - start}")

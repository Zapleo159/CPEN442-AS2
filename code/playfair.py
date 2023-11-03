def preproc_plaintext(plaintext): 
    result = []
    processed_plaintext = plaintext.replace('J', 'I')
    i = 0
    while i < len(processed_plaintext):
        if(processed_plaintext[i] == processed_plaintext[i + 1]):
            result.append(processed_plaintext[i] + 'X')
            i += 1
        else:
            result.append(processed_plaintext[i] + processed_plaintext[i+1])
            i += 2
            
    result =  "".join(result)
    result = (result + 'Z') if (len(result) % 2 != 0) else result
    return result[:300]
        
    
def encrypt(plaintext, key):
    index_arr = [-1, 4, 9, 14, 19, 24]
    print(len(plaintext))
    print(plaintext)
    print(key)
    processed_plaintext = preproc_plaintext(plaintext)
    print(processed_plaintext)
    result = [None] * len(processed_plaintext)
    for iter1 in range(0, len(processed_plaintext), 2):
        i, j = key.find(processed_plaintext[iter1]), key.find(processed_plaintext[iter1+1])
        if ((i % 5) == (j % 5)):
            result[iter1] = key[(i+5) % 25]
            result[iter1 + 1] = key[(j+5) % 25]
        elif (any(index_arr[iter2] < i <= index_arr[iter2 + 1] and index_arr[iter2] < j <= index_arr[iter2 + 1] for iter2 in range(len(index_arr) - 1))):
            if(i in index_arr):
                result[iter1] = key[i - 4]
                result[iter1 + 1] = key[j + 1]
            elif(j in index_arr):
                result[iter1] = key[i + 1]
                result[iter1 + 1] = key[j - 4]
            else:                
                result[iter1] = key[i + 1]
                result[iter1 + 1] = key[j + 1]
        else:
            i_mod, j_mod = (i % 5), (j % 5)
            if(j_mod > i_mod):
                result[iter1] = key[i + (j_mod - i_mod)]
                result[iter1 + 1] = key[j - (j_mod - i_mod)]
            else:
                result[iter1] = key[i - (i_mod - j_mod)]
                result[iter1 + 1] = key[j + (i_mod - j_mod)]
    print("".join(result[:300]))
    return "".join(result[:300]).strip()
    
def decrypt(ciphertext, key):
    index_arr = [-1, 4, 9, 14, 19, 24]
    print(len(ciphertext))
    print(ciphertext)
    print(key)
    
    result = [None] * len(ciphertext)
    for iter1 in range(0, len(ciphertext), 2):
        i, j = key.find(ciphertext[iter1]), key.find(ciphertext[iter1 + 1])
        
        if ((i % 5) == (j % 5)):
            result[iter1] = key[(i - 5) % 25]
            result[iter1 + 1] = key[(j - 5) % 25]
        elif (any(index_arr[iter2] < i <= index_arr[iter2 + 1] and index_arr[iter2] < j <= index_arr[iter2 + 1] for iter2 in range(len(index_arr) - 1))):
            if((i + 4) in index_arr):
                result[iter1] = key[i + 4]
                result[iter1 + 1] = key[j - 1]
            elif((j + 4) in index_arr):
                result[iter1] = key[i - 1]
                result[iter1 + 1] = key[j + 4]
            else:
                result[iter1] = key[i - 1]
                result[iter1 + 1] = key[j - 1]
        else:
            i_mod, j_mod = (i % 5), (j % 5)
            if(j_mod > i_mod):
                result[iter1] = key[i + (j_mod - i_mod)]
                result[iter1 + 1] = key[j - (j_mod - i_mod)]
            else:
                result[iter1] = key[i - (i_mod - j_mod)]
                result[iter1 + 1] = key[j + (i_mod - j_mod)]
    
    print("".join(result))
    return "".join(result).strip()
            
def crack():
    return 0
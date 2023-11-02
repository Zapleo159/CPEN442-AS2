import re

pt_file_path = "q1_plaintexts_group20.txt"
cipher_file_path = "q1_ciphertexts_group20.txt"
key_file_path = "q1_keys_group20.txt"

# ascii_conversion = 65;
# frequency_array = [0.0817, 0.015, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0403, 0.0241, 0.0675, 0.0751, 0.0193, 0.001, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]

# frequencies = [
#     0.0804,  # A
#     0.0148,  # B
#     0.0334,  # C
#     0.0382,  # D
#     0.1249,  # E
#     0.0240,  # F
#     0.0187,  # G
#     0.0505,  # H
#     0.0757,  # I
#     0.0016,  # J
#     0.0054,  # K
#     0.0407,  # L
#     0.0251,  # M
#     0.0723,  # N
#     0.0764,  # O
#     0.0214,  # P
#     0.0012,  # Q
#     0.0628,  # R
#     0.0651,  # S
#     0.0928,  # T
#     0.0105,  # U
#     0.0148,  # V
#     0.0168,  # W
#     0.0023,  # X
#     0.0166,  # Y
#     0.0009   # Z
# ] 

frequency_map = {
    'A': 0.0804,
    'B': 0.0148,
    'C': 0.0334,
    'D': 0.0382,
    'E': 0.1249,
    'F': 0.0240,
    'G': 0.0187,
    'H': 0.0505,
    'I': 0.0757,
    'J': 0.0016,
    'K': 0.0054,
    'L': 0.0407,
    'M': 0.0251,
    'N': 0.0723,
    'O': 0.0764,
    'P': 0.0214,
    'Q': 0.0012,
    'R': 0.0628,
    'S': 0.0651,
    'T': 0.0928,
    'U': 0.0105,
    'V': 0.0148,
    'W': 0.0168,
    'X': 0.0023,
    'Y': 0.0166,
    'Z': 0.0009
}

bigram_map = {
    "TH": 3.56,
    "HE": 3.07,
    "IN": 2.43,
    "ER": 2.05,
    "AN": 1.99,
    "RE": 1.85,
    "ON": 1.76,
    "AT": 1.49,
    "EN": 1.45,
    "ND": 1.35,
    "TI": 1.34,
    "ES": 1.34,
    "OR": 1.28,
    "TE": 1.20,
    "OF": 1.17,
    "ED": 1.17,
    "IS": 1.13,
    "IT": 1.12,
    "AL": 1.09,
    "AR": 1.07,
    "ST": 1.05,
    "TO": 1.04,
    "NT": 1.04,
    "NG": 0.95,
    "SE": 0.93,
    "HA": 0.93,
    "AS": 0.87,
    "OU": 0.87,
    "IO": 0.83,
    "LE": 0.83,
    "VE": 0.83,
    "CO": 0.79,
    "ME": 0.79,
    "DE": 0.76,
    "HI": 0.76,
    "RI": 0.73,
    "RO": 0.73,
    "IC": 0.70,
    "NE": 0.69,
    "EA": 0.69,
    "RA": 0.69,
    "CE": 0.65,
    "LI": 0.62,
    "CH": 0.60,
    "LL": 0.58,
    "BE": 0.58,
    "MA": 0.57,
    "SI": 0.55,
    "OM": 0.55,
    "UR": 0.54,
}




def return_pt_key(pt_file, key_file, cipher_file, cipher_type):
    pt_array = []
    with open(pt_file, "r") as file:
        for line in file:
            pt_array.append(line.strip())
            
    key_array = []
    with open(key_file, "r") as file:
        for line in file:
            key_array.append(line.strip())
            
    cipher_array = []
    with open(cipher_file, "r") as file:
        for line in file:
            cipher_array.append(line.strip())
            
    
    return pt_array[cipher_type], key_array[cipher_type], cipher_array[cipher_type]
         
        
def substitution_encrypt(plaintext, key):
    print(plaintext)
    print(key)
            
    result = []
    for char in plaintext:
        result.append(key[ord(char) - ascii_conversion])
        
    print("".join(result).strip())   
    return "".join(result).strip()
    
def substitution_decrypt(ciphertext, key):
    keymap = {char: index for index, char in enumerate(key)}
    
    print(ciphertext)
    print(key)
            
    result = []
    for char in ciphertext:
        result.append(chr(keymap[char] + ascii_conversion))
        
    print("".join(result).strip())     
    return "".join(result).strip()
    
    
def vigenere_encrypt(plaintext, key):
    key_lenght = len(key)    
    print(plaintext)
    print(key)
            
    result = [None] * len(plaintext)
    for i in range(len(plaintext)):
        key_index = i % key_lenght
        shift = (ord(key[key_index]) + ord(plaintext[i])) % 26
        result[i] = chr(shift + ascii_conversion)
    
    print("".join(result).strip())     
    return "".join(result).strip()
    
def vigenere_decrypt(ciphertext, key):
    key_lenght = len(key)    
    print(ciphertext)
    print(key)
            
    result = [None] * len(ciphertext)
    for i in range(len(ciphertext)):
        key_index = i % key_lenght
        shift = (ord(ciphertext[i]) - ord(key[key_index])) % 26
        result[i] = chr(shift + ascii_conversion)
    
    print("".join(result).strip())   
    return "".join(result).strip()
    
def preproc_plaintext(plaintext):
    result = []
    processed_plaintext = re.sub(r'J', 'I', plaintext)
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
        
    
def playfair_encrypt(plaintext, key):
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
    
def playfair_decrypt(ciphertext, key):
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
            


### Q1.1 

def which_cipher(ciphertext):
    # check if there are no bigrams with repeated letters
    flag = True
    for i in range(0, len(ciphertext), 2):
        if(ciphertext[i] == ciphertext[i + 1]):
            flag = False
            break
    if(flag):
        print("Playfair")
        return 0

    # calculate IC
    letter_count = {char: ciphertext.count(char) for char in ciphertext}
    ic = sum(n * (n - 1) for n in letter_count.values()) / (len(ciphertext) * (len(ciphertext) - 1))
    
    # check if ic is close to english
    if ic > 0.06:
        print("Substitution")
    else:
        print("Vigenere")
    return 0


### Q1.2
def crack_substitution(ciphertext):
    # find most frequent character in ciphertext
    freq = {}
    for char in ciphertext:
        freq[char] = freq.get(char, 0) + 1
    freq = {k: v/len(ciphertext) for k, v in freq.items()}
    
    # convert_to_eng(freq, ciphertext)

    #using bigrams
    bigram_freq = {}
    for i in range(len(ciphertext) - 1):
        bigram = (ciphertext[i], ciphertext[i + 1])
        bigram_freq[bigram] = bigram_freq.get(bigram, 0) + 1

    print(bigram_freq)


def crack_vigenere(ciphertext):
    # find length of key
    key_length = 0
    for i in range (5, 11):
        letter_count = {}
        for j in range(0, len(ciphertext), i):
            char = ciphertext[j]
            letter_count[char] = letter_count.get(char, 0) + 1

        ic = sum(n * (n - 1) for n in letter_count.values()) / (len(ciphertext)/i * (len(ciphertext) - 1)/i)
        if ic > 0.06:
            key_length = i
            break
    print("Key length: " + str(key_length))

    # find key
    key = ""
    slices = []
    for i in range(0, key_length):
        slice = ""
        for j in range(i, len(ciphertext), key_length):
            slice += ciphertext[j]
        print(len(slice))
        slices.append(slice)
    for slice in slices:
        letter_count = {}
        for char in slice:
            letter_count[char] = letter_count.get(char, 0) + 1
        
    # convert_to_eng()

    print("Key: " + key)

def convert_to_eng(cipher_freq, ciphertext):
    sorted_eng = {k: v for k, v in sorted(frequency_map.items(), key=lambda item: item[1], reverse=True)}
    sorted_cipher = {k: v for k, v in sorted(cipher_freq.items(), key=lambda item: item[1], reverse=True)}

    mapped_letters = {cipher: english for cipher, english in zip(sorted_cipher.keys(), sorted_eng.keys())}
    print(mapped_letters)

    plaintext = ""
    for char in ciphertext:
        plaintext += mapped_letters[char]
    print(plaintext)
    return plaintext

    
    
which_cipher("HEDCNTEARXCHVMXZNRMTZIZDAPYRZEXUDPSHCWFEZOTFNDEFHLCUZIWBGBMKPAHAMZXQPTHSLURPNFDXMTQPZDTNQPRZAPUPNORNTNFTTZHMMZWAZFZQVWHOEQKWTNHILBCUIWZMGBXUPMFDKGIZCZNMEMNQHOEQKWTNPEXZQEQWDHDPIQPMRTFHNRAESXEPHYGFNROPCPEMDZUCZMHOEQKWTNQPZNXUPKRQTIPARTPCTPTFZNAPCWVMHLCUIWCRSOBEMZFTULNRCHNDHPTIZDAWXAFXBETZKDTHEFZIWBWB")
which_cipher("AVWETTYEHYWHXEANLWFQIOACPOACJCBOHBLDQGEHHGSUIFOFZDDPGPRTNVLPVWDTYSUIWKWSVRATLBNSPGUPAMLPPBTPDTRTHKZTZXHPOOVGMMICLRZTSBLWLRZXULEWMOURQWEYAODAGPHTSSUAMTNTUUZXAZUYAVWXUIOCAOFIXXOASSACPBSWPTWXVVLFKWFVPBSPEKAKMLAWSQSBMMOEOSUPAMLPMCJPZXAOPBYDNAIDSOKIEBLWHBVIMLTLTSFIBAEJDSJTIELEYOHEMWBJHBSKIEAYJVWPVWHLKHGH") #hospital
# crack_vigenere("AVWETTYEHYWHXEANLWFQIOACPOACJCBOHBLDQGEHHGSUIFOFZDDPGPRTNVLPVWDTYSUIWKWSVRATLBNSPGUPAMLPPBTPDTRTHKZTZXHPOOVGMMICLRZTSBLWLRZXULEWMOURQWEYAODAGPHTSSUAMTNTUUZXAZUYAVWXUIOCAOFIXXOASSACPBSWPTWXVVLFKWFVPBSPEKAKMLAWSQSBMMOEOSUPAMLPMCJPZXAOPBYDNAIDSOKIEBLWHBVIMLTLTSFIBAEJDSJTIELEYOHEMWBJHBSKIEAYJVWPVWHLKHGH") #hospital
which_cipher("TVXLJDOJGBZGTJGZTVXLJDOJGBJXZNZBQXVNGJEJVGXFZIJGVKQZDEZGTVXLJDOJGBGJEJVGXFEKVKQZDQEVDJXZEWEKJHGJEJVGXFEKVKQZDVDMHZDQKZGQDBRVXQNQKWEQKUVKJMQDKFJDZGKFJVEKBGJJDNVDMDVKQZDVNIVGLQDDZGKFJVEKJGDBGJJDNVDMKFJEKVKQZDQEZADJMOWKFJBGJJDNVDMEJNRBZCJGDHJDKVDMAVEGUDOWKFJMVDQEFVGXKQXQDEKQKUKJMVDELIZNVGXJDKJGUDKQNXVV")
crack_substitution("TVXLJDOJGBZGTJGZTVXLJDOJGBJXZNZBQXVNGJEJVGXFZIJGVKQZDEZGTVXLJDOJGBGJEJVGXFEKVKQZDQEVDJXZEWEKJHGJEJVGXFEKVKQZDVDMHZDQKZGQDBRVXQNQKWEQKUVKJMQDKFJDZGKFJVEKBGJJDNVDMDVKQZDVNIVGLQDDZGKFJVEKJGDBGJJDNVDMKFJEKVKQZDQEZADJMOWKFJBGJJDNVDMEJNRBZCJGDHJDKVDMAVEGUDOWKFJMVDQEFVGXKQXQDEKQKUKJMVDELIZNVGXJDKJGUDKQNXVV")
print()

which_cipher("BRLLKNZRDUKPIBKOYDNVKYPULRIIKIRNNVKBRPPKRJEEZKDBKRXNVRNPFDIRLEDONVKJRLLIEWNVKBRLLKNINFZYEZRDUKPIFIKNVKBRPPKNEIFGGEPNNVKXIKLSKIZFPYDOKQKPUYIKIBRPPKJEPAYIZKIYODKZNEJRPXFGNVKBEZMRDZINPKNUVXFIULKINEGPKGRPKWEPUKDNKPJEPAJVKPKNVKMKQKUFNKKQKPUYIKIJYNVEFNNVKBRPPKUKDNKPJEPAYDNVKXYZZLKEWNVKPEEXINRPNIEFNJYNVILE")
crack_substitution("BRLLKNZRDUKPIBKOYDNVKYPULRIIKIRNNVKBRPPKRJEEZKDBKRXNVRNPFDIRLEDONVKJRLLIEWNVKBRLLKNINFZYEZRDUKPIFIKNVKBRPPKNEIFGGEPNNVKXIKLSKIZFPYDOKQKPUYIKIBRPPKJEPAYIZKIYODKZNEJRPXFGNVKBEZMRDZINPKNUVXFIULKINEGPKGRPKWEPUKDNKPJEPAJVKPKNVKMKQKUFNKKQKPUYIKIJYNVEFNNVKBRPPKUKDNKPJEPAYDNVKXYZZLKEWNVKPEEXINRPNIEFNJYNVILE")
which_cipher("MJTXCHHJBYBETQAYUSNHQVIXFLIKOPOTWUUTOFIXFSPIPRWWUXIGRONIEXAKESDQUZIGRWNQARDHYONISIRFLBYQMXEKTBTMQFJBLGHJYSVXOHOYTIUGTHEIEXAMPGASPWTTCHEIXMVBYUISNSSMZBWMQVEAPAAWDMEWSWSXQGOGOKIKQHAGLEUFPVILSSDNQHIGEVEQMXECLGSNZGEMSSNMQLALCSTZDREWECWWUXIGROGFURAGODUGXMSAPRHNEJONCHHGASKBYQAFVELMSCULTMTALGBJQRSTTRTMMXIG") #meatloaf
# crack_vigenere("MJTXCHHJBYBETQAYUSNHQVIXFLIKOPOTWUUTOFIXFSPIPRWWUXIGRONIEXAKESDQUZIGRWNQARDHYONISIRFLBYQMXEKTBTMQFJBLGHJYSVXOHOYTIUGTHEIEXAMPGASPWTTCHEIXMVBYUISNSSMZBWMQVEAPAAWDMEWSWSXQGOGOKIKQHAGLEUFPVILSSDNQHIGEVEQMXECLGSNZGEMSSNMQLALCSTZDREWECWWUXIGROGFURAGODUGXMSAPRHNEJONCHHGASKBYQAFVELMSCULTMTALGBJQRSTTRTMMXIG") #meatloaf
which_cipher("BECMSUDQIQWNWKICXRDTONNMTDQTMSVQXOENGUEOYHOVRGWLWMDUMDEBUSTIXYTWYDDPYXPHOEKVZXXRDAXROENDOEFQOMYUWNXSEWMDEBDQNPWEQAWNIUYXRFQXNMQTBEPVXRMOTCQTMDXRFTODVTNMWYYFTAYSOYTQWRYDIQCXASXRYDHSWMVNTVQXNMQTBEDZHLURRXWNLFTUQXUIUSAPTACXASXROENDOEONYSEODZWKMGZWYLBEQTYGOEWKYHICWQQXCMGQXRNQGQXTPVSCRSWNKSIQVQTXWVQXZDWN")
        
        


        
# substitution_encrypt(*return_pt_key(pt_file_path, key_file_path, cipher_file_path, 0)[:2])
# substitution_decrypt(return_pt_key(pt_file_path, key_file_path, cipher_file_path, 0)[2], return_pt_key(pt_file_path, key_file_path, cipher_file_path, 0)[1])
# vigenere_encrypt(*return_pt_key(pt_file_path, key_file_path, cipher_file_path, 1)[:2])
# vigenere_decrypt(return_pt_key(pt_file_path, key_file_path, cipher_file_path, 1)[2], return_pt_key(pt_file_path, key_file_path, cipher_file_path, 1)[1])
# playfair_encrypt(*return_pt_key(pt_file_path, key_file_path, cipher_file_path, 2)[:2])
# playfair_decrypt(return_pt_key(pt_file_path, key_file_path, cipher_file_path, 2)[2], return_pt_key(pt_file_path, key_file_path, cipher_file_path, 2)[1])
# preproc_plaintext(return_pt_key(pt_file_path, key_file_path, cipher_file_path, 1)[0])

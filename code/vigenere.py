from random import randrange
import letter_data

def vigenere_encrypt(plaintext, key):
    key_length = len(key)    
            
    result = [None] * len(plaintext)
    for i in range(len(plaintext)):
        key_index = i % key_length
        shift = (ord(key[key_index]) + ord(plaintext[i])) % 26
        result[i] = chr(shift + letter_data.ascii_conversion)
    
    return "".join(result).strip()
    
def vigenere_decrypt(ciphertext, key):
    key_length = len(key)    
            
    result = [None] * len(ciphertext)
    for i in range(len(ciphertext)):
        key_index = i % key_length
        shift = (ord(ciphertext[i]) - ord(key[key_index])) % 26
        result[i] = chr(shift + letter_data.ascii_conversion)
    
    return "".join(result).strip()

def crack(ciphertext):
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

    key = "A"*key_length
    best_score = 0
    for i in range(key_length):
        curr_key = key        
        for letter in letter_data.frequency_map.keys():
            curr_key = key[:i] + letter + key[i+1:]
            plaintext = vigenere_decrypt(ciphertext, curr_key)
            curr_score = quadgram_fitness(plaintext)
            if (best_score < curr_score):
                key = curr_key
                best_score = curr_score

    print(key)
    print(vigenere_decrypt(ciphertext, key))

# From https://medium.com/analytics-vidhya/how-to-distinguish-between-gibberish-and-valid-english-text-4975078c5688
def quadgram_fitness(text):
    quadtext = [text[i:i+4] for i in range(len(text)-3)]
    quaddict={}
    with open("quadgrams.txt") as f:
        for line in f:
            quaddict[line.split(",")[0]]= float(line.split(",")[1])

    sum = 0
    for quad in quadtext:
        sum += (quaddict.get(quad.upper(),0))
    return abs(sum)/len(quadtext)

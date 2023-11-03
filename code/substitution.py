import q1
def encrypt(plaintext, key):
    print(plaintext)
    print(key)
            
    result = []
    for char in plaintext:
        result.append(key[ord(char) - q1.ascii_conversion])
        
    return "".join(result).strip()
    
def decrypt(ciphertext, key):
    keymap = {char: index for index, char in enumerate(key)}
    
    print(ciphertext)
    print(key)
            
    result = []
    for char in ciphertext:
        result.append(chr(keymap[char] + q1.ascii_conversion))
        
    return "".join(result).strip()

def crack(ciphertext):
    # find most frequent character in ciphertext
    freq = {}
    for char in ciphertext:
        freq[char] = freq.get(char, 0) + 1
    freq = {k: v/len(ciphertext) for k, v in freq.items()}
    
    # convert_to_eng(freq, ciphertext)

    #using ngrams
    n=4
    ngram_freq = {}
    for i in range(len(ciphertext) - (n-1)):
        ngram = (ciphertext[i], ciphertext[i + (n-1)])
        ngram_freq[ngram] = ngram_freq.get(ngram, 0) + 1
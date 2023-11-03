import letter_data
def encrypt(plaintext, key):
    result = []
    for char in plaintext:
        result.append(key[ord(char) - letter_data.ascii_conversion])
        
    return "".join(result).strip()
    
def decrypt(ciphertext, key):
    print(key)
    keymap = {index: char for index, char in enumerate(key)}
            
    result = []
    for char in ciphertext:
        result.append(keymap[ord(char)-letter_data.ascii_conversion])
  
    return "".join(result).strip()

def crack(ciphertext):
    # find most frequent character in ciphertext
    freq1 = create_n_gram_map(1, ciphertext)
    print_n_gram_map(freq1)

    freq2 = create_n_gram_map(2, ciphertext)
    print_n_gram_map(freq2)
    
    freq3 = create_n_gram_map(3, ciphertext)
    print_n_gram_map(freq3)
    
    freq4 = create_n_gram_map(4, ciphertext)
    print_n_gram_map(freq4)
    
    freq5 = create_n_gram_map(5, ciphertext)
    print_n_gram_map(freq5)
    
    freq6 = create_n_gram_map(6, ciphertext)
    print_n_gram_map(freq6)
    
    freq9 = create_n_gram_map(9, ciphertext)
    print_n_gram_map(freq9)

    letter_map = {
        "A": 'W',
        "B": 'G',
        "C": 'V',
        "D": 'N',
        "E": 'S',
        "F": 'H',
        "G": 'R',
        "H": 'M',
        "I": 'P',
        "J": 'E',
        "K": 'T',
        "L": 'K',
        "M": 'D',
        "N": 'L',
        "O": 'B',
        "P": 'Q',
        "Q": 'I',
        "R": 'F',
        "S": 'X',
        "T": 'Z',
        "U": 'U',
        "V": 'A',
        "W": 'Y',
        "X": 'C',
        "Y": 'J',
        "Z": 'O',
    }

    print(decrypt(ciphertext, "".join(letter_map.values())))


def create_n_gram_map(n, text):
    freq = {}
    for i in range(len(text) - n + 1):
        # get n-gram
        ngram = text[i:i+n]
        freq[ngram] = freq.get(ngram, 0) + 1

    #remove n-grams with frequency 1
    freq = {k: v for k, v in freq.items() if v > 1}
    return freq

def print_n_gram_map(freq, printk=0):
    # print the n-gram map in descending order
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    i = 0
    for key, value in sorted_freq.items():
        print(key, value)
        i += 1
        if i == printk:
            break
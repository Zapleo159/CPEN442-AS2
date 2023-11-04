import letter_data

def substitution_encrypt(plaintext, key):
    print(plaintext)
    print(key)
            
    result = []
    for char in plaintext:
        result.append(key[ord(char) - letter_data.ascii_conversion])
        
    print("".join(result).strip())   
    return "".join(result).strip()
    
def substitution_decrypt(ciphertext, key):
    keymap = {char: index for index, char in enumerate(key)}
    
    print(ciphertext)
    print(key)
            
    result = []
    for char in ciphertext:
        result.append(chr(keymap[char] + letter_data.ascii_conversion))
        
    print("".join(result).strip())     
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
    
    cipher_to_plain = {
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
        "P": None, #Q
        "Q": 'I',
        "R": 'F',
        "S": None, #X
        "T": 'Z',
        "U": 'U',
        "V": 'A',
        "W": 'Y',
        "X": 'C',
        "Y": None, #J
        "Z": 'O',
    }

    plain_to_cipher = {
        "A": 'V',
        "B": 'O',
        "C": 'X',
        "D": 'M',
        "E": 'J',
        "F": 'R',
        "G": 'B',
        "H": 'F',
        "I": 'Q',
        "J": 'Y',
        "K": 'L',
        "L": 'N',
        "M": 'H',
        "N": 'D',
        "O": 'Z',
        "P": 'I',
        "Q": 'P',
        "R": 'G',
        "S": 'E',
        "T": 'K',
        "U": 'U',
        "V": 'C',
        "W": 'A',
        "X": 'S',
        "Y": 'W', 
        "Z": 'T',
    }
    #key: VOXMJRBFQYLNHDZIPGEKUCASWT
    print(embed_plain_in_cipher(cipher_to_plain, ciphertext))
    print('\n')
    substitution_decrypt(ciphertext, "".join(plain_to_cipher.values()))

def embed_plain_in_cipher(cipher_to_plain, ciphertext, print_with_space=True):
    """
    Embeds the plaintext in the ciphertext using the letter map
    In an easy to read way.
    """
    
    embedded_plaintext = ""
    last_char_replaced = False
    
    for char in ciphertext:
        if cipher_to_plain.get(char):
            if print_with_space:
                if last_char_replaced:
                    embedded_plaintext += f"{cipher_to_plain[char].lower()}"
                else:
                    last_char_replaced = True
                    embedded_plaintext += f" {cipher_to_plain[char].lower()}"
            else:
                embedded_plaintext += f"{cipher_to_plain[char].lower()}"
        else:
            if print_with_space:
                if last_char_replaced:
                    embedded_plaintext += f" {char}"
                    last_char_replaced = False
                else:
                    embedded_plaintext += f"{char}"
            else:
                embedded_plaintext += f"{char}"
                
    return embedded_plaintext

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
        
def main():
    file = open('./q1_ciphertexts_group6.txt', 'r')
    data = [line.rstrip('\n') for line in file]
    file.close()

    ciphertext = data[2]
    crack(ciphertext)

if __name__ == "__main__":
    main()
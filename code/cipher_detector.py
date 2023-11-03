import vigenere, playfair, substitution
from twoTimePad import readfile

def which_cipher(ciphertext):
    # check if there are no bigrams with repeated letters
    flag = True
    for i in range(0, len(ciphertext), 2):
        if(ciphertext[i] == ciphertext[i + 1] or ciphertext[i] == 'J'):
            flag = False
            break
    if(flag):
        print("Playfair")
        # playfair.crack(ciphertext)
        return 0

    # calculate IC
    letter_count = {char: ciphertext.count(char) for char in ciphertext}
    ic = sum(n * (n - 1) for n in letter_count.values()) / (len(ciphertext) * (len(ciphertext) - 1))
    
    # check if ic is close to english
    if ic > 0.06:
        print("Substitution")
        substitution.crack(ciphertext)
    else:
        print("Vigenere")
        vigenere.crack(ciphertext)

if __name__ == "__main__":
    ciphertexts = readfile("../q1_ciphertexts_group6.txt")
    for line in ciphertexts:
        which_cipher(line)
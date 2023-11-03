import math
import os
import numpy as np
import random
import concurrent.futures
from vigenere import quadgram_fitness

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
    # print(len(ciphertext))
    # print(ciphertext)
    # print(key)
    
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
    
    # print("".join(result))
    return "".join(result).strip()
            
def create_5x5_matrix(input_string):
    if len(input_string) != 25:
        raise ValueError("Input string must contain exactly 25 characters.")

    matrix = np.array(list(input_string)).reshape(5, 5)
    return matrix

def col_swap(key, c1, c2):
    key_matrix = create_5x5_matrix(key)
    key_matrix[:, [c1,c2]] = key_matrix[:,[c2,c1]]
    return ''.join(key_matrix.flatten())

def row_swap(key, r1, r2):
    key_matrix = create_5x5_matrix(key)
    key_matrix[[r1,r2], :] = key_matrix[[r2,r1], :]
    return ''.join(key_matrix.flatten())

def row_flip(key):
    key_matrix = create_5x5_matrix(key)
    return "".join(np.flipud(key_matrix).flatten())
    
def col_flip(key):
    key_matrix = create_5x5_matrix(key)
    return "".join(np.fliplr(key_matrix).flatten())

def swap_chars(key, index1, index2):
    char_list = list(key)
    if(len(char_list) > 25):
        return key
    else:
        char_list[index1], char_list[index2] = char_list[index2], char_list[index1]
        return ''.join(char_list)
def reverse_string(key):
    return key[::-1]

def shuffleKey(key):
    choice = random.randint(0, 100)
    if(choice in (0,1)):
        return reverse_string(key)
    elif(choice in (2,3)):
        return col_swap(key, random.randint(0,4), random.randint(0,4))
    elif(choice in (4,5)):
        return row_swap(key, random.randint(0,4),random.randint(0,4))
    elif(choice in (6,7)):
        return col_flip(key)
    elif(choice in (8,9)):
        return row_flip(key)
    else:
        ch1, ch2 = random.randint(0, 24), random.randint(0, 24)
        return swap_chars(key, ch1, ch2)

max_tick = 500
def sa_crack(attempts=30000, key='ABCDEFGHIKLMNOPQRSTUVWXYZ', ciphertext='', temperature=0.5, cooling_rate=0.005):
    current_key = key
    current_score = quadgram_fitness(decrypt(ciphertext, current_key))

    best_key = current_key
    best_score = current_score
    tick = 0

    for _ in range(attempts):
        candidate_key = shuffleKey(current_key)
        score = quadgram_fitness(decrypt(ciphertext, candidate_key))

        delta = score - current_score
        delta_ratio = delta / temperature
        if abs(delta_ratio) > 100:
            delta_ratio = math.copysign(100, delta)
        acceptance_rate = math.exp(delta_ratio)
        if random.random() < acceptance_rate:
            current_score = score
            current_key = candidate_key

            if score > best_score:
                tick = 0
                best_score = score
                best_key = current_key
                print("Per attempt: " + str(best_score) + " " +  str(best_key))
            else:
                tick += 1
                if tick > max_tick:
                    tick = 0
                    score = best_score
                    current_key = best_key

        temperature *= 1 - cooling_rate
    print(best_key, decrypt(ciphertext, best_key))
    return best_key, best_score, temperature


def proc_worker(key, ciphertext):
    best_key = key 
    best_score = quadgram_fitness(decrypt(ciphertext, best_key))
    tick = 0
    temperature = 0.05
    cooling_rate = 0.005

    while tick < max_tick:
        key, score, temperature = sa_crack(30000, key, ciphertext, temperature, cooling_rate)
        print(score, key)
        if score > best_score:
            best_score = score
            best_key = key
            tick = 0
            print("Per worker: " + str(best_score) + " " + str(best_key))
        else:
            tick += 1
    return best_score, best_key

def parallel_crack(ciphertext):
    num_workers = 8

    best_key = shuffleKey('ABCDEFGHIKLMNOPQRSTUVWXYZ')
    best_score = quadgram_fitness(decrypt(ciphertext, best_key))
    with concurrent.futures.ProcessPoolExecutor(num_workers) as executor:
        procs = [executor.submit(proc_worker, shuffleKey(best_key), ciphertext) for _ in range(num_workers)]

        for proc in procs:
            score, key = proc.result()
            print(score, key)
            if score > best_score:
                best_score = score
                best_key = key
        executor.shutdown(wait=True)
    print(decrypt(ciphertext, best_key))
    
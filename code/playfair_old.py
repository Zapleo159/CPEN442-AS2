import re
import code.q1 as q1


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

# To access a specific bigram's frequency, you can use the bigram as the key.
print(bigram_map["TH"])  # Example: Accessing the frequency for the bigram "TH"



def playfair_identifier(ciphertext):
    for i in range(0, len(ciphertext), 2):
        if(ciphertext[i] == ciphertext[i+1]):
            return False
    return True

print(playfair_identifier("HEDCNTEARXCHVMXZNRMTZIZDAPYRZEXUDPSHCWFEZOTFNDEFHLCUZIWBGBMKPAHAMZXQPTHSLURPNFDXMTQPZDTNQPRZAPUPNORNTNFTTZHMMZWAZFZQVWHOEQKWTNHILBCUIWZMGBXUPMFDKGIZCZNMEMNQHOEQKWTNPEXZQEQWDHDPIQPMRTFHNRAESXEPHYGFNROPCPEMDZUCZMHOEQKWTNQPZNXUPKRQTIPARTPCTPTFZNAPCWVMHLCUIWCRSOBEMZFTULNRCHNDHPTIZDAWXAFXBETZKDTHEFZIWBWB"))
print(playfair_identifier("AVWETTYEHYWHXEANLWFQIOACPOACJCBOHBLDQGEHHGSUIFOFZDDPGPRTNVLPVWDTYSUIWKWSVRATLBNSPGUPAMLPPBTPDTRTHKZTZXHPOOVGMMICLRZTSBLWLRZXULEWMOURQWEYAODAGPHTSSUAMTNTUUZXAZUYAVWXUIOCAOFIXXOASSACPBSWPTWXVVLFKWFVPBSPEKAKMLAWSQSBMMOEOSUPAMLPMCJPZXAOPBYDNAIDSOKIEBLWHBVIMLTLTSFIBAEJDSJTIELEYOHEMWBJHBSKIEAYJVWPVWHLKHGH"))
print(playfair_identifier("TVXLJDOJGBZGTJGZTVXLJDOJGBJXZNZBQXVNGJEJVGXFZIJGVKQZDEZGTVXLJDOJGBGJEJVGXFEKVKQZDQEVDJXZEWEKJHGJEJVGXFEKVKQZDVDMHZDQKZGQDBRVXQNQKWEQKUVKJMQDKFJDZGKFJVEKBGJJDNVDMDVKQZDVNIVGLQDDZGKFJVEKJGDBGJJDNVDMKFJEKVKQZDQEZADJMOWKFJBGJJDNVDMEJNRBZCJGDHJDKVDMAVEGUDOWKFJMVDQEFVGXKQXQDEKQKUKJMVDELIZNVGXJDKJGUDKQNXVV"))

def playfair_breaker(ciphertext):
    bigram_count = {}
    for i in range(0, len(ciphertext), 2):
        if (ciphertext[i] + ciphertext[i+1]) in bigram_count:
            bigram_count[(ciphertext[i] + ciphertext[i+1])] += 1
        else:
            bigram_count[(ciphertext[i] + ciphertext[i+1])] = 1
    bigram_count = {key: value / len(bigram_count) for key, value in bigram_count.items()}
    print(bigram_count)
    print(sum(bigram_count.values()))
    
    
    
    # #! bigrams should be every char, not every 2 coz we may miss some instances of TH, HE, etc if its like ETHA wed get only ET and HA
    # #am doing every two char to see which ones fit in a row, cuz CA and AC in cipher will correspond to Xi Yi and Yi Xi in plaintext, i'll try doing every char too
    # reversed_pairs = [(key, key[::-1], value, bigram_count[key[::-1]]) for key, value in bigram_count.items() if key[::-1] in bigram_count and key != key[::-1] and key < key[::-1]]
    reversed_pairs = [(key) for key, value in bigram_count.items() if key[::-1] in bigram_count and key != key[::-1] and key < key[::-1]]
    reversed_freq = [(key, key[::-1], value, bigram_map[key[::-1]]) for key, value in bigram_map.items() if key[::-1] in bigram_map and key != key[::-1] and key < key[::-1]]
    # sorted_array = sorted(bigram_count.items(), key=lambda x: x[1], reverse=True)
    
    # print(len(bigram_count))
    # # print(len(reversed_pairs))
    print(reversed_pairs)
    print("   ")
    print(reversed_freq)
    # # print(sorted_array)
    
    dict1 = {}
    alpha = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    for char in alpha:
        for bigram in reversed_pairs:
            if(char in bigram):
                string2 = bigram
                other_char = string2.replace(char, '')
                if(char in dict1):
                    dict1[char].append(other_char)
                else:
                    dict1[char] = [other_char]
    print(dict1)
    
    
playfair_breaker("HEDCNTEARXCHVMXZNRMTZIZDAPYRZEXUDPSHCWFEZOTFNDEFHLCUZIWBGBMKPAHAMZXQPTHSLURPNFDXMTQPZDTNQPRZAPUPNORNTNFTTZHMMZWAZFZQVWHOEQKWTNHILBCUIWZMGBXUPMFDKGIZCZNMEMNQHOEQKWTNPEXZQEQWDHDPIQPMRTFHNRAESXEPHYGFNROPCPEMDZUCZMHOEQKWTNQPZNXUPKRQTIPARTPCTPTFZNAPCWVMHLCUIWCRSOBEMZFTULNRCHNDHPTIZDAWXAFXBETZKDTHEFZIWBWB")

q1.which_cipher('TVXLJDOJGBZGTJGZTVXLJDOJGBJXZNZBQXVNGJEJVGXFZIJGVKQZDEZGTVXLJDOJGBGJEJVGXFEKVKQZDQEVDJXZEWEKJHGJEJVGXFEKVKQZDVDMHZDQKZGQDBRVXQNQKWEQKUVKJMQDKFJDZGKFJVEKBGJJDNVDMDVKQZDVNIVGLQDDZGKFJVEKJGDBGJJDNVDMKFJEKVKQZDQEZADJMOWKFJBGJJDNVDMEJNRBZCJGDHJDKVDMAVEGUDOWKFJMVDQEFVGXKQXQDEKQKUKJMVDELIZNVGXJDKJGUDKQNXVV')


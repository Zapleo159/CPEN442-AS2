import sys

def string_to_binary(s):
  return "".join(format(ord(i), "07b") for i in s)

def binary_to_string(b):
  s = ""
  for i in range(0, len(b), 7):
    s += chr(int(b[i:i+7],2))
  return s

def encrypt(key, plaintext):
  """Take in binary key and string plaintext and return encrypted binary string."""
  
  plaintext_binary = string_to_binary(plaintext)
  encrypted_binary_str = xor(key, plaintext_binary)
  return encrypted_binary_str

def decrypt(key, ciphertext):
  """Take in binary key and binary ciphertext"""
  
  decrypted_binary_str = xor(key, ciphertext)
  decrypted_string = binary_to_string(decrypted_binary_str)
  return decrypted_string

def xor(a, b):
  """XOR two binary strings together and return the resulting binary string."""
  
  xor_binary_str = ""
  for i in range(len(a)):
    xor_binary_str += str(int(a[i]) ^ int(b[i]))
  return xor_binary_str

def readfile(path):
  file = open(path,'r')
  data = [line.rstrip('\n') for line in file]
  file.close()
  return data

def testMessageText(file_name, test_word, ciphertexts_xor):
  with open(f"./output_text_files/{file_name}.txt", "w") as f:
  
    test_word_binary = string_to_binary(test_word)
    
    for i in range(0, len(ciphertexts_xor) - len(test_word_binary), 7):
      right_pad = "".zfill(len(ciphertexts_xor) - len(test_word_binary) - i)
      left_pad = "".zfill(i)
      test_word_binary_padded = left_pad + test_word_binary + right_pad
      xor_val = xor(ciphertexts_xor, test_word_binary_padded)
      relevant_xor = xor_val[i:i+len(test_word_binary)]
      f.write(f"{i/7}: {binary_to_string(relevant_xor)}\n")

def group6(file_name, test_word_formatted):
  ciphertexts = readfile('./q2_ciphertexts_group6.txt')
  ciphertexts_xor = xor(ciphertexts[0], ciphertexts[1])
  testMessageText(file_name, test_word_formatted, ciphertexts_xor)

def group20():
  plaintexts = readfile('../q2_plaintexts_group20.txt')
  ciphertexts = readfile('../q2_ciphertexts_group20.txt')
  keygroup = readfile('../q2_key_group20.txt')
  
  enc1 = encrypt(keygroup[0], plaintexts[0])
  enc2 = encrypt(keygroup[0], plaintexts[1])
  
  dec1 = decrypt(keygroup[0], enc1)
  dec2 = decrypt(keygroup[0], enc2)
  print(dec1 + '\n')
  print(dec2 + '\n')
  
  print(dec1 == plaintexts[0])
  print(dec2 == plaintexts[1])
  
def group6_find_key_and_plaintext_order():
  ciphertexts = readfile('./assignment2_files/q2_ciphertexts_group6.txt')
  
  message = "Crop diversity loss threatens global food security, as the world's human population depends on a diminishing number of varieties of a diminishing number of crop species. Crops are increasingly grown in monoculture, meaning that if, as in the historic Great Famine of Ireland, a single disease overcom"
  message_binary = string_to_binary(message)
  secret_key = xor(message_binary, ciphertexts[0])
  
  plaintext0 = xor(ciphertexts[0], secret_key)
  plaintext0 = binary_to_string(plaintext0)
  plaintext1 = xor(ciphertexts[1], secret_key)
  plaintext1 = binary_to_string(plaintext1)
  
  print(secret_key)
  print(plaintext0)
  print(plaintext1)
  
  
if __name__ == "__main__":
  
  if len(sys.argv) > 1:
    test_word = sys.argv[1]    
    if test_word != "":
      test_words = test_word.split("_")
      test_word_formatted = " ".join(test_words)
      print(test_word_formatted)
      group6(test_word, test_word_formatted)
  
  else:
    group6_find_key_and_plaintext_order()
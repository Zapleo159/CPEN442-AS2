def solution(xs):
    # Your code here
    max_var = "1"
    max_neg = "1"
    for i in sorted(xs, reverse=True, key=lambda x: abs(x)):
        if i < 0:
            max_neg = multiply_big(max_neg,str(i))
            if max_neg[0] != "-":
                max_var = multiply_big(max_var,max_neg)
                max_neg = "1"
        if i > 0:
            max_var = multiply_big(max_var,str(i))

    return max_var

def multiply_big(s1, s2):
    sign = ""
    if s1[0] == '-' and s2[0] == '-':
        s1 = s1[1:]
        s2 = s2[1:]
    elif s1[0] == '-' or s2[0] == '-':
        sign = "-"

    r1 = s1[::-1].rstrip("-")
    r2 = s2[::-1].rstrip("-")
    res = [0]*(len(r1)+len(r2))

    for i in range(len(r1)):
        for j in range(len(r2)):
            res[i+j] += int(r1[i])*int(r2[j])
            res[i+j+1] += res[i+j]//10
            res[i+j] %= 10
    # print (sign + "".join(map(str,res[::-1])).lstrip("0") )
    print(res[::-1])
    return sign + "".join(map(str,res[::-1])).lstrip("0")
print(solution([22108, 3, -421354, -5,0, -6,21234567892]))

# def solution(s):
#     # Your code here

#     dict={
#         'a': '100000',
#         'b': '110000',
#         'c': '100100',
#         'd': '100110',
#         'e': '100010',
#         'f': '110100',
#         'g': '110110',
#         'h': '110010',
#         'i': '010100',
#         'j': '010110',
#         'k': '101000',
#         'l': '111000',
#         'm': '101100',
#         'n': '101110',
#         'o': '101010',
#         'p': '111100',
#         'q': '111110',
#         'r': '111010',
#         's': '011100',
#         't': '011110',
#         'u': '101001',
#         'v': '111001',
#         'w': '010111',
#         'x': '101101',
#         'y': '101111',
#         'z': '101011',
#         ' ': '000000',
#         'CAP': '0000001'
#     }
#     soln = ""
#     for char in s:
#         if(char.isupper()):
#             soln += dict['CAP'] + dict[char.lower()]
#         else:
#             soln += dict[char]
#     return soln

# print(solution("Braille"))
# import q1
# string = 'THESTATIONBEGANBROADCASTINGOCTOBER131947UNDERTHEWBBCCALLSIGNITWASOWNEDBYBOOTHRADIOSTATIONSINCORPORATEDANDWASAMUTUALAFFILIATEWBBCLSOBRIEFLYACBSRADIOAFFILIATEIN1959AFTERWJRINDETROITBRIEFLYDROPPEDITSCBSAFFILIATIONTOBECOMEANINDEPENDENTIN1960WBBCLSPURCHASEDBYROBERTEEASTMANWHOCMANGEDTHECALLLETTERSTOWTRX'
# cipher = 'HEDCNTEARXCHVMXZNRMTZIZDAPYRZEXUDPSHCWFEZOTFNDEFHLCUZIWBGBMKPAHAMZXQPTHSLURPNFDXMTQPZDTNQPRZAPUPNORNTNFTTZHMMZWAZFZQVWHOEQKWTNHILBCUIWZMGBXUPMFDKGIZCZNMEMNQHOEQKWTNPEXZQEQWDHDPIQPMRTFHNRAESXEPHYGFNROPCPEMDZUCZMHOEQKWTNQPZNXUPKRQTIPARTPCTPTFZNAPCWVMHLCUIWCRSOBEMZFTULNRCHNDHPTIZDAWXAFXBETZKDTHEFZIWBWB'
# print(len(string))
# number_to_letter_mapping = {
#     '1': 'A',
#     '2': 'B',
#     '3': 'C',
#     '4': 'D',
#     '5': 'E',
#     '6': 'F',
#     '7': 'G',
#     '8': 'H',
#     '9': 'J'
# }
# result = [None] * len(string)
# for i in range(len(string)):
#     if string[i] in number_to_letter_mapping:
#         result[i] = number_to_letter_mapping[string[i]]
#     else:
#         result[i] = string[i]
        
# result = ''.join(result)
# print(result)
# cipher = q1.preproc_plaintext(result)

# for i in range(0, len(cipher), 2):
#     print(cipher[i] + cipher[i+1])
# count = 0
# for i in range(1000000):
#     count += 1
# print('done')
import random

def initialize_grid():
    return [['' for _ in range(5)] for _ in range(5)]

def is_valid_placement(grid, row, col, character):
    # Check if the character is already in the same row or column
    for i in range(5):
        if grid[row][i] == character or grid[i][col] == character:
            return False
    return True

def solve_grid(grid, character_dict, row, col):
    if row == 5:
        return True
    if grid[row][col] != '':
        next_row, next_col = (row, col + 1) if col < 4 else (row + 1, 0)
        return solve_grid(grid, character_dict, next_row, next_col)
    
    key = list(character_dict.keys())[row]
    values = character_dict[key]
    random.shuffle(values)
    
    for value in values:
        if is_valid_placement(grid, row, col, key) and is_valid_placement(grid, col, row, value):
            grid[row][col] = key
            grid[col][row] = value
            next_row, next_col = (row, col + 1) if col < 4 else (row + 1, 0)
            if solve_grid(grid, character_dict, next_row, next_col):
                return True
            grid[row][col] = ''
            grid[col][row] = ''
    
    return False

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Given character dictionary
character_dict = {
    'A': ['P', 'E', 'W'],
    'C': ['U', 'P'],
    'D': ['Z'],
    'E': ['F', 'Q', 'A', 'P'],
    'F': ['E', 'T'],
    'H': ['S'],
    'I': ['Z'],
    'L': ['U'],
    'M': ['Z'],
    'N': ['T', 'R'],
    'P': ['A', 'T', 'E', 'C'],
    'Q': ['E'],
    'R': ['N'],
    'S': ['H'],
    'T': ['N', 'P', 'F'],
    'U': ['C', 'L'],
    'W': ['A'],
    'Z': ['M', 'I', 'D']
}

# Initialize a 5x5 grid
grid = initialize_grid()

# Try to solve the grid
if solve_grid(grid, character_dict, 0, 0):
    print("Solution found:")
    print_grid(grid)
else:
    print("No solution found.")
import random

# Given character dictionary
character_dict = {
    'A': ['P', 'E', 'W'],
    # 'C': ['U', 'P'],
    # 'D': ['Z'],
    # 'E': ['F', 'Q', 'A', 'P'],
    # 'F': ['E', 'T'],
    # 'H': ['S'],
    # 'I': ['Z'],
    # 'L': ['U'],
    # 'M': ['Z'],
    # 'N': ['T', 'R'],
    # 'P': ['A', 'T', 'E', 'C'],
    # 'Q': ['E'],
    # 'R': ['N'],
    # 'S': ['H'],
    # 'T': ['N', 'P', 'F'],
    # 'U': ['C', 'L'],
    # 'W': ['A'],
    # 'Z': ['M', 'I', 'D']
}

# Initialize the 5x5 grid
grid = [[' ' for _ in range(5)] for _ in range(5)]

# Create a shuffled list of characters (excluding J)
characters = [chr(i) for i in range(65, 91) if i != 74]
random.shuffle(characters)

# Shuffle the values for each character in the character_dict
shuffled_dict = {key: value for key, value in character_dict.items()}
for key in shuffled_dict:
    random.shuffle(shuffled_dict[key])

# Fill the grid while satisfying the rules
for i, key in enumerate(characters):
    row, col = divmod(i, 5)
    grid[row][col] = key
    for j, value in enumerate(shuffled_dict[key]):
        if j != i:
            row, col = divmod(j, 5)
            grid[row][col] = value

# Print the resulting grid
for row in grid:
    print(' '.join(row))


# # Given character dictionary
# character_dict = {
#     'A': ['P', 'E', 'W'],
#     'C': ['U', 'P'],
#     'D': ['Z'],
#     'E': ['F', 'Q', 'A', 'P'],
#     'F': ['E', 'T'],
#     'H': ['S'],
#     'I': ['Z'],
#     'L': ['U'],
#     'M': ['Z'],
#     'N': ['T', 'R'],
#     'P': ['A', 'T', 'E', 'C'],
#     'Q': ['E'],
#     'R': ['N'],
#     'S': ['H'],
#     'T': ['N', 'P', 'F'],
#     'U': ['C', 'L'],
#     'W': ['A'],
#     'Z': ['M', 'I', 'D']
# }

# def error_calc(dict, key):
#     score = 34
#     for i in range(len(key)):
#         if(key[i] in dict)
        
        
        
    

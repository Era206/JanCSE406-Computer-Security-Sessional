from BitVector import *


Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]



round_constant_Matrix = [
    [BitVector(hexstring="01"), BitVector(hexstring="00"), BitVector(hexstring="00"), BitVector(hexstring="00")],
    [BitVector(hexstring="02"), BitVector(hexstring="00"), BitVector(hexstring="00"), BitVector(hexstring="00")],
    [BitVector(hexstring="04"), BitVector(hexstring="00"), BitVector(hexstring="00"), BitVector(hexstring="00")],
    [BitVector(hexstring="08"), BitVector(hexstring="00"), BitVector(hexstring="00"), BitVector(hexstring="00")],
    [BitVector(hexstring="10"), BitVector(hexstring="00"), BitVector(hexstring="00"), BitVector(hexstring="00")],
    [BitVector(hexstring="20"), BitVector(hexstring="00"), BitVector(hexstring="00"), BitVector(hexstring="00")],
    [BitVector(hexstring="40"), BitVector(hexstring="00"), BitVector(hexstring="00"), BitVector(hexstring="00")],
    [BitVector(hexstring="80"), BitVector(hexstring="00"), BitVector(hexstring="00"), BitVector(hexstring="00")],
    [BitVector(hexstring="1B"), BitVector(hexstring="00"), BitVector(hexstring="00"), BitVector(hexstring="00")],
    [BitVector(hexstring="36"), BitVector(hexstring="00"), BitVector(hexstring="00"), BitVector(hexstring="00")]
]


#reading from input files
def read_text_files(file1_path):
    with open(file1_path, 'r') as file1:
        text1 = file1.read()

    return text1


def get_modified_word(matrix1, iteration):
    result = [[None] * len(matrix1[0]) for _ in range(len(matrix1))]
    #circular byte shift(left)
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            value=(j+1)%4
            result[i][j] = matrix1[i][value]

    #replace with substituted value    
    for i in range(len(result)):
        for j in range(len(result[0])):
            value=result[i][j]
            # print(hex(ord(chr(int(value)))))
            int_val = value.intValue()
            # print(int_val)
            s = Sbox[int_val]
            s = BitVector(intVal=s, size=8)
            result[i][j] = s

    # adding part with round constant matrix
    for i in range(len(result)):
        for j in range(len(result[0])):
            value=round_constant_Matrix[iteration][j]
            result[i][j] = result[i][j]^value
    

    return result

def add_words(matrix1, matrix2):
    result = [[None] * len(matrix1[0]) for _ in range(len(matrix1))]
    for i in range(len(result)):
        for j in range(len(result[0])):
            if i==0:
                result[i][j] = matrix1[i][j]^matrix2[i][j]
            else:
                result[i][j] = matrix1[i][j]^result[i-1][j]

    return result


def get_round_key_matrix(text, text_size):
    # Calculate the number of characters required for the matrix
    # print(len(text)*8)
    # jokhon key_size=128 round 11 ta tai 4*11=44 row lagbe
    if text_size==128:
        num_rows=4
        num_cols=4
        iter=11
    # jokhon key_size=192 round 13 ta tai 4*13=52 row lagbe
    elif text_size==192:
        num_rows=6
        num_cols=4
        iter=9
    # jokhon key_size=256 round 15 ta tai 4*15=60 row lagbe
    else:
        num_rows=8
        num_cols=4
        iter=8
    matrix_size = num_rows*iter * num_cols
    # print(matrix_size)

    # Ensure the text length is a multiple of the matrix size
    while len(text)*8 < text_size :
        text += '\x00'

    if len(text)*8 > text_size:
        text=text[:text_size]
    

    # Create an empty 2D matrix to store the BitVectors
    matrix = [[None] * num_cols for _ in range(num_rows)]

    # Convert each character to a BitVector and populate the matrix
    char_index = 0
    for row in range(num_rows):
        for col in range(num_cols):
            char = text[char_index]
            bitvector = BitVector(intVal=ord(char), size=8)
            matrix[row][col] = bitvector
            char_index += 1

    result = [[None] * num_cols for _ in range(num_rows)]
    modified_word=[[None] * num_cols for _ in range(1)]
    # iter 1 kom as matrix e 4 row already added
    for i in range(iter-1):
        
        if i==0:
            # print("yo")
            for k in range(len(result)):
                for j in range(len(result[0])):
                    result[k][j] = matrix[k][j]
            for k in range(len(modified_word)):
                for j in range(len(modified_word[0])):
                    modified_word[k][j] = matrix[num_rows-1][j]

        modified_word=get_modified_word(modified_word, i)
        modified_matrix=add_words(result, modified_word)

        matrix.extend(modified_matrix) 
        
        result=modified_matrix
        modified_word=[matrix[-1]]

    return matrix


def text_to_bitvector_matrix(text, num_rows, num_cols):
    # Calculate the number of characters required for the matrix
    matrix_size = num_rows * num_cols

    # Ensure the text length is a multiple of the matrix size
    while len(text) % matrix_size != 0:
        text += ' '

    # Create an empty 2D matrix to store the BitVectors
    matrix = [[None] * num_cols for _ in range(num_rows)]

    # Convert each character to a BitVector and populate the matrix
    char_index = 0
    for row in range(num_rows):
        for col in range(num_cols):
            char = text[char_index]
            bitvector = BitVector(intVal=ord(char), size=8)
            matrix[row][col] = bitvector
            char_index += 1

    # Transpose the matrix
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    return transposed_matrix


def print_bitvector_as_characters(bitvector):
    # Convert the BitVector to an integer
    integer_value = int(bitvector)

    # Print the corresponding character
    print(chr(integer_value), end='')



def add_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for XOR operation.")

    # Create an empty result matrix
    result = [[None] * len(matrix1[0]) for _ in range(len(matrix1))]

    # Perform XOR operation on corresponding elements
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] ^ matrix2[i][j]

    return result


def get_inv_svalue_matrix(matrix1):
    result = [[None] * len(matrix1[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            value=matrix1[i][j]
            int_val = value.intValue()
            # print(int_val)
            s = InvSbox[int_val]
            s = BitVector(intVal=s, size=8)
            result[i][j] = s


    return result



    return result

def get_inv_rounded_matrix(matrix1):
    result = [[None] * len(matrix1[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            value=(j-i)%4
            result[i][j] = matrix1[i][value]


    return result

def mix_column_matrix(matrix1, matrix2):
    AES_modulus = BitVector(bitstring='100011011')
    # Get dimensions of matrices
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            result[i][j]=BitVector(size=1, intVal=0)
            for k in range(cols1):
                value=matrix1[i][k].gf_multiply_modular(matrix2[k][j], AES_modulus, 8)
                result[i][j] =result[i][j] ^ value
                

    return result



def dividing_text(text,division_size):
    texts=[]
    for i in range(0,len(text), division_size):
        texts.append(text[i:i+division_size])
    
    while len(texts[-1]) <division_size:
        texts[-1] +='\x00'

    return texts




def plain_text_generation(text, round_key_matrix,key_size):
    plain_text=[]
    if key_size==128:
        round=11
        last_round=10
    elif key_size==192:
        round=13
        last_round=12
    else:
        round=15
        last_round=14
    
    # round 0 er count, sobar jnno same
    plain_text=text_to_bitvector_matrix(text,4,4)
    transposed_key_matrix = round_key_matrix[last_round*4:(last_round*4)+4]
    transposed_key_matrix = [[transposed_key_matrix[j][i] for j in range(len(transposed_key_matrix))] for i in range(len(transposed_key_matrix[0]))]
    plain_text=add_matrices(plain_text, transposed_key_matrix)

    for i in range(round-2,0,-1):
        inv_rounded_matrix=get_inv_rounded_matrix(plain_text)
        inv_substituted_matrix=get_inv_svalue_matrix(inv_rounded_matrix)
        transposed_key_matrix=round_key_matrix[i*4:(i*4) + 4]
        transposed_key_matrix = [[transposed_key_matrix[j][i] for j in range(len(transposed_key_matrix))] for i in range(len(transposed_key_matrix[0]))]
        add_round_key_matrix=add_matrices(inv_substituted_matrix,transposed_key_matrix )
        # rounded_BitVector_matrix=hex_to_BitVector_matrix(rounded_matrix)
        plain_text=mix_column_matrix(InvMixer, add_round_key_matrix)
        
        # plain_text=add_matrices(mix_column,transposed_key_matrix)
       
    inv_rounded_matrix=get_inv_rounded_matrix(plain_text)
    inv_substituted_matrix=get_inv_svalue_matrix(inv_rounded_matrix)
    transposed_key_matrix=round_key_matrix[:4]
    transposed_key_matrix = [[transposed_key_matrix[j][i] for j in range(len(transposed_key_matrix))] for i in range(len(transposed_key_matrix[0]))]
    plain_text=add_matrices(inv_substituted_matrix,transposed_key_matrix )
    plain_text=[[plain_text[j][i] for j in range(len(plain_text))] for i in range(len(plain_text[0]))]


    return plain_text


def aes_decryption(cipher_text, secret_key, text_chars, key_size):
    text_matrix=dividing_text(cipher_text, text_chars)
    text_nums=len(text_matrix)
    round_key_matrix=get_round_key_matrix(secret_key,key_size)
    plain_text_matrix=[]
    for i in range(text_nums):
        plain_text_matrix.extend(plain_text_generation(text_matrix[i], round_key_matrix, key_size))

    return plain_text_matrix




def BitVector_to_character_matrix(matrix1):
    char_matrix = [[chr(int(bit_vector.get_bitvector_in_hex(), 16)) for bit_vector in row] for row in matrix1]
    return char_matrix


def BitVector_to_hexadecimal_matrix(matrix1):
    hex_matrix = [[bit_vector.get_bitvector_in_hex() for bit_vector in row] for row in matrix1]
    return hex_matrix

def character_to_BitVector_Matrix(char_matrix):
    bit_matrix = [[BitVector(textstring=char) for char in row] for row in char_matrix]
    return bit_matrix

def string_to_char_matrix(char_string, num_rows, num_columns):
    char_matrix = [[char_string[i*num_columns + j] for j in range(num_columns)] for i in range(num_rows)]
    return char_matrix




# -------------------decryption part-------------------------------------------
def decryption(encrypted_char_string,secretKey):
    text_chars=16
    key_size=128
    decrypted_BitVector_Matrix=aes_decryption(encrypted_char_string,secretKey,text_chars,key_size)
    decrypted_char_matrix=BitVector_to_character_matrix(decrypted_BitVector_Matrix)
    decrypted_char_string = ''.join([''.join(row) for row in decrypted_char_matrix])
    return decrypted_char_string

    



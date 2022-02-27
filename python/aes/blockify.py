'''Functions to blockify a plain text either into 128bit blocks, or to
take a 128bit block and separate into four bytes block'''


def split_text(input):
    return None


def matrixify_col(input):
    ''' Function to take a 16 bytes string input and organize them into
    4 bytes block (i.e. columns)'''
    '''We 'allocate' the four columns, since the byte_list
     are to be ordered column major wise.'''

    block1 = []  # will host the first four bytes of our block
    block2 = []
    block3 = []
    block4 = []  # will host the last four bytes of our block

    # This for loop has been made by Gianluca
    for i in range(4):
        block1.append(ord(input[i]))
        block2.append(ord(input[i+4]))
        block3.append(ord(input[i+8]))
        block4.append(ord(input[i+12]))

    block_list = []  # we allocate the list containing the four columns
    # we populate with the four colomuns
    block_list.extend([block1, block2, block3, block4])
    return block_list


def dematrixify(block_list):
    output = ""  # init an empty string
    for block in block_list:
        for byte in block:
            output += chr(byte)
    return output

# if __name__ == "__main__":
#     test_string = "abcdefghijklmnop"
#     print(test_string)
#     test_list = list(test_string)
#     print(test_list)
#     matr = matrixify_col(test_list)
#     print(matr)
#     dematr = dematrixify(matr)
#     print(dematr)

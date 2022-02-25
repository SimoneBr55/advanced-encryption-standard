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

    for char, i in zip(input, range(16)):
        byte = (ord(char))
        if(i <= 3):  # we add bytes to the blocks based on the posizion. That's quite rude
            block1.append(byte)
        elif(4 <= i <= 7):
            block2.append(byte)
        elif(8 <= i <= 11):
            block3.append(byte)
        elif(12 <= i <= 16):
            block4.append(byte)

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

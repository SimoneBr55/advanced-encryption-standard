from aes import blockify, subbytes, shiftrows

input = "abcdefghijklmnop"

# Checking length of input
if len(input) < 16:
    message_chunks = blockify.split_text()
    print("Padding not yet implemented!")
    print("Length of input is", len(input))
    quit()

'''We are assuming we are working with just a 128bit text
(as blockify.split_text is not yet implemented)'''

block_list = blockify.matrixify_col(input)

first_step = subbytes.subbytes(block_list)
second_step = shiftrows.shiftrows(first_step)
print(second_step)

# ''' Preparation for second step of round'''
# first_point = blockify.dematrixify(first_step)
# second_point = blockify.matrixify_row(first_point)
#

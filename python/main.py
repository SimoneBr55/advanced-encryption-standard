from aes import blockify, subbytes, shiftrows, mixcolumns, cipher

input = "f34481ec3cc627bacd5dc3fb08f273e6"  # This is my plaintext
for i in range(0,32,2):
    print(chr(int(input[i:i+2],16)))

exit()
key   = "00000000000000000000000000000000"

# Checking length of input
if len(input) < 16 or len(input) > 16:
    # message_chunks = blockify.split_text()
    print("Padding not yet implemented!")
    print("Length of input is", len(input))
    quit()

'''We are assuming, we are working with just a 128bit text
(as blockify.split_text is not yet implemented...)'''
print(input)

block_input = blockify.matrixify_col(input)
block_key = blockify.matrixify_col(key)
rounded = cipher.add_key(block_input, block_key)  # add key
input_state = blockify.dematrixify(rounded)
for i in range(1,11):
    # print("Staring round number", i)
    block_list = blockify.matrixify_col(input_state)
    # print("Round start: ", block_list)
    first_step = subbytes.subbytes(block_list)
    # print("First step: ", first_step)
    second_step = shiftrows.shiftrows(first_step)
    # print("Second step: ", second_step)
    if i < 9:
        third_step = mixcolumns.mixcolumns(second_step)
    else:
        third_step = second_step
    # print("Third step: ", third_step)
    rounded = cipher.add_key(third_step, block_key)
    # print("Rounded key added: ", rounded)
    input_state = blockify.dematrixify(rounded)
    print("Temp chars", input_state)


# ''' Preparation for second step of round'''
# first_point = blockify.dematrixify(first_step)
# second_point = blockify.matrixify_row(first_point)
#

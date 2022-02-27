import copy

def add_key(input, key):
    iw = copy.deepcopy(input)
    kw = copy.deepcopy(key)

    for i in range(len(iw)):
        for j in range(len(iw[i])):
            iw[i][j] = iw[i][j] ^ kw[i][j]
    # for col_plain, col_key in zip(input, key):
    #     for elem_plain, elem_key in zip(col_plain, col_key):
    #         test = elem_plain ^ elem_key
    return iw

'''Functions to mix bytes inside columns'''


aes_matrix = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]


def rc_product(matrix, vector):
    '''for now this function takes only one column of the block.
    The separation must be implemented in main. Why are you doing this?
    Because I want to be more general and make use of this function in the
    future :)'''

    '''CAUTION! The matrix MUST BE DEFINED AS LIST OF RAWS!'''

    '''The add operation is XOR.'''
    '''The moltiplication is modular polynomial'''
    # Add check for isometry

    for row in matrix:
        for index, elem in enumerate(row):
            new = elem ^ vector[index]
            )

    return None

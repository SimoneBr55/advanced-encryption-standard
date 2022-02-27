'''
AES is a 128bit symmetric block cipher. It takes 128 bit of message and outputs 128 bit of cipher text. The key can be 128,. 192, 256 bit long.
It relies on a sp network. Bit shifts and permutations are involved.

1. RoundKey
2. SubBytes
3. ShiftRows
4. MixColumns
5. Again from the top

I am going to implement the simple ECB mode right now
'''
import binascii
import aes.subbytes as sb


## FIRST BASIC IMPLEMENTATION
# byte_list = []
# for char, i in zip(input,range(16)):
#     byte_input = bytearray(char, encoding='ascii')
#     byte_list.append(byte_input)

## SECOND MORE STRAIGHT-FORWARD IMPLEMENTATION USEFUL FOR BYTE MANIPULATION


# print([byte_list[i].hex() for i in range(16)])  # just to print hex rappresentation of all byte_list

# first thing SHOULD BE 'xor' the first key. I am not implementing this, because right now i am more interested in the byte manipulation.

### SOME INFO ###
# The irreducible binary polinomial of degree 8 which is used in the modulo operations is:

#   m(x) = x^8 + x^4 + x^3 + x + 1

# SubBytes
# Step 1: Multiplicative inverse in GF(2^8).

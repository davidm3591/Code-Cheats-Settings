# Python - bit calculations

# ------------------------------------------------------------
# Given a number of bits, n, the number of distinct possible
# values that can be represented in n-bits is 2^n


def n_possible_values(nbits: int) -> int:
    return 2 ** nbits


num_of_1_bit = n_possible_values(1)  # 0 or 1 for 1 bit
print(num_of_1_bit)

num_of_8_bits = n_possible_values(8)  # 8 bits = 1 byte
print(num_of_8_bits)

num_of_64_bits = n_possible_values(64)  # 64 bits = 8 bytes
print(num_of_64_bits)

# ASCII encoding could have used only 7 bits
# Using 8 bits left 128 code points unused
num_of_7_bits = n_possible_values(7)  # 7 bits
print(num_of_7_bits)
# ------------------------------------------------------------


# Number of bits required for a given range of code points/values
from math import ceil, log


def n_bits_required(nvalues: int) -> int:
    return ceil(log(nvalues) / log(2))


# for 256 distinct code points/values
bits_for_256 = n_bits_required(256)
print(bits_for_256)

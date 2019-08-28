# ######################################################################
#
# Python - Convert ASCII Character to Binary Representaion
#
# ######################################################################


def brk_ln():
    print("")


def make_bitseq(s: str) -> str:
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)


x_1 = make_bitseq("bits")
print(x_1)

x_2 = make_bitseq("CAPS")
print(x_2)

x_3 = make_bitseq("$25.43")
print(x_3)

x_4 = make_bitseq("~5")
print(x_4)

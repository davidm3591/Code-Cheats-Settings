# ######################################################################
#
# Python - Convert ASCII Character to Binary Representaion
#
# ######################################################################

nl = '\n'


def brk_ln():
    print("")


def make_bitseq(s: str) -> str:
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)


x_1 = make_bitseq("bits")
print(f"x_1 = 'bits'{nl}Binary Representaion: {x_1}{nl}")

x_2 = make_bitseq("CAPS")
print(f"x_2 = 'CAPS'{nl}Binary Representaion: {x_2}{nl}")

x_3 = make_bitseq("$25.43")
print(f"x_3 = $25.43{nl}Binary Representaion: {x_3}{nl}")

x_4 = make_bitseq("~5")
print(f"x_4 = ~5{nl}Binary Representaion: {x_4}{nl}")

# x_5 = make_bitseq("α")

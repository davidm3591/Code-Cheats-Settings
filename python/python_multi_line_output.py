# Practice with mult-line printing
def brk_line():
    brk = 35 * ('-')
    print(brk)


brk_line()

test1 = """Try this
and see if there is a space
between at the top
"""
print(test1)

brk_line()

test2 = """
Try this
and see if there is a space
between at the top
"""
print(test2)

brk_line()

test3 = """
Yup! Sure enough... put the
first line in line with the
variable and opening triple-quote
to avoid a blank line at the top
just like the next example.
"""
print(test3)

brk_line()

test4 = """Lookie here!
First line is in line with
the variable and the opening
triple-quote and, VOILA, no
space at the top.
"""
print(test4)

brk_line()

print("Testing range() function:")
row_count = 5
# range(count)
for num in range(row_count):
    print(num)

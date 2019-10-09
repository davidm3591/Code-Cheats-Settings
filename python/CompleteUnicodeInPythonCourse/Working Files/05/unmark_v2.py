import sys
from unicodedata import normalize, combining

def unmark(text):
    s = normalize('NFD', text)
    s = ''.join(c for c in s if not combining(c))
    return normalize('NFC', s)

def main():
    infile = open(sys.argv[1], encoding='utf-8')
    outfile = open(sys.argv[2], 'w', encoding='utf-8')

    for line in infile:
        outfile.write(unmark(line))

    infile.close()
    outfile.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {} <infile> <outfile>'.format(sys.argv[0]))
    else:
        main()

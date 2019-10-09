import sys
import re
from unicodedata import normalize

MARKS_RE = re.compile('[\u0300-\u036f]')

def unmark(text):
    s = normalize('NFD', text)
    s = MARKS_RE.sub('', s)
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

import sys
from collections import Counter

counter = Counter()

def main():
    with open(sys.argv[1], encoding='utf-8') as infile:
        for line in infile:
            counter.update(line.rstrip())

    with open(sys.argv[2], 'w', encoding='utf-8') as outfile:
        for key in sorted(counter):
            outfile.write('{} → {}\n'.format(key, counter[key]))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {} <infile> <outfile>'.format(sys.argv[0]))
    else:
        main()

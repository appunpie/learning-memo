#Trackのでも問題一問目途中経過
import sys

def main(lines):
    n = int(lines[0])
    print(n)
    for i in range(1, n + 1):
        score = list(map(int, lines[i].split()))
        print(score)

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
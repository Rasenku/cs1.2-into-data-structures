import random
from sys import argv



s = '''The wind whistles past my ears.
Closing my eyes, I lose all my fears.'''.split("\n")


def lines_printed_random(s):

    lines = []

    for i in range(0, len(s)):
        index = random.randint(0, len(s) - 1)
        lines.append(s[index])

    print("\n".join(lines))


if __name__ == '__main__':
    lines_printed_random(s)
